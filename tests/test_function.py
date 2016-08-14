# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
import subprocess

class RuningTest(unittest.TestCase):
    def test_run(self):
        self.maxDiff = None
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

        ## he do a little test
        # he try ping
        result = subprocess.getoutput('curl -X POST --header "X-GitHub-Event: ping" http://localhost:3610/')

        self.assertIn('pong', result)

        # he try push
        result = subprocess.getoutput('curl -X POST --header "X-GitHub-Event: push" http://localhost:3610/')
        self.assertIn('hookman-0.1.0 get', result)

class RunStopTest(unittest.TestCase):
    def setUp(self):
        # stop it first
        subprocess.getoutput('hookman --stop')



    def test_run_then_stop(self):
        start_run = subprocess.getoutput('hookman --run')

        self.assertEqual('listen :3610, hookman run!!!', start_run)

        stop_run = subprocess.getoutput('hookman --stop')
        self.assertEqual('stop hookman!!!', stop_run)

    def test_stop_twice(self):
        stop_run = subprocess.getoutput('hookman --stop')
        stop_run = subprocess.getoutput('hookman --stop')
        self.assertEqual('hookman not running!!!', stop_run)

if __name__ == '__main__':
    unittest.main()
