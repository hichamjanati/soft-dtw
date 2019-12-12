#! /usr/bin/env python
from __future__ import print_function
import os.path
import sys

from setuptools import find_packages, setup
from setuptools.extension import Extension
from Cython.Build import cythonize

import numpy

extensions = [
    Extension(
        "sdtw.soft_dtw_fast",
        ['sdtw/soft_dtw_fast.pyx'],
    ),
]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)

# get __version__ from _version.py
ver_file = os.path.join('sdtw', '_version.py')
with open(ver_file) as f:
    exec(f.read())


DISTNAME = 'soft-dtw'
DESCRIPTION = "Python implementation of soft-DTW"
LONG_DESCRIPTION = open('README.rst').read()
MAINTAINER = 'Mathieu Blondel'
MAINTAINER_EMAIL = ''
URL = 'https://github.com/mblondel/soft-dtw/'
LICENSE = 'Simplified BSD'
DOWNLOAD_URL = 'https://github.com/mblondel/soft-dtw/'
VERSION = __version__

INSTALL_REQUIRES = ['numpy', 'scikit-learn', 'cython', 'torch']


if __name__ == '__main__':

    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          long_description_content_type='text/x-rst',
          zip_safe=False,  # the package can run out of an .egg file
          packages=find_packages(),
          include_dirs=[numpy.get_include()],
          install_requires=INSTALL_REQUIRES,
          ext_modules=cythonize(extensions))
