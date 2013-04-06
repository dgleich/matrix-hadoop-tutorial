#!/usr/bin/env python

"""
make_rand_data.py
-----------------

Generate random data to use with MapReduce experiments.

Usage:
"""
usage_str = "python %s <nrows> <ncols>"

import sys
import numpy

if len(sys.argv) != 3:
  print>>sys.stderr, usage_str%(sys.argv[0])
  sys.exit(-1)

m = int(sys.argv[1])
n = int(sys.argv[2])

A = numpy.random.randn(m, n)
numpy.savetxt(sys.stdout, A)
