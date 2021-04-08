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

try:
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import Backend
    from ._models_py3 import BackendPool
    from ._models_py3 import BackendPoolListResult
    from ._models_py3 import BackendPoolsSettings
    from ._models_py3 import BackendPoolUpdateParameters
    from ._models_py3 import CacheConfiguration
    from ._models_py3 import CheckNameAvailabilityInput
    from ._models_py3 import CheckNameAvailabilityOutput
    from ._models_py3 import CustomHttpsConfiguration
    from ._models_py3 import CustomRule
    from ._models_py3 import CustomRuleList
    from ._models_py3 import Endpoint
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import Experiment
    from ._models_py3 import ExperimentUpdateModel
    from ._models_py3 import ForwardingConfiguration
    from ._models_py3 import FrontDoor
    from ._models_py3 import FrontDoorUpdateParameters
    from ._models_py3 import FrontendEndpoint
    from ._models_py3 import FrontendEndpointLink
    from ._models_py3 import FrontendEndpointUpdateParameters
    from ._models_py3 import FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink
    from ._models_py3 import HeaderAction
    from ._models_py3 import HealthProbeSettingsListResult
    from ._models_py3 import HealthProbeSettingsModel
    from ._models_py3 import HealthProbeSettingsUpdateParameters
    from ._models_py3 import KeyVaultCertificateSourceParametersVault
    from ._models_py3 import LatencyMetric
    from ._models_py3 import LatencyScorecard
    from ._models_py3 import LoadBalancingSettingsListResult
    from ._models_py3 import LoadBalancingSettingsModel
    from ._models_py3 import LoadBalancingSettingsUpdateParameters
    from ._models_py3 import ManagedRuleDefinition
    from ._models_py3 import ManagedRuleExclusion
    from ._models_py3 import ManagedRuleGroupDefinition
    from ._models_py3 import ManagedRuleGroupOverride
    from ._models_py3 import ManagedRuleOverride
    from ._models_py3 import ManagedRuleSet
    from ._models_py3 import ManagedRuleSetDefinition
    from ._models_py3 import ManagedRuleSetList
    from ._models_py3 import MatchCondition
    from ._models_py3 import PolicySettings
    from ._models_py3 import PreconfiguredEndpoint
    from ._models_py3 import Profile
    from ._models_py3 import ProfileUpdateModel
    from ._models_py3 import PurgeParameters
    from ._models_py3 import RedirectConfiguration
    from ._models_py3 import Resource
    from ._models_py3 import RouteConfiguration
    from ._models_py3 import RoutingRule
    from ._models_py3 import RoutingRuleLink
    from ._models_py3 import RoutingRuleListResult
    from ._models_py3 import RoutingRuleUpdateParameters
    from ._models_py3 import RoutingRuleUpdateParametersWebApplicationFirewallPolicyLink
    from ._models_py3 import RulesEngine
    from ._models_py3 import RulesEngineAction
    from ._models_py3 import RulesEngineMatchCondition
    from ._models_py3 import RulesEngineRule
    from ._models_py3 import RulesEngineUpdateParameters
    from ._models_py3 import SecurityPolicyLink
    from ._models_py3 import Sku
    from ._models_py3 import SubResource
    from ._models_py3 import TagsObject
    from ._models_py3 import Timeseries
    from ._models_py3 import TimeseriesDataPoint
    from ._models_py3 import ValidateCustomDomainInput
    from ._models_py3 import ValidateCustomDomainOutput
    from ._models_py3 import WebApplicationFirewallPolicy
except (SyntaxError, ImportError):
    from ._models import AzureAsyncOperationResult
    from ._models import Backend
    from ._models import BackendPool
    from ._models import BackendPoolListResult
    from ._models import BackendPoolsSettings
    from ._models import BackendPoolUpdateParameters
    from ._models import CacheConfiguration
    from ._models import CheckNameAvailabilityInput
    from ._models import CheckNameAvailabilityOutput
    from ._models import CustomHttpsConfiguration
    from ._models import CustomRule
    from ._models import CustomRuleList
    from ._models import Endpoint
    from ._models import Error
    from ._models import ErrorDetails
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import Experiment
    from ._models import ExperimentUpdateModel
    from ._models import ForwardingConfiguration
    from ._models import FrontDoor
    from ._models import FrontDoorUpdateParameters
    from ._models import FrontendEndpoint
    from ._models import FrontendEndpointLink
    from ._models import FrontendEndpointUpdateParameters
    from ._models import FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink
    from ._models import HeaderAction
    from ._models import HealthProbeSettingsListResult
    from ._models import HealthProbeSettingsModel
    from ._models import HealthProbeSettingsUpdateParameters
    from ._models import KeyVaultCertificateSourceParametersVault
    from ._models import LatencyMetric
    from ._models import LatencyScorecard
    from ._models import LoadBalancingSettingsListResult
    from ._models import LoadBalancingSettingsModel
    from ._models import LoadBalancingSettingsUpdateParameters
    from ._models import ManagedRuleDefinition
    from ._models import ManagedRuleExclusion
    from ._models import ManagedRuleGroupDefinition
    from ._models import ManagedRuleGroupOverride
    from ._models import ManagedRuleOverride
    from ._models import ManagedRuleSet
    from ._models import ManagedRuleSetDefinition
    from ._models import ManagedRuleSetList
    from ._models import MatchCondition
    from ._models import PolicySettings
    from ._models import PreconfiguredEndpoint
    from ._models import Profile
    from ._models import ProfileUpdateModel
    from ._models import PurgeParameters
    from ._models import RedirectConfiguration
    from ._models import Resource
    from ._models import RouteConfiguration
    from ._models import RoutingRule
    from ._models import RoutingRuleLink
    from ._models import RoutingRuleListResult
    from ._models import RoutingRuleUpdateParameters
    from ._models import RoutingRuleUpdateParametersWebApplicationFirewallPolicyLink
    from ._models import RulesEngine
    from ._models import RulesEngineAction
    from ._models import RulesEngineMatchCondition
    from ._models import RulesEngineRule
    from ._models import RulesEngineUpdateParameters
    from ._models import SecurityPolicyLink
    from ._models import Sku
    from ._models import SubResource
    from ._models import TagsObject
    from ._models import Timeseries
    from ._models import TimeseriesDataPoint
    from ._models import ValidateCustomDomainInput
    from ._models import ValidateCustomDomainOutput
    from ._models import WebApplicationFirewallPolicy
from ._paged_models import ExperimentPaged
from ._paged_models import FrontDoorPaged
from ._paged_models import FrontendEndpointPaged
from ._paged_models import ManagedRuleSetDefinitionPaged
from ._paged_models import PreconfiguredEndpointPaged
from ._paged_models import ProfilePaged
from ._paged_models import RulesEnginePaged
from ._paged_models import WebApplicationFirewallPolicyPaged
from ._front_door_management_client_enums import (
    NetworkOperationStatus,
    NetworkExperimentResourceState,
    State,
    AggregationInterval,
    TimeseriesType,
    EndpointType,
    FrontDoorResourceState,
    CustomHttpsProvisioningState,
    CustomHttpsProvisioningSubstate,
    FrontDoorCertificateSource,
    MinimumTLSVersion,
    FrontDoorCertificateType,
    EnforceCertificateNameCheckEnabledState,
    FrontDoorEnabledState,
    FrontDoorProtocol,
    RoutingRuleEnabledState,
    FrontDoorForwardingProtocol,
    FrontDoorQuery,
    DynamicCompressionEnabled,
    FrontDoorRedirectType,
    FrontDoorRedirectProtocol,
    PrivateEndpointStatus,
    BackendEnabledState,
    FrontDoorHealthProbeMethod,
    HealthProbeEnabled,
    SessionAffinityEnabledState,
    HeaderActionType,
    RulesEngineMatchVariable,
    RulesEngineOperator,
    Transform,
    MatchProcessingBehavior,
    ResourceType,
    Availability,
    PolicyEnabledState,
    PolicyMode,
    PolicyRequestBodyCheck,
    CustomRuleEnabledState,
    RuleType,
    MatchVariable,
    Operator,
    TransformType,
    ActionType,
    ManagedRuleSetActionType,
    ManagedRuleExclusionMatchVariable,
    ManagedRuleExclusionSelectorMatchOperator,
    ManagedRuleEnabledState,
    PolicyResourceState,
    SkuName,
    LatencyScorecardAggregationInterval,
    TimeseriesAggregationInterval,
)

__all__ = [
    'AzureAsyncOperationResult',
    'Backend',
    'BackendPool',
    'BackendPoolListResult',
    'BackendPoolsSettings',
    'BackendPoolUpdateParameters',
    'CacheConfiguration',
    'CheckNameAvailabilityInput',
    'CheckNameAvailabilityOutput',
    'CustomHttpsConfiguration',
    'CustomRule',
    'CustomRuleList',
    'Endpoint',
    'Error',
    'ErrorDetails',
    'ErrorResponse', 'ErrorResponseException',
    'Experiment',
    'ExperimentUpdateModel',
    'ForwardingConfiguration',
    'FrontDoor',
    'FrontDoorUpdateParameters',
    'FrontendEndpoint',
    'FrontendEndpointLink',
    'FrontendEndpointUpdateParameters',
    'FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink',
    'HeaderAction',
    'HealthProbeSettingsListResult',
    'HealthProbeSettingsModel',
    'HealthProbeSettingsUpdateParameters',
    'KeyVaultCertificateSourceParametersVault',
    'LatencyMetric',
    'LatencyScorecard',
    'LoadBalancingSettingsListResult',
    'LoadBalancingSettingsModel',
    'LoadBalancingSettingsUpdateParameters',
    'ManagedRuleDefinition',
    'ManagedRuleExclusion',
    'ManagedRuleGroupDefinition',
    'ManagedRuleGroupOverride',
    'ManagedRuleOverride',
    'ManagedRuleSet',
    'ManagedRuleSetDefinition',
    'ManagedRuleSetList',
    'MatchCondition',
    'PolicySettings',
    'PreconfiguredEndpoint',
    'Profile',
    'ProfileUpdateModel',
    'PurgeParameters',
    'RedirectConfiguration',
    'Resource',
    'RouteConfiguration',
    'RoutingRule',
    'RoutingRuleLink',
    'RoutingRuleListResult',
    'RoutingRuleUpdateParameters',
    'RoutingRuleUpdateParametersWebApplicationFirewallPolicyLink',
    'RulesEngine',
    'RulesEngineAction',
    'RulesEngineMatchCondition',
    'RulesEngineRule',
    'RulesEngineUpdateParameters',
    'SecurityPolicyLink',
    'Sku',
    'SubResource',
    'TagsObject',
    'Timeseries',
    'TimeseriesDataPoint',
    'ValidateCustomDomainInput',
    'ValidateCustomDomainOutput',
    'WebApplicationFirewallPolicy',
    'ProfilePaged',
    'PreconfiguredEndpointPaged',
    'ExperimentPaged',
    'FrontDoorPaged',
    'FrontendEndpointPaged',
    'RulesEnginePaged',
    'WebApplicationFirewallPolicyPaged',
    'ManagedRuleSetDefinitionPaged',
    'NetworkOperationStatus',
    'NetworkExperimentResourceState',
    'State',
    'AggregationInterval',
    'TimeseriesType',
    'EndpointType',
    'FrontDoorResourceState',
    'CustomHttpsProvisioningState',
    'CustomHttpsProvisioningSubstate',
    'FrontDoorCertificateSource',
    'MinimumTLSVersion',
    'FrontDoorCertificateType',
    'EnforceCertificateNameCheckEnabledState',
    'FrontDoorEnabledState',
    'FrontDoorProtocol',
    'RoutingRuleEnabledState',
    'FrontDoorForwardingProtocol',
    'FrontDoorQuery',
    'DynamicCompressionEnabled',
    'FrontDoorRedirectType',
    'FrontDoorRedirectProtocol',
    'PrivateEndpointStatus',
    'BackendEnabledState',
    'FrontDoorHealthProbeMethod',
    'HealthProbeEnabled',
    'SessionAffinityEnabledState',
    'HeaderActionType',
    'RulesEngineMatchVariable',
    'RulesEngineOperator',
    'Transform',
    'MatchProcessingBehavior',
    'ResourceType',
    'Availability',
    'PolicyEnabledState',
    'PolicyMode',
    'PolicyRequestBodyCheck',
    'CustomRuleEnabledState',
    'RuleType',
    'MatchVariable',
    'Operator',
    'TransformType',
    'ActionType',
    'ManagedRuleSetActionType',
    'ManagedRuleExclusionMatchVariable',
    'ManagedRuleExclusionSelectorMatchOperator',
    'ManagedRuleEnabledState',
    'PolicyResourceState',
    'SkuName',
    'LatencyScorecardAggregationInterval',
    'TimeseriesAggregationInterval',
]