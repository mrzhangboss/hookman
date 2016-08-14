# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
import os
import sys
import subprocess
import multiprocessing
import logging
from hookman.weblistener import  app
PID_FILE = '/home/zhanglun/hookman.pid'
ERROR_LOG = '/home/zhanglun/hookman.log'

logging.basicConfig(filemode='w',
                    filename='/home/zhanglun/hookman/log.txt',
                    level=logging.DEBUG)
def is_alive(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

def main():
    logging.error('log ???')
    import sys
    import argparse
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parse = argparse.ArgumentParser()
    # todo: complete help text
    parse.add_argument('--version', action='version', version='0.1.0')
    parse.add_argument('-s', '--stop', action='store_true', help='stop running')
    parse.add_argument('-r', '--run', action='store_true', help='show help text')
    parse.add_argument('-d', '--daemon',action='store_true', help='running in background')
    args = parse.parse_args()

    if args.d == True:
        error_file = open(ERROR_LOG, mode='w')
    else:
        error_file = subprocess.PIPE

    # todo: lighter complex logic
    if args.run:
        if os.path.exists(PID_FILE):
            pid = open(PID_FILE).read()
            pid = int(pid)
            if is_alive(pid):
                print('hookman already run')
                return
            else:
                os.remove(PID_FILE)
        pid_file = open(PID_FILE, mode='w')
        popen = subprocess.Popen(['python', '/home/zhanglun/hookman/hookman/weblistener.py'],
                                 stderr=error_file,
                                 stdout=error_file,)

                                 # preexec_fn=os.setsid)
        logging.info('PID: {}'.format(popen.pid))
        pid_file.write(str(popen.pid))
        pid_file.close()
        if args.d:
            print('hookman running background')
        else:
            try:
                while True:
                    print(popen.stderr.readline())
            finally:
                popen.kill()


    elif args.stop == True:
        if os.path.exists(PID_FILE):
            pid = open(PID_FILE).read()
            pid = int(pid)
            if is_alive(pid):
                os.kill(pid, 9)
                print('stop hookman!!!')
            else:
                print('hookman not running!!!')
            logging.error('delete pid file')
            os.remove(PID_FILE)

        else:
            print('hookman not running!!!')




