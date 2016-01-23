#!/usr/bin/env python
"""Distutils based setup script for Green_roof

This uses Distutils (http://python.org/sigs/distutils-sig/) the standard
python mechanism for installing packages. For the easiest installation
just type the command (you'll probably need root privileges for that):

    python setup.py install

This will install the library in the default location. For instructions on
how to customize the install procedure read the output of:

    python setup.py --help install

In addition, there are some other commands:

    python setup.py clean -> will clean all trash (*.pyc and stuff)
    python setup.py test  -> will run the complete test suite
    python setup.py bench -> will run the complete benchmark suite
    python setup.py audit -> will run pyflakes checker on source code

To get a full list of avaiable commands, read the output of:

    python setup.py --help-commands
"""

from distutils.core import setup, Command
import sys
import subprocess
import os

# Make sure I have the right Python version.
if sys.version_info[:2] < (3, 0):
    print("Green_roof requires Python 3.0 or newer. Python %d.%d detected" % sys.version_info[:2])
    sys.exit(-1)


modules = [
    'Roof_model.',
    'Roof_model.',
    'Roof_model.',
    'Roof_model.',
    'Roof_model.',
]


class clean(Command):
    """Cleans *.pyc and debian trashs, so you should get the same copy as
    is in the VCS.
    """

    description = "remove build files"
    user_options = [("all", "a", "the same")]

    def initialize_options(self):
        self.all = None

    def finalize_options(self):
        pass

    def run(self):
        import os
        os.system("find . -name '*.pyc' | xargs rm -f")
