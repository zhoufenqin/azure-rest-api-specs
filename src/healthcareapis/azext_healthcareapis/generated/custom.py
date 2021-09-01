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

from azure.cli.core.util import sdk_no_wait


def healthcareapis_service_list(client,
                                resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def healthcareapis_service_show(client,
                                resource_group_name,
                                resource_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name)


def healthcareapis_service_create(client,
                                  resource_group_name,
                                  resource_name,
                                  kind,
                                  location,
                                  tags=None,
                                  etag=None,
                                  identity_type=None,
                                  access_policies=None,
                                  cosmos_db_configuration=None,
                                  authentication_configuration=None,
                                  cors_configuration=None,
                                  private_endpoint_connections=None,
                                  public_network_access=None,
                                  export_configuration_storage_account_name=None,
                                  no_wait=False):

    properties = {
        'access_policies': access_policies,
        'cosmos_db_configuration': cosmos_db_configuration,
        'authentication_configuration': authentication_configuration,
        'cors_configuration': cors_configuration,
        'private_endpoint_connections': private_endpoint_connections,
        'public_network_access': public_network_access,
        'export_configuration_storage_account_name': export_configuration_storage_account_name
    }

    service_description = {
        'name': resource_name,
        'kind': kind,
        'location': location,
        'tags': tags,
        'etag': etag,
        'identity_type': identity_type,
        'properties': properties
    }

    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_description=service_description)


def healthcareapis_service_update(client,
                                  resource_group_name,
                                  resource_name,
                                  tags=None,
                                  public_network_access=None,
                                  no_wait=False):

    return sdk_no_wait(no_wait,
                       client.update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       tags=tags,
                       public_network_access=public_network_access)


def healthcareapis_service_delete(client,
                                  resource_group_name,
                                  resource_name,
                                  no_wait=False):
    return sdk_no_wait(no_wait,
                       client.delete,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name)


def healthcareapis_operation_result_show(client,
                                         location_name,
                                         operation_result_id):
    return client.get(location_name=location_name,
                      operation_result_id=operation_result_id)


def healthcareapis_private_endpoint_connection_list(client,
                                                    resource_group_name,
                                                    resource_name):
    return client.list_by_service(resource_group_name=resource_group_name,
                                  resource_name=resource_name)


def healthcareapis_private_endpoint_connection_show(client,
                                                    resource_group_name,
                                                    resource_name,
                                                    private_endpoint_connection_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name,
                      private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_private_endpoint_connection_create(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      private_link_service_connection_state_status=None,
                                                      private_link_service_connection_state_description=None,
                                                      private_link_service_connection_state_actions_required=None,
                                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       status=private_link_service_connection_state_status,
                       description=private_link_service_connection_state_description,
                       actions_required=private_link_service_connection_state_actions_required)


def healthcareapis_private_endpoint_connection_update(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      private_link_service_connection_state_status=None,
                                                      private_link_service_connection_state_description=None,
                                                      private_link_service_connection_state_actions_required=None,
                                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name,
                       status=private_link_service_connection_state_status,
                       description=private_link_service_connection_state_description,
                       actions_required=private_link_service_connection_state_actions_required)


def healthcareapis_private_endpoint_connection_delete(client,
                                                      resource_group_name,
                                                      resource_name,
                                                      private_endpoint_connection_name,
                                                      no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       private_endpoint_connection_name=private_endpoint_connection_name)


def healthcareapis_private_link_resource_list(client,
                                              resource_group_name,
                                              resource_name):
    return client.list_by_service(resource_group_name=resource_group_name,
                                  resource_name=resource_name)


def healthcareapis_private_link_resource_show(client,
                                              resource_group_name,
                                              resource_name,
                                              group_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name,
                      group_name=group_name)


def healthcareapis_acr_list(client,
                            resource_group_name,
                            resource_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name).properties.acr_configuration


def healthcareapis_acr_add(client,
                           resource_group_name,
                           resource_name,
                           login_servers=None,
                           no_wait=False):
    service_description = client.get(resource_group_name=resource_group_name,
                                     resource_name=resource_name)
    if not login_servers:
        return service_description

    new_login_servers = service_description.properties.acr_configuration.login_servers
    for login_server in login_servers.split():
        if login_server not in new_login_servers:
            new_login_servers.append(login_server)

    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_description=service_description)


def healthcareapis_acr_remove(client,
                              resource_group_name,
                              resource_name,
                              login_servers=None,
                              no_wait=False):
    service_description = client.get(resource_group_name=resource_group_name,
                                     resource_name=resource_name)
    if not login_servers:
        return service_description

    new_login_servers = service_description.properties.acr_configuration.login_servers
    for login_server in login_servers.split():
        if login_server in new_login_servers:
            new_login_servers.remove(login_server)

    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_description=service_description)


def healthcareapis_acr_reset(client,
                             resource_group_name,
                             resource_name,
                             login_servers=None,
                             no_wait=False):
    service_description = client.get(resource_group_name=resource_group_name,
                                     resource_name=resource_name)
    login_servers = login_servers.split() if login_servers else []
    service_description.properties.acr_configuration.login_servers = login_servers

    return sdk_no_wait(no_wait,
                       client.create_or_update,
                       resource_group_name=resource_group_name,
                       resource_name=resource_name,
                       service_description=service_description)