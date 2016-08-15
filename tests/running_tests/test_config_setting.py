# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
import subprocess

class FileSettingTest(unittest.TestCase):
    def setUp(self):
        subprocess.getoutput('hookman --stop --pidfile ~/my.pid')

    def tearDown(self):
        subprocess.getoutput('hookman --stop --pidfile ~/my.pid')

    def run_cmd(self, cmd, expect_text):
        true_text = subprocess.getoutput(cmd)
        self.assertEqual(true_text, expect_text)

    def test_run_as_set_pid_file(self):
        from os.path import expanduser
        pid_real_file = expanduser('~/my.pid')
        self.run_cmd('hookman --run -d --pidfile ~/my.pid',
                     'hookman running background\npidfile={}'.format(pid_real_file))
