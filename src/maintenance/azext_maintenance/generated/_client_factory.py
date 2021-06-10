# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_maintenance_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_maintenance.vendored_sdks.maintenance import MaintenanceClient
    return get_mgmt_service_client(cli_ctx,
                                   MaintenanceClient)


def cf_public_maintenance_configuration(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).public_maintenance_configurations


def cf_apply_update(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).apply_updates


def cf_configuration_assignment(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).configuration_assignments


def cf_maintenance_configuration(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).maintenance_configurations


def cf_maintenance_configuration_for_resource_group(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).maintenance_configurations_for_resource_group


def cf_apply_update_for_resource_group(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).apply_update_for_resource_group


def cf_update(cli_ctx, *_):
    return cf_maintenance_cl(cli_ctx).updates