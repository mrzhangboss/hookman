# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function


def run_work(projectdir):
    from os.path import join
    import time
    f = open(join(projectdir, 'date'), 'w')
    f.write(str(time.time()))
    pass