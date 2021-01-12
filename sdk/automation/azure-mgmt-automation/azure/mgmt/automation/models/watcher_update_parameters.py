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

from msrest.serialization import Model


class WatcherUpdateParameters(Model):
    """WatcherUpdateParameters.

    :param execution_frequency_in_seconds: Gets or sets the frequency at which
     the watcher is invoked.
    :type execution_frequency_in_seconds: long
    :param name: Gets or sets the name of the resource.
    :type name: str
    """

    _attribute_map = {
        'execution_frequency_in_seconds': {'key': 'properties.executionFrequencyInSeconds', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WatcherUpdateParameters, self).__init__(**kwargs)
        self.execution_frequency_in_seconds = kwargs.get('execution_frequency_in_seconds', None)
        self.name = kwargs.get('name', None)