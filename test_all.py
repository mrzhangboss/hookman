# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
import subprocess

# todo: test is complex
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

from hookman.weblistener import app
from flask import Request
class AppHookmanTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass


    def test_hookman_allow_get(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 405)

    def test_hookman_allow_post(self):
        res = self.client.post('/')
        self.assertEqual(res.status_code, 200)

    def test_hookman_can_ping_back(self):
        header = {'X-GitHub-Event': 'ping'}
        res = self.client.post('/', headers=header)
        self.assertEqual(res.data, b'pong')

    def test_hookman_can_get_push_command(self):
        header = {'X-GitHub-Event': 'push'}
        res = self.client.post('/', headers=header)
        self.assertEqual(res.data, b'hookman-0.1.0 get')








if __name__ == '__main__':
    unittest.main()
