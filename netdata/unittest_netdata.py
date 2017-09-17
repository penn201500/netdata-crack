#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys
from netdata.netdata import parse_proc_net_dev
from netdata import __version__

# Unittest class
# =============
print('Unit tests for NetData %s' % __version__)

class TestNetData(unittest.TestCase):
    """Test NetData class"""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skipIf(sys.platform.startswith("win"), "Only tested in Linux")
    def test_window_skip(self):
        """windows os skip"""
        print('Skip windows platform')

    def test_001_parse_proc_net_dev(self):
        "Check function parse_proc_netdata"
        print('INFO: [TEST_001] check parse_proc_net_dev function')
        net_dev_info = parse_proc_net_dev()
        self.assertTrue(type(net_dev_info) is tuple, msg = 'parse_proc_net_dev can not get a right result')
        print('INFO: network device input and output is %s' % (net_dev_info,))
        self.assertEqual(len(net_dev_info), 2)
        print('INFO: return result length is 2')


if __name__ == '__main__':
    unittest.main()
