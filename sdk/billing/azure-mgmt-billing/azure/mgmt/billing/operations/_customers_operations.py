# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class CustomersOperations(object):
    """CustomersOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The version of the API to be used with the client request. The current version is 2020-05-01. Constant value: "2020-05-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-05-01"

        self.config = config

    def list_by_billing_profile(
            self, billing_account_name, billing_profile_name, search=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the customers that are billed to a billing profile. The operation
        is supported only for billing accounts with agreement type Microsoft
        Partner Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param billing_profile_name: The ID that uniquely identifies a billing
         profile.
        :type billing_profile_name: str
        :param search: Used for searching customers by their name. Any
         customer with name containing the search text will be included in the
         response
        :type search: str
        :param filter: May be used to filter the list of customers.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Customer
        :rtype:
         ~azure.mgmt.billing.models.CustomerPaged[~azure.mgmt.billing.models.Customer]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_billing_profile.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
                    'billingProfileName': self._serialize.url("billing_profile_name", billing_profile_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if search is not None:
                    query_parameters['$search'] = self._serialize.query("search", search, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.CustomerPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_billing_profile.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/customers'}

    def list_by_billing_account(
            self, billing_account_name, search=None, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists the customers that are billed to a billing account. The operation
        is supported only for billing accounts with agreement type Microsoft
        Partner Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param search: Used for searching customers by their name. Any
         customer with name containing the search text will be included in the
         response
        :type search: str
        :param filter: May be used to filter the list of customers.
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of Customer
        :rtype:
         ~azure.mgmt.billing.models.CustomerPaged[~azure.mgmt.billing.models.Customer]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_billing_account.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if search is not None:
                    query_parameters['$search'] = self._serialize.query("search", search, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.CustomerPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list_by_billing_account.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers'}

    def get(
            self, billing_account_name, customer_name, expand=None, custom_headers=None, raw=False, **operation_config):
        """Gets a customer by its ID. The operation is supported only for billing
        accounts with agreement type Microsoft Partner Agreement.

        :param billing_account_name: The ID that uniquely identifies a billing
         account.
        :type billing_account_name: str
        :param customer_name: The ID that uniquely identifies a customer.
        :type customer_name: str
        :param expand: May be used to expand enabledAzurePlans and resellers
        :type expand: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Customer or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.Customer or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'customerName': self._serialize.url("customer_name", customer_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Customer', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}'}