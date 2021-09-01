# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_upgrade_extension
from .example_steps import step_extension_create
from .example_steps import step_extension_list
from .example_steps import step_extension_show
from .example_steps import step_extension_update
from .example_steps import step_extension_delete
from .example_steps import step_delete
from .example_steps import step_private_endpoint_connection_update
from .example_steps import step_private_endpoint_connection_list
from .example_steps import step_private_endpoint_connection_show
from .example_steps import step_private_endpoint_connection_delete
from .example_steps import step_private_link_resource_list
from .example_steps import step_private_link_scope_create
from .example_steps import step_private_link_scope_update
from .example_steps import step_private_link_scope_show
from .example_steps import step_private_link_scope_list
from .example_steps import step_private_link_scope_update_tag
from .example_steps import step_private_link_scope_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))

MACHINE_NAME = 'sdkTestVM'
RESOURCE_GROUP = 'az-sdk-test'
LOCATION = 'eastus2euap'
EXTENSION_NAME = 'CustomScriptExtension'
SCOPE_NAME = ''
PRIVATE_ENDPOINT_NAME = ''

# Env setup_scenario
@try_manual
def setup_scenario(test):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test):
    setup_scenario(test)
    step_show(test, checks=[
        test.check('name', MACHINE_NAME),
        test.check('resourceGroup', RESOURCE_GROUP)
    ])
    step_list(test, checks=[
        test.check('length(@)', 3)
    ])
    step_extension_create(test, checks=[
        test.check('name', EXTENSION_NAME),
        test.check('properties.typeHandlerVersion', '1.10.10')
    ])
    step_extension_list(test, checks=[
        test.check('length(@)', 1)
    ])
    step_extension_show(test, checks=[
        test.check('name', EXTENSION_NAME),
        test.check('properties.typeHandlerVersion', '1.10.10')
    ])
    step_upgrade_extension(test, checks=[])
    step_extension_update(test, checks=[
        test.check('name', EXTENSION_NAME),
        test.check('properties.provisioningState', 'Succeeded'),
        test.check('properties.settings.commandToExecute', 'hostname'),
        test.check('properties.typeHandlerVersion', '1.10.12')
    ])
    step_extension_delete(test, checks=[])
    step_delete(test, checks=[])
    # Below functions are manually tested
    # --------------------------------------------------------------
    # step_private_link_scope_create(test, checks=[
    #     test.check('name', SCOPE_NAME),
    #     test.check('location', LOCATION),
    #     test.check('length(tags)', 0)
    # ])
    # step_private_link_scope_update(test, checks=[

    # ])
    # step_private_link_scope_show(test, checks=[])
    # step_private_link_scope_list(test, checks=[])
    # step_private_link_scope_update_tag(test, checks=[])
    # step_private_link_scope_delete(test, checks=[])

    # step_private_endpoint_connection_list(test, checks=[
    #     test.check('length(@)', 1),
    # ])
    # step_private_endpoint_connection_show(test, checks=[
    #     test.check("name", "{myPrivateEndpointConnection}", case_sensitive=False),
    # ])
    # step_private_endpoint_connection_delete(test, checks=[])
    # step_private_link_resource_list(test, checks=[])
    cleanup_scenario(test)


# Test class for Scenario
@try_manual
class ConnectedmachineScenarioTest(ScenarioTest):
    def __init__(self, *args, **kwargs):
        super(ConnectedmachineScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'myMachine': 'myMachine',
            'myMachine2': 'machineName',
            'myPrivateEndpointConnection': 'private-endpoint-connection-name',
        })

    @ResourceGroupPreparer(name_prefix='clitestconnectedmachine_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestconnectedmachine_my-resource-group'[:7], key='rg_2',
                           parameter_name='rg_2')
    def test_connectedmachine_Scenario(self, rg, rg_2):
        call_scenario(self)
        calc_coverage(__file__)
        raise_if()