# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddPolicySigningCertificatesKeys(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddPolicySigningCertificatesKeys, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'alg':
                d['alg'] = v[0]
            elif kl == 'crv':
                d['crv'] = v[0]
            elif kl == 'd':
                d['d'] = v[0]
            elif kl == 'dp':
                d['dp'] = v[0]
            elif kl == 'dq':
                d['dq'] = v[0]
            elif kl == 'e':
                d['e'] = v[0]
            elif kl == 'k':
                d['k'] = v[0]
            elif kl == 'kid':
                d['kid'] = v[0]
            elif kl == 'kty':
                d['kty'] = v[0]
            elif kl == 'n':
                d['n'] = v[0]
            elif kl == 'p':
                d['p'] = v[0]
            elif kl == 'q':
                d['q'] = v[0]
            elif kl == 'qi':
                d['qi'] = v[0]
            elif kl == 'use':
                d['use'] = v[0]
            elif kl == 'x':
                d['x'] = v[0]
            elif kl == 'x5-c':
                d['x5_c'] = v
            elif kl == 'y':
                d['y'] = v[0]
        return d