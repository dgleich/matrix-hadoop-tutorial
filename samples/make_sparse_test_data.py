#!/usr/bin/env python

"""
make_sparse_test_data.py
------------------------

Generate random data to use with MapReduce experiments.

Usage:
"""
usage_str = "python %s <nrows> <ncols> <density>"

import sys
import numpy

if len(sys.argv) != 4:
  print>>sys.stderr, usage_str%(sys.argv[0])
  sys.exit(-1)

m = int(sys.argv[1])
n = int(sys.argv[2])
density = float(sys.argv[3])

nnz = max( min( int(m*n*density), m*n), 0)
rand_seq = numpy.random.permutation(m*n)[:nnz]
row  = rand_seq / n
col  = rand_seq % n
vals = numpy.random.randn(nnz,1)

mat = [ {} for _ in xrange(m) ] # create placeholder dictionaries
for i in xrange(nnz):
  mat[row[i]][col[i]] = vals[i][0] # dereference the numpy array

for rowid,vals in enumerate(mat):
  print rowid,
  for col,val in vals.items():
    print col, val,
  print 
