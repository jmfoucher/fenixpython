#!/usr/bin/env python

import os

#from distutils.core import setup
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='ModuleName',
    version='0.1',
    author='Jean-Michel Foucher',
    author_email='foucher@piq.co.jp',
    description='Parity Innovations Co. Ltd. Module Name',
    long_description=read('README'),
    license = "to be defined",
    keywords = "keyword1 keyword2",
    url='https://www.piq.co.jp',
    packages=['module'],
    entry_points = {
        'console_scripts' : [
    #      'disp=inspector.commandlines:disp',
    #      'inspector=inspector.commandlines:inspector',
    #      'inspectorGUI=inspector.commandlines:inspectorGUI',
    #      'mesh=inspector.commandlines:meshFactory',
    #      'shutter=inspector.commandlines:shutter',
          ],
        },
    classifiers=[
        #"Development Status :: 3 - Alpha",
        #"Topic :: Utilities",
        #"License :: OSI Approved :: BSD License",
    ],
)
