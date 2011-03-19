#!/usr/bin/env python
"""Installs StarPy using distutils

Run:
	python setup.py install
to install the package from the source archive.
"""

import sys,os, string
from distutils.sysconfig import *
from distutils.core import setup


setup (
    name = "starpy",
    version = '1.0.0b1',
    url = "http://starpy.sourceforge.net",
    download_url = "http://sourceforge.net/project/showfiles.php?group_id=164040",
    description = "Twisted Protocols for interaction with the Asterisk PBX",
    author = "Mike C. Fletcher",
    author_email = "mcfletch@vrplumber.com",
    license = "BSD",
    
    packages = [
    'starpy'
    ],
    
    classifiers = [
    """License :: OSI Approved :: BSD License""",
    """Programming Language :: Python""",
    """Topic :: Software Development :: Libraries :: Python Modules""",
    """Intended Audience :: Developers""",
    ],
    keywords = 'asterisk,fastagi,twisted,protocol,manager,ami',
    long_description = """Twisted Protocols for interaction with Asterisk PBX
    
    Provides Asterisk AMI and Asterisk FastAGI protocols under Twisted,
    allowing for fairly extensive customisation of Asterisk operations
    from a Twisted process.""",
    platforms = ['Any'],
)

