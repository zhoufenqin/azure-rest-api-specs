# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ApplicationInsightsComponent
    from ._models_py3 import ApplicationInsightsComponentListResult
    from ._models_py3 import ComponentPurgeBody
    from ._models_py3 import ComponentPurgeBodyFilters
    from ._models_py3 import ComponentPurgeResponse
    from ._models_py3 import ComponentPurgeStatusResponse
    from ._models_py3 import ComponentsResource
    from ._models_py3 import ErrorAdditionalInfo
    from ._models_py3 import ErrorDetail
    from ._models_py3 import ErrorResponse
    from ._models_py3 import PrivateLinkScopedResource
    from ._models_py3 import TagsResource
except (SyntaxError, ImportError):
    from ._models import ApplicationInsightsComponent  # type: ignore
    from ._models import ApplicationInsightsComponentListResult  # type: ignore
    from ._models import ComponentPurgeBody  # type: ignore
    from ._models import ComponentPurgeBodyFilters  # type: ignore
    from ._models import ComponentPurgeResponse  # type: ignore
    from ._models import ComponentPurgeStatusResponse  # type: ignore
    from ._models import ComponentsResource  # type: ignore
    from ._models import ErrorAdditionalInfo  # type: ignore
    from ._models import ErrorDetail  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import PrivateLinkScopedResource  # type: ignore
    from ._models import TagsResource  # type: ignore

from ._application_insights_management_client_enums import (
    ApplicationType,
    FlowType,
    IngestionMode,
    PublicNetworkAccessType,
    PurgeState,
    RequestSource,
)

__all__ = [
    'ApplicationInsightsComponent',
    'ApplicationInsightsComponentListResult',
    'ComponentPurgeBody',
    'ComponentPurgeBodyFilters',
    'ComponentPurgeResponse',
    'ComponentPurgeStatusResponse',
    'ComponentsResource',
    'ErrorAdditionalInfo',
    'ErrorDetail',
    'ErrorResponse',
    'PrivateLinkScopedResource',
    'TagsResource',
    'ApplicationType',
    'FlowType',
    'IngestionMode',
    'PublicNetworkAccessType',
    'PurgeState',
    'RequestSource',
]