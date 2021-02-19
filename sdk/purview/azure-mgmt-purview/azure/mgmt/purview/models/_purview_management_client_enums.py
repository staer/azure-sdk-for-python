# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class Name(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the sku name.
    """

    STANDARD = "Standard"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the state of the provisioning.
    """

    UNKNOWN = "Unknown"
    CREATING = "Creating"
    MOVING = "Moving"
    DELETING = "Deleting"
    SOFT_DELETING = "SoftDeleting"
    SOFT_DELETED = "SoftDeleted"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"

class PublicNetworkAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets or sets the public network access.
    """

    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"

class Reason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason the name is not available.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class ScopeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TENANT = "Tenant"
    SUBSCRIPTION = "Subscription"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status.
    """

    UNKNOWN = "Unknown"
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"

class Type(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Identity Type
    """

    SYSTEM_ASSIGNED = "SystemAssigned"