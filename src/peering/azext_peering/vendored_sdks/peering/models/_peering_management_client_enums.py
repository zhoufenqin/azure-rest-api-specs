# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ConnectionState(str, Enum):
    """The state of the connection.
    """

    none = "None"
    pending_approval = "PendingApproval"
    approved = "Approved"
    provisioning_started = "ProvisioningStarted"
    provisioning_failed = "ProvisioningFailed"
    provisioning_completed = "ProvisioningCompleted"
    validating = "Validating"
    active = "Active"

class DirectPeeringType(str, Enum):
    """The type of direct peering.
    """

    edge = "Edge"
    transit = "Transit"
    cdn = "Cdn"
    internal = "Internal"
    ix = "Ix"
    ix_rs = "IxRs"

class Enum0(str, Enum):

    available = "Available"
    unavailable = "Unavailable"

class Enum1(str, Enum):

    direct = "Direct"
    exchange = "Exchange"

class Enum14(str, Enum):

    direct = "Direct"
    exchange = "Exchange"

class Enum15(str, Enum):

    edge = "Edge"
    transit = "Transit"
    cdn = "Cdn"
    internal = "Internal"
    ix = "Ix"
    ix_rs = "IxRs"

class Family(str, Enum):
    """The family of the peering SKU.
    """

    direct = "Direct"
    exchange = "Exchange"

class Kind(str, Enum):
    """The kind of the peering.
    """

    direct = "Direct"
    exchange = "Exchange"

class LearnedType(str, Enum):
    """The prefix learned type
    """

    none = "None"
    via_service_provider = "ViaServiceProvider"
    via_session = "ViaSession"

class PrefixValidationState(str, Enum):
    """The prefix validation state.
    """

    none = "None"
    invalid = "Invalid"
    verified = "Verified"
    failed = "Failed"
    pending = "Pending"
    warning = "Warning"
    unknown = "Unknown"

class ProvisioningState(str, Enum):
    """The provisioning state of the resource.
    """

    succeeded = "Succeeded"
    updating = "Updating"
    deleting = "Deleting"
    failed = "Failed"

class Role(str, Enum):
    """The role of the contact.
    """

    noc = "Noc"
    policy = "Policy"
    technical = "Technical"
    service = "Service"
    escalation = "Escalation"
    other = "Other"

class SessionAddressProvider(str, Enum):
    """The field indicating if Microsoft provides session ip addresses.
    """

    microsoft = "Microsoft"
    peer = "Peer"

class SessionStateV4(str, Enum):
    """The state of the IPv4 session.
    """

    none = "None"
    idle = "Idle"
    connect = "Connect"
    active = "Active"
    open_sent = "OpenSent"
    open_confirm = "OpenConfirm"
    open_received = "OpenReceived"
    established = "Established"
    pending_add = "PendingAdd"
    pending_update = "PendingUpdate"
    pending_remove = "PendingRemove"

class SessionStateV6(str, Enum):
    """The state of the IPv6 session.
    """

    none = "None"
    idle = "Idle"
    connect = "Connect"
    active = "Active"
    open_sent = "OpenSent"
    open_confirm = "OpenConfirm"
    open_received = "OpenReceived"
    established = "Established"
    pending_add = "PendingAdd"
    pending_update = "PendingUpdate"
    pending_remove = "PendingRemove"

class Size(str, Enum):
    """The size of the peering SKU.
    """

    free = "Free"
    metered = "Metered"
    unlimited = "Unlimited"

class Tier(str, Enum):
    """The tier of the peering SKU.
    """

    basic = "Basic"
    premium = "Premium"

class ValidationState(str, Enum):
    """The validation state of the ASN associated with the peer.
    """

    none = "None"
    pending = "Pending"
    approved = "Approved"
    failed = "Failed"