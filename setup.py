# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
from setuptools import setup, find_packages

# todo: add install_requires and test_requires
setup(name='hookman',
      version='0.1.0',
      packages=find_packages(),
      test_requires = ['py.test>=2.92'],
      install_requires = ['flask>=0.6.0'],
      entry_points={
    'console_scripts': ['hookman = hookman.manage:main']
})