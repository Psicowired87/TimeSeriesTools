#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for the installation of TimeSeriesTools.
It is possible to install this package with

python setup.py install
"""

from glob import glob
import sys
import os
import warnings
from TimeSeriesTools import release

## Temporally commented
#if os.path.exists('MANIFEST'):
#    os.remove('MANIFEST')


## Definition of useful functions
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


## Check problems with the setuptools
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()


version = release.write_versionfile()

packages = ['TimeSeriesTools',
            'TimeSeriesTools.artificial_data',
            'TimeSeriesTools.Burst_detection', 'TimeSeriesTools.Causality',
            'TimeSeriesTools.Feature_extraction', 'TimeSeriesTools.Measures',
            'TimeSeriesTools.Prediction', 'TimeSeriesTools.Regime_detection',
            'TimeSeriesTools.Similarities', 'TimeSeriesTools.Sorting',
            'TimeSeriesTools.tests', 'TimeSeriesTools.Transformation',
            'TimeSeriesTools.TS_statistics', 'TimeSeriesTools.utils'
            ]

docdirbase = 'share/doc/TimeSeriesTools-%s' % version
# add basic documentation
data = [(docdirbase, glob("*.txt"))]
# add examples
for d in ['advanced',
          'algorithms']:
    dd = os.path.join(docdirbase, 'examples', d)
    pp = os.path.join('examples', d)
    data.append((dd, glob(os.path.join(pp, "*.py"))))
    data.append((dd, glob(os.path.join(pp, "*.bz2"))))
    data.append((dd, glob(os.path.join(pp, "*.gz"))))
    data.append((dd, glob(os.path.join(pp, "*.mbox"))))
    data.append((dd, glob(os.path.join(pp, "*.edgelist"))))

# add the tests
#package_data = {'TimeSeriesTools': ['tests/*.py']}
package_data = {}

install_requires = ['numpy', 'scipy', 'pandas', 'matplotlib']

## Setup
setup(name=release.name,
      version=version,
      description=release.description,
      license=release.license,
      platforms=release.platforms,
      maintainer=release.maintainer,
      maintainer_email=release.maintainer_email,
      author=release.author,
      author_email=release.author_email,
      url=release.url,
      classifiers=release.classifiers,
      long_description=read('README.md'),
      packages=packages,
      install_requires=install_requires,
      )
