# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_healthcareapis.action import (
    AddAccessPolicies,
    AddCosmosDbConfiguration,
    AddAuthenticationConfiguration,
    AddCorsConfiguration,
    AddPrivateEndpointConnections
)


def load_arguments(self, _):

    with self.argument_context('healthcareapis service list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('healthcareapis service show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')

    with self.argument_context('healthcareapis service create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.')
        c.argument('kind', arg_type=get_enum_type(['fhir', 'fhir-Stu3', 'fhir-R4']), help='The kind of the service.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx),
                   validator=get_default_location_from_resource_group)
        c.argument('tags', tags_type)
        c.argument('etag', type=str, help='An etag associated with the resource, used for optimistic concurrency when '
                   'editing it.')
        c.argument('identity_type', arg_type=get_enum_type(['SystemAssigned', 'None']), help='Type of identity being '
                   'specified, currently SystemAssigned and None are allowed.')
        c.argument('access_policies', action=AddAccessPolicies, nargs='*', help='The access policies of the service '
                   'instance.')
        c.argument('cosmos_db_configuration', action=AddCosmosDbConfiguration, nargs='*', help='The settings for the '
                   'Cosmos DB database backing the service.')
        c.argument('authentication_configuration', action=AddAuthenticationConfiguration, nargs='*', help='The '
                   'authentication configuration for the service instance.')
        c.argument('cors_configuration', action=AddCorsConfiguration, nargs='*', help='The settings for the CORS '
                   'configuration of the service instance.')
        c.argument('private_endpoint_connections', action=AddPrivateEndpointConnections, nargs='*', help='The list of '
                   'private endpoint connections that are set up for this resource.')
        c.argument('public_network_access', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Control permission '
                   'for data plane traffic coming from public networks while private endpoint is enabled.')
        c.argument('export_configuration_storage_account_name', type=str, help='The name of the default export storage '
                   'account.')

    with self.argument_context('healthcareapis service update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('tags', tags_type)
        c.argument('public_network_access', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Control permission '
                   'for data plane traffic coming from public networks while private endpoint is enabled.')

    with self.argument_context('healthcareapis service delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')

    with self.argument_context('healthcareapis service wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')

    with self.argument_context('healthcareapis operation-result show') as c:
        c.argument('location_name', type=str, help='The location of the operation.', id_part='name')
        c.argument('operation_result_id', type=str, help='The ID of the operation result to get.', id_part=''
                   'child_name_1')

    with self.argument_context('healthcareapis private-endpoint-connection list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.')

    with self.argument_context('healthcareapis private-endpoint-connection show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('private_endpoint_connection_name', options_list=['--name', '-n', '--private-endpoint-connection-nam'
                                                                     'e'], type=str, help='The name of the private '
                   'endpoint connection associated with the Azure resource', id_part='child_name_1')

    with self.argument_context('healthcareapis private-endpoint-connection create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.')
        c.argument('private_endpoint_connection_name', options_list=['--name', '-n', '--private-endpoint-connection-nam'
                                                                     'e'], type=str, help='The name of the private '
                   'endpoint connection associated with the Azure resource')
        c.argument('private_link_service_connection_state_status', arg_type=get_enum_type(['Pending', 'Approved', ''
                                                                                           'Rejected']), help=''
                   'Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.')
        c.argument('private_link_service_connection_state_description', type=str, help='The reason for '
                   'approval/rejection of the connection.')
        c.argument('private_link_service_connection_state_actions_required', type=str, help='A message indicating if '
                   'changes on the service provider require any updates on the consumer.')

    with self.argument_context('healthcareapis private-endpoint-connection update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('private_endpoint_connection_name', options_list=['--name', '-n', '--private-endpoint-connection-nam'
                                                                     'e'], type=str, help='The name of the private '
                   'endpoint connection associated with the Azure resource', id_part='child_name_1')
        c.argument('private_link_service_connection_state_status', arg_type=get_enum_type(['Pending', 'Approved', ''
                                                                                           'Rejected']), help=''
                   'Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.')
        c.argument('private_link_service_connection_state_description', type=str, help='The reason for '
                   'approval/rejection of the connection.')
        c.argument('private_link_service_connection_state_actions_required', type=str, help='A message indicating if '
                   'changes on the service provider require any updates on the consumer.')

    with self.argument_context('healthcareapis private-endpoint-connection delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('private_endpoint_connection_name', options_list=['--name', '-n', '--private-endpoint-connection-nam'
                                                                     'e'], type=str, help='The name of the private '
                   'endpoint connection associated with the Azure resource', id_part='child_name_1')

    with self.argument_context('healthcareapis private-endpoint-connection wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('private_endpoint_connection_name', options_list=['--name', '-n', '--private-endpoint-connection-nam'
                                                                     'e'], type=str, help='The name of the private '
                   'endpoint connection associated with the Azure resource', id_part='child_name_1')

    with self.argument_context('healthcareapis private-link-resource list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.')

    with self.argument_context('healthcareapis private-link-resource show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('group_name', type=str, help='The name of the private link resource group.',
                   id_part='child_name_1')

    with self.argument_context('healthcareapis acr list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.')

    with self.argument_context('healthcareapis acr add') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('login_servers', type=str, help='The list of login servers that shall'
                   'be added to the service instance.')

    with self.argument_context('healthcareapis acr remove') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('login_servers', type=str, help='The list of login servers that shall'
                   'be removed from the service instance.')

    with self.argument_context('healthcareapis acr reset') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('resource_name', type=str, help='The name of the service instance.', id_part='name')
        c.argument('login_servers', type=str, help='The list of login servers to substitute for the existing one.')