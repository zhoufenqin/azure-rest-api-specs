# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines


def maintenance_public_configuration_list(client):
    return client.list()


def maintenance_public_configuration_show(client,
                                          resource_name):
    return client.get(resource_name=resource_name)


def maintenance_applyupdate_list(client):
    return client.list()


def maintenance_applyupdate_show(client,
                                 resource_group_name,
                                 provider_name,
                                 resource_type,
                                 resource_name,
                                 apply_update_name):
    return client.get(resource_group_name=resource_group_name,
                      provider_name=provider_name,
                      resource_type=resource_type,
                      resource_name=resource_name,
                      apply_update_name=apply_update_name)


def maintenance_applyupdate_create(client,
                                   resource_group_name,
                                   provider_name,
                                   resource_type,
                                   resource_name,
                                   resource_parent_type=None,
                                   resource_parent_name=None):
    if resource_group_name and provider_name is not None and resource_parent_type is not None and resource_parent_name is not None and resource_type is not None and resource_name is not None:
        return client.create_or_update_parent(resource_group_name=resource_group_name,
                                              provider_name=provider_name,
                                              resource_parent_type=resource_parent_type,
                                              resource_parent_name=resource_parent_name,
                                              resource_type=resource_type,
                                              resource_name=resource_name)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name)


def maintenance_applyupdate_update(client,
                                   resource_group_name,
                                   provider_name,
                                   resource_type,
                                   resource_name):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name)


def maintenance_applyupdate_show_parent(client,
                                        resource_group_name,
                                        resource_parent_type,
                                        resource_parent_name,
                                        provider_name,
                                        resource_type,
                                        resource_name,
                                        apply_update_name):
    return client.get_parent(resource_group_name=resource_group_name,
                             resource_parent_type=resource_parent_type,
                             resource_parent_name=resource_parent_name,
                             provider_name=provider_name,
                             resource_type=resource_type,
                             resource_name=resource_name,
                             apply_update_name=apply_update_name)


def maintenance_assignment_list(client,
                                resource_group_name,
                                provider_name,
                                resource_type,
                                resource_name):
    return client.list(resource_group_name=resource_group_name,
                       provider_name=provider_name,
                       resource_type=resource_type,
                       resource_name=resource_name)


def maintenance_assignment_create(client,
                                  resource_group_name,
                                  provider_name,
                                  resource_type,
                                  resource_name,
                                  configuration_assignment_name,
                                  resource_parent_type=None,
                                  resource_parent_name=None,
                                  location=None,
                                  maintenance_configuration_id=None,
                                  resource_id=None):
    configuration_assignment = {}
    configuration_assignment['location'] = location
    configuration_assignment['maintenance_configuration_id'] = maintenance_configuration_id
    configuration_assignment['resource_id'] = resource_id
    configuration_assignment = {}
    configuration_assignment['location'] = location
    configuration_assignment['maintenance_configuration_id'] = maintenance_configuration_id
    configuration_assignment['resource_id'] = resource_id
    if resource_group_name and provider_name is not None and resource_parent_type is not None and resource_parent_name is not None and resource_type is not None and resource_name is not None and configuration_assignment_name is not None:
        return client.create_or_update_parent(resource_group_name=resource_group_name,
                                              provider_name=provider_name,
                                              resource_parent_type=resource_parent_type,
                                              resource_parent_name=resource_parent_name,
                                              resource_type=resource_type,
                                              resource_name=resource_name,
                                              configuration_assignment_name=configuration_assignment_name,
                                              configuration_assignment=configuration_assignment)
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name,
                                   configuration_assignment_name=configuration_assignment_name,
                                   configuration_assignment=configuration_assignment)


def maintenance_assignment_update(client,
                                  resource_group_name,
                                  provider_name,
                                  resource_type,
                                  resource_name,
                                  configuration_assignment_name,
                                  location=None,
                                  maintenance_configuration_id=None,
                                  resource_id=None):
    configuration_assignment = {}
    configuration_assignment['location'] = location
    configuration_assignment['maintenance_configuration_id'] = maintenance_configuration_id
    configuration_assignment['resource_id'] = resource_id
    return client.create_or_update(resource_group_name=resource_group_name,
                                   provider_name=provider_name,
                                   resource_type=resource_type,
                                   resource_name=resource_name,
                                   configuration_assignment_name=configuration_assignment_name,
                                   configuration_assignment=configuration_assignment)


def maintenance_assignment_delete(client,
                                  resource_group_name,
                                  provider_name,
                                  resource_type,
                                  resource_name,
                                  configuration_assignment_name,
                                  resource_parent_type=None,
                                  resource_parent_name=None):
    if resource_group_name and provider_name is not None and resource_parent_type is not None and resource_parent_name is not None and resource_type is not None and resource_name is not None and configuration_assignment_name is not None:
        return client.delete_parent(resource_group_name=resource_group_name,
                                    provider_name=provider_name,
                                    resource_parent_type=resource_parent_type,
                                    resource_parent_name=resource_parent_name,
                                    resource_type=resource_type,
                                    resource_name=resource_name,
                                    configuration_assignment_name=configuration_assignment_name)
    return client.delete(resource_group_name=resource_group_name,
                         provider_name=provider_name,
                         resource_type=resource_type,
                         resource_name=resource_name,
                         configuration_assignment_name=configuration_assignment_name)


def maintenance_assignment_list_parent(client,
                                       resource_group_name,
                                       provider_name,
                                       resource_parent_type,
                                       resource_parent_name,
                                       resource_type,
                                       resource_name):
    return client.list_parent(resource_group_name=resource_group_name,
                              provider_name=provider_name,
                              resource_parent_type=resource_parent_type,
                              resource_parent_name=resource_parent_name,
                              resource_type=resource_type,
                              resource_name=resource_name)


def maintenance_configuration_list(client):
    return client.list()


def maintenance_configuration_show(client,
                                   resource_group_name,
                                   resource_name):
    return client.get(resource_group_name=resource_group_name,
                      resource_name=resource_name)


def maintenance_configuration_create(client,
                                     resource_group_name,
                                     resource_name,
                                     location=None,
                                     tags=None,
                                     namespace=None,
                                     extension_properties=None,
                                     maintenance_scope=None,
                                     visibility=None,
                                     start_date_time=None,
                                     expiration_date_time=None,
                                     duration=None,
                                     time_zone=None,
                                     recur_every=None):
    configuration = {}
    configuration['location'] = location
    configuration['tags'] = tags
    configuration['namespace'] = namespace
    configuration['extension_properties'] = extension_properties
    configuration['maintenance_scope'] = maintenance_scope
    configuration['visibility'] = visibility
    configuration['start_date_time'] = start_date_time
    configuration['expiration_date_time'] = expiration_date_time
    configuration['duration'] = duration
    configuration['time_zone'] = time_zone
    configuration['recur_every'] = recur_every
    return client.create_or_update(resource_group_name=resource_group_name,
                                   resource_name=resource_name,
                                   configuration=configuration)


def maintenance_configuration_update(client,
                                     resource_group_name,
                                     resource_name,
                                     location=None,
                                     tags=None,
                                     namespace=None,
                                     extension_properties=None,
                                     maintenance_scope=None,
                                     visibility=None,
                                     start_date_time=None,
                                     expiration_date_time=None,
                                     duration=None,
                                     time_zone=None,
                                     recur_every=None):
    configuration = {}
    configuration['location'] = location
    configuration['tags'] = tags
    configuration['namespace'] = namespace
    configuration['extension_properties'] = extension_properties
    configuration['maintenance_scope'] = maintenance_scope
    configuration['visibility'] = visibility
    configuration['start_date_time'] = start_date_time
    configuration['expiration_date_time'] = expiration_date_time
    configuration['duration'] = duration
    configuration['time_zone'] = time_zone
    configuration['recur_every'] = recur_every
    return client.update(resource_group_name=resource_group_name,
                         resource_name=resource_name,
                         configuration=configuration)


def maintenance_configuration_delete(client,
                                     resource_group_name,
                                     resource_name):
    return client.delete(resource_group_name=resource_group_name,
                         resource_name=resource_name)


def maintenance_configuration_for_resource_group_list(client,
                                                      resource_group_name):
    return client.list(resource_group_name=resource_group_name)


def maintenance_applyupdate_for_resource_group_list(client,
                                                    resource_group_name):
    return client.list(resource_group_name=resource_group_name)


def maintenance_update_list(client,
                            resource_group_name,
                            provider_name,
                            resource_type,
                            resource_name):
    return client.list(resource_group_name=resource_group_name,
                       provider_name=provider_name,
                       resource_type=resource_type,
                       resource_name=resource_name)


def maintenance_update_list_parent(client,
                                   resource_group_name,
                                   provider_name,
                                   resource_parent_type,
                                   resource_parent_name,
                                   resource_type,
                                   resource_name):
    return client.list_parent(resource_group_name=resource_group_name,
                              provider_name=provider_name,
                              resource_parent_type=resource_parent_type,
                              resource_parent_name=resource_parent_name,
                              resource_type=resource_type,
                              resource_name=resource_name)