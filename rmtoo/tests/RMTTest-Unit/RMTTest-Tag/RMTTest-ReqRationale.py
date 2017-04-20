'''
 rmtoo
   Free and Open Source Requirements Management Tool

  Unit test for ReqRationale

 (c) 2010-2012,2017 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
from __future__ import unicode_literals

import unittest

from rmtoo.inputs.ReqRationale import ReqRationale
from rmtoo.tests.lib.ReqTag import create_parameters
from rmtoo.lib.storagebackend.RecordEntry import RecordEntry


class RMTTestReqRationale(unittest.TestCase):

    def rmttest_positive_01(self):
        "Requirement Tag Rationale - no tag given"
        config, req = create_parameters()

        rt = ReqRationale(config)
        name, value = rt.rewrite("Rationale-test", req)
        self.assertEqual("Rationale", name)
        self.assertIsNone(value)

    def rmttest_positive_02(self):
        "Requirement Tag Rationale - Rationale set"
        config, req = create_parameters()
        req = {"Rationale": RecordEntry("Rationale", "something")}

        rt = ReqRationale(config)
        name, value = rt.rewrite("Rationale-test", req)
        self.assertEqual("Rationale", name)
        self.assertEqual("something", value.get_content())
