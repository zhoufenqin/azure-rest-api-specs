# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from collections import OrderedDict
from azure.cli.core.commands import CliCommandType
from azext_connectedmachine.generated._client_factory import (
    cf_machine,
    cf_machine_extension,
    cf_connectedmachine_cl,
    cf_private_link_scope,
    cf_private_link_resource,
    cf_private_endpoint_connection,
)


connectedmachine_machine = CliCommandType(
    operations_tmpl=(
        'azext_connectedmachine.vendored_sdks.connectedmachine.operations._machines_operations#MachinesOperations.{}'
    ),
    client_factory=cf_machine,
)


connectedmachine_ = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._connected_machine_operations#ConnectedMachineOperationsMixin.{}',
    client_factory=cf_connectedmachine_cl,
)


connectedmachine_machine_extension = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._machine_extensions_operations#MachineExtensionsOperations.{}',
    client_factory=cf_machine_extension,
)


connectedmachine_private_endpoint_connection = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._private_endpoint_connections_operations#PrivateEndpointConnectionsOperations.{}',
    client_factory=cf_private_endpoint_connection,
)


connectedmachine_private_link_resource = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._private_link_resources_operations#PrivateLinkResourcesOperations.{}',
    client_factory=cf_private_link_resource,
)


connectedmachine_private_link_scope = CliCommandType(
    operations_tmpl='azext_connectedmachine.vendored_sdks.connectedmachine.operations._private_link_scopes_operations#PrivateLinkScopesOperations.{}',
    client_factory=cf_private_link_scope,
)


def load_command_table(self, _):

    with self.command_group('connectedmachine', connectedmachine_machine, client_factory=cf_machine) as g:
        g.custom_command('list', 'connectedmachine_list', table_transformer=transform_machine_list)


def transform_machine_list(result):
    return [transform_machine(machine) for machine in result]


def transform_machine(result):
    return OrderedDict([('Name', result['name']),
                        ('ResourceGroup', result['resourceGroup']),
                        ('Location', result['location']),
                        ('Status', result.get('status'))])