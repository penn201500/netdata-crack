#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

# Unittest class
# =============
#print('Unit tests for NetData %s' % __version__)

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


if __name__ == '__main__':
    unittest.main()
