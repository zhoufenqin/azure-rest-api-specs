# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)

from .utils import get_test_resource_group, get_test_workspace, get_test_workspace_location

TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


class QuantumTargetsScenarioTest(ScenarioTest):

    def test_targets(self):
        # set current workspace:
        self.cmd(f'az quantum workspace set -g {get_test_resource_group()} -w {get_test_workspace()} -l {get_test_workspace_location()}')

        # clear current target
        self.cmd(f'az quantum target clear')

        # list
        targets = self.cmd('az quantum target list -o json').get_output_in_json()
        assert len(targets) > 0

        # set
        self.cmd(f'az quantum target set -t microsoft.paralleltempering.cpu -o json', checks=[
            self.check("targetId", "microsoft.paralleltempering.cpu")
        ])

        # show
        self.cmd(f'az quantum target show -o json', checks=[
            self.check("targetId", "microsoft.paralleltempering.cpu")
        ])
        self.cmd(f'az quantum target show -t microsoft.simulatedannealing.cpu -o json', checks=[
            self.check("targetId", "microsoft.simulatedannealing.cpu")
        ])

        # clear
        self.cmd(f'az quantum target clear')