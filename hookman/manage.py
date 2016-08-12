# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

def main():
    import sys
    import argparse
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    parse = argparse.ArgumentParser()
    # todo: complete help text
    parse.add_argument('--version', action='version', version='0.1.0')
    parse.add_argument('--stop')
    parse.add_argument('--run', action='store_true')
    parse.add_argument('--restart')
    args = parse.parse_args()
    # todo: analyze args and start work
    print('listen :3610, hookman run!!!')