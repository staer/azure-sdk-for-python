# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import asyncio
from collections.abc import AsyncIterator
import functools
import logging
from typing import Any, Union, Optional, AsyncIterator as AsyncIteratorType
import urllib3 # type: ignore

import requests

from azure.core.exceptions import (
    ServiceRequestError,
    ServiceResponseError
)
from azure.core.pipeline import Pipeline
from ._base import HttpRequest, parse_range_header, make_range_header
from ._base_async import (
    AsyncHttpResponse,
    _ResponseStopIteration,
    _iterate_response_content)
from ._requests_basic import RequestsTransportResponse
from ._base_requests_async import RequestsAsyncTransportBase


_LOGGER = logging.getLogger(__name__)


def _get_running_loop():
    try:
        return asyncio.get_running_loop()
    except AttributeError:  # 3.5 / 3.6
        loop = asyncio._get_running_loop()  # pylint: disable=protected-access, no-member
        if loop is None:
            raise RuntimeError('No running event loop')
        return loop


#pylint: disable=too-many-ancestors
class AsyncioRequestsTransport(RequestsAsyncTransportBase):
    """Identical implementation as the synchronous RequestsTransport wrapped in a class with
    asynchronous methods. Uses the built-in asyncio event loop.

    .. admonition:: Example:

        .. literalinclude:: ../samples/test_example_async.py
            :start-after: [START asyncio]
            :end-before: [END asyncio]
            :language: python
            :dedent: 4
            :caption: Asynchronous transport with asyncio.
    """
    async def __aenter__(self):
        return super(AsyncioRequestsTransport, self).__enter__()

    async def __aexit__(self, *exc_details):  # pylint: disable=arguments-differ
        return super(AsyncioRequestsTransport, self).__exit__()

    async def sleep(self, duration):  # pylint:disable=invalid-overridden-method
        await asyncio.sleep(duration)

    async def send(self, request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:  # type: ignore # pylint:disable=invalid-overridden-method
        """Send the request using this HTTP sender.

        :param request: The HttpRequest
        :type request: ~azure.core.pipeline.transport.HttpRequest
        :return: The AsyncHttpResponse
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse

        :keyword requests.Session session: will override the driver session and use yours.
         Should NOT be done unless really required. Anything else is sent straight to requests.
        :keyword dict proxies: will define the proxy to use. Proxy is a dict (protocol, url)
        """
        self.open()
        loop = kwargs.get("loop", _get_running_loop())
        response = None
        error = None # type: Optional[Union[ServiceRequestError, ServiceResponseError]]
        data_to_send = await self._retrieve_request_data(request)
        try:
            response = await loop.run_in_executor(
                None,
                functools.partial(
                    self.session.request,
                    request.method,
                    request.url,
                    headers=request.headers,
                    data=data_to_send,
                    files=request.files,
                    verify=kwargs.pop('connection_verify', self.connection_config.verify),
                    timeout=kwargs.pop('connection_timeout', self.connection_config.timeout),
                    cert=kwargs.pop('connection_cert', self.connection_config.cert),
                    allow_redirects=False,
                    **kwargs))

        except urllib3.exceptions.NewConnectionError as err:
            error = ServiceRequestError(err, error=err)
        except requests.exceptions.ReadTimeout as err:
            error = ServiceResponseError(err, error=err)
        except requests.exceptions.ConnectionError as err:
            if err.args and isinstance(err.args[0], urllib3.exceptions.ProtocolError):
                error = ServiceResponseError(err, error=err)
            else:
                error = ServiceRequestError(err, error=err)
        except requests.RequestException as err:
            error = ServiceRequestError(err, error=err)

        if error:
            raise error

        return AsyncioRequestsTransportResponse(request, response, self.connection_config.data_block_size)


class AsyncioStreamDownloadGenerator(AsyncIterator):
    """Streams the response body data.

    :param pipeline: The pipeline object
    :param response: The response object.
    :param generator iter_content_func: Iterator for response data.
    :param int content_length: size of body in bytes.
    """
    def __init__(self, pipeline: Pipeline, response: AsyncHttpResponse) -> None:
        self.pipeline = pipeline
        self.request = response.request
        self.response = response
        self.block_size = response.block_size
        self.iter_content_func = self.response.internal_response.iter_content(self.block_size)
        self.content_length = int(response.headers.get('Content-Length', 0))
        self.downloaded = 0
        headers = response.headers
        if "x-ms-range" in headers:
            self.range_header = "x-ms-range"
            self.range = headers["x-ms-range"]
        elif "Range" in headers:
            self.range_header = "Range"
            self.range = headers["Range"]
        else:
            self.range_header = None
        self.etag = response.headers['etag'] if 'etag' in headers else None

    def __len__(self):
        return self.content_length

    async def __anext__(self):
        loop = _get_running_loop()
        retry_active = True
        retry_total = 3
        retry_interval = 1  # 1 second
        try:
            chunk = await loop.run_in_executor(
                None,
                _iterate_response_content,
                self.iter_content_func,
            )
            if not chunk:
                raise _ResponseStopIteration()
            self.downloaded += self.block_size
            return chunk
        except _ResponseStopIteration:
            raise StopAsyncIteration()
        except (requests.exceptions.ChunkedEncodingError,
                requests.exceptions.ConnectionError) as ex:
            while retry_active:
                retry_total -= 1
                if retry_total <= 0:
                    _LOGGER.warning("Unable to stream download: %s", ex)
                    raise ex
                if not self.etag:
                    _LOGGER.warning("Unable to stream download: %s", ex)
                    raise ex
                await asyncio.sleep(retry_interval)
                headers = self.request.headers.copy()
                if not self.range_header:
                    range_header = {'range': 'bytes=' + str(self.downloaded) + '-'}
                else:
                    range_header = {self.range_header: make_range_header(self.range, self.downloaded)}
                range_header.update({'If-Match': self.etag})
                headers.update(range_header)
                try:
                    resp = await self.pipeline.run(self.request, stream=True, headers=headers)
                    if not resp.http_response:
                        continue
                    if resp.http_response.status_code == 412:
                        continue
                    self.response = resp.http_response
                    chunk = await loop.run_in_executor(
                        None,
                        _iterate_response_content,
                        self.iter_content_func,
                    )
                    if not chunk:
                        await self.response.internal_response.close()
                        raise StopAsyncIteration()
                    self.downloaded += self.block_size
                    return chunk
                except StopAsyncIteration:
                    raise StopAsyncIteration()
                except Exception:  # pylint: disable=broad-except
                    continue
        except requests.exceptions.StreamConsumedError:
            raise
        except Exception as err:
            _LOGGER.warning("Unable to stream download: %s", err)
            raise

class AsyncioRequestsTransportResponse(AsyncHttpResponse, RequestsTransportResponse): # type: ignore
    """Asynchronous streaming of data from the response.
    """
    def stream_download(self, pipeline) -> AsyncIteratorType[bytes]: # type: ignore
        """Generator for streaming request body data."""
        return AsyncioStreamDownloadGenerator(pipeline, self) # type: ignore
