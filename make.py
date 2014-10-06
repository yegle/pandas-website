#!/usr/bin/env python

"""
Python script for building documentation.

To build the docs you must have all optional dependencies for pandas-website
installed. See the installation instructions for a list of these.

Usage
-----
python make.py clean
python make.py html
"""
from __future__ import print_function

import glob
import os
import shutil
import sys
import sphinx
import argparse
import jinja2

os.environ['PYTHONPATH'] = '..'

SPHINX_BUILD = 'sphinxbuild'

def clean():
    if os.path.exists('_build'):
        shutil.rmtree('_build')

def html():
    if os.system('sphinx-build -b html -d _build/doctrees . _build/html'):
        raise SystemExit("Building HTML failed.")

def all():
    clean()
    html()

if __name__ == '__main__':
    import sys

    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            func = globals().get(arg)
            if func is None:
                raise SystemExit('Do not know how to handle %s' % arg)
            func()
    else:
        all()
    sys.exit()
