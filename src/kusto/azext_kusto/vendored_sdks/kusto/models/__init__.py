# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AttachedDatabaseConfiguration
    from ._models_py3 import AttachedDatabaseConfigurationListResult
    from ._models_py3 import AzureCapacity
    from ._models_py3 import AzureResourceSku
    from ._models_py3 import AzureSku
    from ._models_py3 import CheckNameRequest
    from ._models_py3 import CheckNameResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import Cluster
    from ._models_py3 import ClusterCheckNameRequest
    from ._models_py3 import ClusterListResult
    from ._models_py3 import ClusterPrincipalAssignment
    from ._models_py3 import ClusterPrincipalAssignmentCheckNameRequest
    from ._models_py3 import ClusterPrincipalAssignmentListResult
    from ._models_py3 import ClusterUpdate
    from ._models_py3 import ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties
    from ._models_py3 import DataConnection
    from ._models_py3 import DataConnectionCheckNameRequest
    from ._models_py3 import DataConnectionListResult
    from ._models_py3 import DataConnectionValidation
    from ._models_py3 import DataConnectionValidationListResult
    from ._models_py3 import DataConnectionValidationResult
    from ._models_py3 import Database
    from ._models_py3 import DatabaseListResult
    from ._models_py3 import DatabasePrincipal
    from ._models_py3 import DatabasePrincipalAssignment
    from ._models_py3 import DatabasePrincipalAssignmentCheckNameRequest
    from ._models_py3 import DatabasePrincipalAssignmentListResult
    from ._models_py3 import DatabasePrincipalListRequest
    from ._models_py3 import DatabasePrincipalListResult
    from ._models_py3 import DatabaseStatistics
    from ._models_py3 import DiagnoseVirtualNetworkResult
    from ._models_py3 import EventGridDataConnection
    from ._models_py3 import EventHubDataConnection
    from ._models_py3 import FollowerDatabaseDefinition
    from ._models_py3 import FollowerDatabaseListResult
    from ._models_py3 import Identity
    from ._models_py3 import IotHubDataConnection
    from ._models_py3 import KeyVaultProperties
    from ._models_py3 import LanguageExtension
    from ._models_py3 import LanguageExtensionsList
    from ._models_py3 import ListResourceSkusResult
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import OperationListResult
    from ._models_py3 import OperationResult
    from ._models_py3 import OptimizedAutoscale
    from ._models_py3 import ProxyResource
    from ._models_py3 import ReadOnlyFollowingDatabase
    from ._models_py3 import ReadWriteDatabase
    from ._models_py3 import Resource
    from ._models_py3 import Script
    from ._models_py3 import ScriptCheckNameRequest
    from ._models_py3 import ScriptListResult
    from ._models_py3 import SkuDescription
    from ._models_py3 import SkuDescriptionList
    from ._models_py3 import SkuLocationInfoItem
    from ._models_py3 import SystemData
    from ._models_py3 import TableLevelSharingProperties
    from ._models_py3 import TrackedResource
    from ._models_py3 import TrustedExternalTenant
    from ._models_py3 import VirtualNetworkConfiguration
except (SyntaxError, ImportError):
    from ._models import AttachedDatabaseConfiguration  # type: ignore
    from ._models import AttachedDatabaseConfigurationListResult  # type: ignore
    from ._models import AzureCapacity  # type: ignore
    from ._models import AzureResourceSku  # type: ignore
    from ._models import AzureSku  # type: ignore
    from ._models import CheckNameRequest  # type: ignore
    from ._models import CheckNameResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import Cluster  # type: ignore
    from ._models import ClusterCheckNameRequest  # type: ignore
    from ._models import ClusterListResult  # type: ignore
    from ._models import ClusterPrincipalAssignment  # type: ignore
    from ._models import ClusterPrincipalAssignmentCheckNameRequest  # type: ignore
    from ._models import ClusterPrincipalAssignmentListResult  # type: ignore
    from ._models import ClusterUpdate  # type: ignore
    from ._models import ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties  # type: ignore
    from ._models import DataConnection  # type: ignore
    from ._models import DataConnectionCheckNameRequest  # type: ignore
    from ._models import DataConnectionListResult  # type: ignore
    from ._models import DataConnectionValidation  # type: ignore
    from ._models import DataConnectionValidationListResult  # type: ignore
    from ._models import DataConnectionValidationResult  # type: ignore
    from ._models import Database  # type: ignore
    from ._models import DatabaseListResult  # type: ignore
    from ._models import DatabasePrincipal  # type: ignore
    from ._models import DatabasePrincipalAssignment  # type: ignore
    from ._models import DatabasePrincipalAssignmentCheckNameRequest  # type: ignore
    from ._models import DatabasePrincipalAssignmentListResult  # type: ignore
    from ._models import DatabasePrincipalListRequest  # type: ignore
    from ._models import DatabasePrincipalListResult  # type: ignore
    from ._models import DatabaseStatistics  # type: ignore
    from ._models import DiagnoseVirtualNetworkResult  # type: ignore
    from ._models import EventGridDataConnection  # type: ignore
    from ._models import EventHubDataConnection  # type: ignore
    from ._models import FollowerDatabaseDefinition  # type: ignore
    from ._models import FollowerDatabaseListResult  # type: ignore
    from ._models import Identity  # type: ignore
    from ._models import IotHubDataConnection  # type: ignore
    from ._models import KeyVaultProperties  # type: ignore
    from ._models import LanguageExtension  # type: ignore
    from ._models import LanguageExtensionsList  # type: ignore
    from ._models import ListResourceSkusResult  # type: ignore
    from ._models import Operation  # type: ignore
    from ._models import OperationDisplay  # type: ignore
    from ._models import OperationListResult  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import OptimizedAutoscale  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import ReadOnlyFollowingDatabase  # type: ignore
    from ._models import ReadWriteDatabase  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import Script  # type: ignore
    from ._models import ScriptCheckNameRequest  # type: ignore
    from ._models import ScriptListResult  # type: ignore
    from ._models import SkuDescription  # type: ignore
    from ._models import SkuDescriptionList  # type: ignore
    from ._models import SkuLocationInfoItem  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TableLevelSharingProperties  # type: ignore
    from ._models import TrackedResource  # type: ignore
    from ._models import TrustedExternalTenant  # type: ignore
    from ._models import VirtualNetworkConfiguration  # type: ignore

from ._kusto_management_client_enums import (
    AzureScaleType,
    AzureSkuName,
    AzureSkuTier,
    BlobStorageEventType,
    ClusterPrincipalRole,
    Compression,
    CreatedByType,
    DataConnectionKind,
    DatabasePrincipalRole,
    DatabasePrincipalType,
    DefaultPrincipalsModificationKind,
    EngineType,
    EventGridDataFormat,
    EventHubDataFormat,
    IdentityType,
    IotHubDataFormat,
    Kind,
    LanguageExtensionName,
    PrincipalType,
    PrincipalsModificationKind,
    ProvisioningState,
    Reason,
    State,
    Status,
    Type,
)

__all__ = [
    'AttachedDatabaseConfiguration',
    'AttachedDatabaseConfigurationListResult',
    'AzureCapacity',
    'AzureResourceSku',
    'AzureSku',
    'CheckNameRequest',
    'CheckNameResult',
    'CloudErrorBody',
    'Cluster',
    'ClusterCheckNameRequest',
    'ClusterListResult',
    'ClusterPrincipalAssignment',
    'ClusterPrincipalAssignmentCheckNameRequest',
    'ClusterPrincipalAssignmentListResult',
    'ClusterUpdate',
    'ComponentsSgqdofSchemasIdentityPropertiesUserassignedidentitiesAdditionalproperties',
    'DataConnection',
    'DataConnectionCheckNameRequest',
    'DataConnectionListResult',
    'DataConnectionValidation',
    'DataConnectionValidationListResult',
    'DataConnectionValidationResult',
    'Database',
    'DatabaseListResult',
    'DatabasePrincipal',
    'DatabasePrincipalAssignment',
    'DatabasePrincipalAssignmentCheckNameRequest',
    'DatabasePrincipalAssignmentListResult',
    'DatabasePrincipalListRequest',
    'DatabasePrincipalListResult',
    'DatabaseStatistics',
    'DiagnoseVirtualNetworkResult',
    'EventGridDataConnection',
    'EventHubDataConnection',
    'FollowerDatabaseDefinition',
    'FollowerDatabaseListResult',
    'Identity',
    'IotHubDataConnection',
    'KeyVaultProperties',
    'LanguageExtension',
    'LanguageExtensionsList',
    'ListResourceSkusResult',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationResult',
    'OptimizedAutoscale',
    'ProxyResource',
    'ReadOnlyFollowingDatabase',
    'ReadWriteDatabase',
    'Resource',
    'Script',
    'ScriptCheckNameRequest',
    'ScriptListResult',
    'SkuDescription',
    'SkuDescriptionList',
    'SkuLocationInfoItem',
    'SystemData',
    'TableLevelSharingProperties',
    'TrackedResource',
    'TrustedExternalTenant',
    'VirtualNetworkConfiguration',
    'AzureScaleType',
    'AzureSkuName',
    'AzureSkuTier',
    'BlobStorageEventType',
    'ClusterPrincipalRole',
    'Compression',
    'CreatedByType',
    'DataConnectionKind',
    'DatabasePrincipalRole',
    'DatabasePrincipalType',
    'DefaultPrincipalsModificationKind',
    'EngineType',
    'EventGridDataFormat',
    'EventHubDataFormat',
    'IdentityType',
    'IotHubDataFormat',
    'Kind',
    'LanguageExtensionName',
    'PrincipalType',
    'PrincipalsModificationKind',
    'ProvisioningState',
    'Reason',
    'State',
    'Status',
    'Type',
]