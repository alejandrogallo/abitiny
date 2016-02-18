#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from abitiny import __version__ as version

def requireModules(moduleNames=None):
    import re
    if moduleNames is None:
        moduleNames = []
    else:
        moduleNames = moduleNames

    commentPattern = re.compile(r'^\w*?#')
    moduleNames.extend(
        filter(lambda line: not commentPattern.match(line), 
            open('requirements.rst').readlines()))

    return moduleNames

setup(
    name    = 'abitiny',
    version = version,

    author       = 'Alejandro Gallo',
    author_email = 'alejandroamsg@gmail.com',
    url          = "http://github.com/alejandroamsg@gmail.com/abitiny",

    description      = 'Tiny and pedagogical implementation of ab initio codes',
    long_description = open('README.txt').read(),
    classifiers      = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    scripts          = [],
    install_requires = requireModules([

    ]),

    test_suite = 'abitiny',
    zip_sage   = False
)
