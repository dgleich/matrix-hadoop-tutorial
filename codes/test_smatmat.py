#!/usr/bin/env python

import sys

""" Test sparse matrix matrix product. No error checking here. """

matfileA = sys.argv[1]
matfileB = sys.argv[2]

Amat = [] # create a list of (row,col,val) tuples
Bmat = {} # a dict of (row,val) relationships

with open(matfileA) as mfile:
    for line in mfile:
        vals = [float(p) for p in line.split()]
        row = int(vals[0])
        for i in xrange(1,len(vals),2):
            Amat.append((row,int(vals[i]),vals[i+1]))
with open(matfileB) as mfile:
    for line in mfile:
        vals = [float(p) for p in line.split()]
        row = int(vals[0])
        rowvals = [(int(vals[i]),vals[i+1]) for i in xrange(1,len(vals),2)]
        Bmat[row] = rowvals
# transpose B     
AB = {}            
for (Arow,Acol,Aval) in Amat:
    if Acol in Bmat:
        for (Bcol,Bval) in Bmat[Acol]:
            if (Arow,Bcol) not in AB:
                AB[(Arow,Bcol)] = 0.
            AB[(Arow,Bcol)] += Aval * Bval

C = {}
for key,val in AB.iteritems():
    row,col = key
    if row not in C:
        C[row] = []
    C[row].extend((col,val))
for i in xrange(max(C.iterkeys())+1):
    if i not in C:
        print "%i"%(i)
    else:
        print "%i %s"%(i," ".join([str(c) for c in C[i]]))
        
        
