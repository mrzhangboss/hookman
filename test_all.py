# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
import subprocess


class RuningTest(unittest.TestCase):
    def test_run(self):
        # begin test
        # jack install the *hookman* by pip
        # he run his cmd
        help_text = subprocess.getoutput('hookman')

        # help list
        self.assertIn('-h', help_text)
        self.assertIn('--version', help_text)
        self.assertIn('--stop', help_text)
        self.assertIn('--run', help_text)
        self.assertIn('--restart', help_text)

        # he try -v
        version_info = subprocess.getoutput('hookman --version')

        self.assertEqual('0.1.0', version_info)

        # he let it run

        start_run = subprocess.getoutput('hookman --run')
        self.assertEqual('listen :3610, hookman run!!!', start_run)

from hookman.weblistener import app
class AppHookmanTest(unittest.TestCase):
    def test_hookman_can_listen(self):
        res = app.test_client().get('/')
        self.assertEqual(res.status_code, 200)







if __name__ == '__main__':
    unittest.main()