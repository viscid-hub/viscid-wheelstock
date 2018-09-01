#!/usr/bin/env python

from __future__ import print_function
import platform

# Version numbers of the earliest versions of Numpy with
# binary wheels on PyPI for a given python version / platform

NPY_WHEEL_VERSIONS = {
  # py27
  'cp27-Darwin': '1.9.3',
  'cp27-Linux': '1.9.3',
  'cp27-Windows': '1.14.5',  # should be 1.10.4
  # py35
  'cp35-Darwin': '1.9.3',
  'cp35-Linux': '1.9.3',
  'cp35-Windows': '1.14.5',  # should be 1.10.4
  # py36
  'cp36-Darwin': '1.11.3',
  'cp36-Linux': '1.11.3',
  'cp36-Windows': '1.14.5',  # should be 1.12.1
  # py37
  'cp37-Darwin': '1.14.5',
  'cp37-Linux': '1.14.5',
  'cp37-Windows': '1.14.5',
}

key = ('cp'
       + ''.join(str(i) for i in platform.python_version_tuple()[:2])
       + '-'
       + platform.system()
       )

print(NPY_WHEEL_VERSIONS[key])
