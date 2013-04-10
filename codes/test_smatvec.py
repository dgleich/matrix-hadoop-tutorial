#!/usr/bin/env python

import sys

""" Test sparse matrix vector product. No error checking here. """

matfile = sys.argv[1]
vecfile = sys.argv[2]

mat = [] # create a list of (row,col,val) tuples
vec = {} # a dict of (row,val) relationships

with open(matfile) as mfile:
    for line in mfile:
        vals = [float(p) for p in line.split()]
        row = int(vals[0])
        for i in xrange(1,len(vals),2):
            mat.append((row,int(vals[i]),vals[i+1]))
with open(vecfile) as vfile:
    for line in vfile:
        vals = [float(p) for p in line.split()]
        vec[int(vals[0])] = vals[1]
mv = {} # a dict of (row,val) relationships
for nnz in mat:
    if nnz[0] not in mv: 
        mv[nnz[0]] = 0.
    mv[nnz[0]] += nnz[2]*vec[nnz[1]]
for i in xrange(max(mv.iterkeys())+1):
    if i not in mv:
        print "%i 0"%(i)
    else:
        print "%i %f"%(i,mv[i])
        
        
