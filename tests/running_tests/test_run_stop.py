# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import unittest
import subprocess


# @unittest.skip
class RuningTest(unittest.TestCase):
    def setUp(self):
        subprocess.getoutput('hookman --stop')

    def tearDown(self):
        subprocess.getoutput('hookman --stop')

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
        self.assertIn('--pidfile', help_text)

        # he try -v
        version_info = subprocess.getoutput('hookman --version')

        self.assertEqual('0.1.0', version_info)

        # he let it run

        start_run = subprocess.getoutput('hookman --run -d')
        self.assertEqual('hookman running background', start_run)
        import time
        time.sleep(1)

        ## he do a little test
        # he try ping
        result = subprocess.getoutput('curl -X POST --header "X-GitHub-Event: ping" http://localhost:3610/')

        self.assertIn('pong', result)

        # he try push
        result = subprocess.getoutput('curl -X POST --header "X-GitHub-Event: push" http://localhost:3610/')
        self.assertIn('hookman-0.1.0 get', result)

# @unittest.skip
class RunStopRestartTest(RuningTest):
    def run_cmd(self, cmd, expect_text):
        true_text = subprocess.getoutput(cmd)
        self.assertEqual(true_text, expect_text)


    def test_run_then_stop(self):
        self.run_cmd('hookman --run -d','hookman running background')
        self.run_cmd('hookman --stop', 'stop hookman!!!')

    def test_stop_twice(self):
        stop_run = subprocess.getoutput('hookman --stop')
        stop_run = subprocess.getoutput('hookman --stop')
        self.assertEqual('hookman not running!!!', stop_run)

    def test_run_twice(self):
        start_run = subprocess.getoutput('hookman --run -d')

        self.assertEqual('hookman running background', start_run)

        twith_run = subprocess.getoutput('hookman --run -d')

        self.assertEqual('hookman already run', twith_run)



# @unittest.skip
class DaemonTest(RuningTest):
    def check_timeout(self, cmd):
        daemon_open = subprocess.check_output(cmd, timeout=1)
        return daemon_open

    def test_daemon_open(self):
        self.assertEqual(self.check_timeout(['hookman', '--run', '-d']), b'hookman running background\n')

    def test_daemon_close(self):
        self.assertRaises(subprocess.TimeoutExpired, self.check_timeout, ['hookman', '--run'])




if __name__ == '__main__':
    unittest.main()
