# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ServiceOperations:
    """ServiceOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.storage.filedatalake.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_file_systems(
        self,
        prefix: Optional[str] = None,
        continuation: Optional[str] = None,
        max_results: Optional[int] = None,
        request_id_parameter: Optional[str] = None,
        timeout: Optional[int] = None,
        **kwargs
    ) -> AsyncIterable["_models.FileSystemList"]:
        """List FileSystems.

        List filesystems and their properties in given account.

        :param prefix: Filters results to filesystems within the specified prefix.
        :type prefix: str
        :param continuation: Optional.  When deleting a directory, the number of paths that are deleted
         with each invocation is limited.  If the number of paths to be deleted exceeds this limit, a
         continuation token is returned in this response header.  When a continuation token is returned
         in the response, it must be specified in a subsequent invocation of the delete operation to
         continue deleting the directory.
        :type continuation: str
        :param max_results: An optional value that specifies the maximum number of items to return. If
         omitted or greater than 5,000, the response will include up to 5,000 items.
        :type max_results: int
        :param request_id_parameter: Provides a client-generated, opaque value with a 1 KB character
         limit that is recorded in the analytics logs when storage analytics logging is enabled.
        :type request_id_parameter: str
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a href="https://docs.microsoft.com/en-us/rest/api/storageservices/fileservices/setting-
         timeouts-for-blob-service-operations">Setting Timeouts for Blob Service Operations.</a>`.
        :type timeout: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FileSystemList or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.storage.filedatalake.models.FileSystemList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FileSystemList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        resource = "account"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            if request_id_parameter is not None:
                header_parameters['x-ms-client-request-id'] = self._serialize.header("request_id_parameter", request_id_parameter, 'str')
            header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_file_systems.metadata['url']  # type: ignore
                path_format_arguments = {
                    'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['resource'] = self._serialize.query("resource", resource, 'str')
                if prefix is not None:
                    query_parameters['prefix'] = self._serialize.query("prefix", prefix, 'str')
                if continuation is not None:
                    query_parameters['continuation'] = self._serialize.query("continuation", continuation, 'str')
                if max_results is not None:
                    query_parameters['maxResults'] = self._serialize.query("max_results", max_results, 'int', minimum=1)
                if timeout is not None:
                    query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('FileSystemList', pipeline_response)
            list_of_elem = deserialized.filesystems
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.StorageError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_file_systems.metadata = {'url': '/'}  # type: ignore