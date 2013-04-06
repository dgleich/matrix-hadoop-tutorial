#!/usr/bin/env python

"""
make_sparse_test_data.py
------------------------

Generate random data to use with MapReduce experiments.

Usage:
"""
usage_str = "python %s <nrows>"

import sys
import numpy

if len(sys.argv) != 2:
  print>>sys.stderr, usage_str%(sys.argv[0])
  sys.exit(-1)

m = int(sys.argv[1])
A = numpy.random.randn(m, 1)
for rowid in xrange(m):
  print rowid, A[rowid][0] # derefence the array completely
