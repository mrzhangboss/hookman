# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import os
import subprocess
import multiprocessing
from hookman.weblistener import  app
PID_FILE = '/home/zhanglun/hookman.pid'
ERROR_LOG = '/home/zhanglun/hookman.log'

def main():
    import sys
    import argparse
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parse = argparse.ArgumentParser()
    # todo: complete help text
    parse.add_argument('--version', action='version', version='0.1.0')
    parse.add_argument('--stop', action='store_true')
    parse.add_argument('--run', action='store_true')
    parse.add_argument('--restart')
    args = parse.parse_args()
    # todo: analyze args and start work
    if args.run == True:
        error_file = open(ERROR_LOG, mode='a+')
        pid_file = open(PID_FILE, mode='w')
        args = {'args': ['python', '/home/zhanglun/hookman/hookman/weblistener.py', '&']}
        popen = subprocess.Popen(['python /home/zhanglun/hookman/hookman/weblistener.py'],
                                 shell=True,
                                 stderr=error_file,
                                 stdout=error_file,
                                 preexec_fn=os.setsid)
        pid_file.write(str(popen.pid))
        pid_file.close()
        print('listen :3610, hookman run!!!')
    elif args.stop == True:
        if os.path.exists(PID_FILE):
            print('stop hookman!!!')
            os.remove(PID_FILE)
        else:
            print('hookman not running!!!')




