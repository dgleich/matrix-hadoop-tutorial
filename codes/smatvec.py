#!/usr/bin/env python

from mrjob.job import MRJob

class MRRowSum(MRJob):
    def mapper(self, key, line):
        yield key, sum(float(tok) for tok in line.split())

if __name__=='__main__':
    MRRowSum.run()        
