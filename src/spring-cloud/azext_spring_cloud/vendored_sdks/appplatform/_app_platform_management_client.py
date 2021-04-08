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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration import AppPlatformManagementClientConfiguration



class AppPlatformManagementClient(MultiApiClientMixin, SDKClient):
    """REST API for Azure Spring Cloud

    This ready contains multiple API versions, to help you deal with all Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, uses latest API version available on public Azure.
    For production, you should stick a particular api-version and/or profile.
    The profile sets a mapping between the operation group and an API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :ivar config: Configuration for client.
    :vartype config: AppPlatformManagementClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION = '2020-07-01'
    _PROFILE_TAG = "azure.mgmt.appplatform.AppPlatformManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'sku': '2019-05-01-preview',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, subscription_id, api_version=None, base_url=None, profile=KnownProfiles.default):
        self.config = AppPlatformManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AppPlatformManagementClient, self).__init__(
            credentials,
            self.config,
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2019-05-01-preview: :mod:`v2019_05_01_preview.models<azure.mgmt.appplatform.v2019_05_01_preview.models>`
           * 2020-07-01: :mod:`v2020_07_01.models<azure.mgmt.appplatform.v2020_07_01.models>`
           * 2020-11-01-preview: :mod:`v2020_11_01_preview.models<azure.mgmt.appplatform.v2020_11_01_preview.models>`
        """
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview import models
            return models
        elif api_version == '2020-07-01':
            from .v2020_07_01 import models
            return models
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    @property
    def apps(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.AppsOperations>`
           * 2020-07-01: :class:`AppsOperations<azure.mgmt.appplatform.v2020_07_01.operations.AppsOperations>`
           * 2020-11-01-preview: :class:`AppsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.AppsOperations>`
        """
        api_version = self._get_api_version('apps')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import AppsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import AppsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import AppsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def bindings(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.BindingsOperations>`
           * 2020-07-01: :class:`BindingsOperations<azure.mgmt.appplatform.v2020_07_01.operations.BindingsOperations>`
           * 2020-11-01-preview: :class:`BindingsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.BindingsOperations>`
        """
        api_version = self._get_api_version('bindings')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import BindingsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import BindingsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import BindingsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def certificates(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.CertificatesOperations>`
           * 2020-07-01: :class:`CertificatesOperations<azure.mgmt.appplatform.v2020_07_01.operations.CertificatesOperations>`
           * 2020-11-01-preview: :class:`CertificatesOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.CertificatesOperations>`
        """
        api_version = self._get_api_version('certificates')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import CertificatesOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import CertificatesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import CertificatesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def config_servers(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2020_07_01.operations.ConfigServersOperations>`
           * 2020-11-01-preview: :class:`ConfigServersOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.ConfigServersOperations>`
        """
        api_version = self._get_api_version('config_servers')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import ConfigServersOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ConfigServersOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def custom_domains(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.CustomDomainsOperations>`
           * 2020-07-01: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2020_07_01.operations.CustomDomainsOperations>`
           * 2020-11-01-preview: :class:`CustomDomainsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.CustomDomainsOperations>`
        """
        api_version = self._get_api_version('custom_domains')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import CustomDomainsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import CustomDomainsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deployments(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.DeploymentsOperations>`
           * 2020-07-01: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2020_07_01.operations.DeploymentsOperations>`
           * 2020-11-01-preview: :class:`DeploymentsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.DeploymentsOperations>`
        """
        api_version = self._get_api_version('deployments')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import DeploymentsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def monitoring_settings(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2020_07_01.operations.MonitoringSettingsOperations>`
           * 2020-11-01-preview: :class:`MonitoringSettingsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.MonitoringSettingsOperations>`
        """
        api_version = self._get_api_version('monitoring_settings')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import MonitoringSettingsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import MonitoringSettingsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`Operations<azure.mgmt.appplatform.v2019_05_01_preview.operations.Operations>`
           * 2020-07-01: :class:`Operations<azure.mgmt.appplatform.v2020_07_01.operations.Operations>`
           * 2020-11-01-preview: :class:`Operations<azure.mgmt.appplatform.v2020_11_01_preview.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import Operations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import Operations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import Operations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def runtime_versions(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.RuntimeVersionsOperations>`
           * 2020-07-01: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2020_07_01.operations.RuntimeVersionsOperations>`
           * 2020-11-01-preview: :class:`RuntimeVersionsOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.RuntimeVersionsOperations>`
        """
        api_version = self._get_api_version('runtime_versions')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import RuntimeVersionsOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import RuntimeVersionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def services(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.ServicesOperations>`
           * 2020-07-01: :class:`ServicesOperations<azure.mgmt.appplatform.v2020_07_01.operations.ServicesOperations>`
           * 2020-11-01-preview: :class:`ServicesOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.ServicesOperations>`
        """
        api_version = self._get_api_version('services')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import ServicesOperations as OperationClass
        elif api_version == '2020-07-01':
            from .v2020_07_01.operations import ServicesOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import ServicesOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def sku(self):
        """Instance depends on the API version:

           * 2019-05-01-preview: :class:`SkuOperations<azure.mgmt.appplatform.v2019_05_01_preview.operations.SkuOperations>`
        """
        api_version = self._get_api_version('sku')
        if api_version == '2019-05-01-preview':
            from .v2019_05_01_preview.operations import SkuOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def skus(self):
        """Instance depends on the API version:

           * 2020-07-01: :class:`SkusOperations<azure.mgmt.appplatform.v2020_07_01.operations.SkusOperations>`
           * 2020-11-01-preview: :class:`SkusOperations<azure.mgmt.appplatform.v2020_11_01_preview.operations.SkusOperations>`
        """
        api_version = self._get_api_version('skus')
        if api_version == '2020-07-01':
            from .v2020_07_01.operations import SkusOperations as OperationClass
        elif api_version == '2020-11-01-preview':
            from .v2020_11_01_preview.operations import SkusOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))