#!/usr/bin/env python

from mrjob.job import MRJob
from mrjob.compat import get_jobconf_value
import itertools

class SparseMatMatMult(MRJob):
    """ First, join the two matrices based on columns, then output
    the cartesian product of the columns, which forms the input for
    the product. """
    
    def configure_options(self):
        super(SparseMatMatMult,self).configure_options()
        self.add_passthrough_option('--A-matrix',default='A',
            dest='Amatname')
    
    def parsemat(self):
        """ Return 1 if this is the A matrix, otherwise return 2"""
        fn = get_jobconf_value('map.input.file')
        if self.options.Amatname in fn: 
            return 1
        else:
            return 2
    
    def joinmap(self, key, line):
        mtype = self.parsemat()
        vals = [float(v) for v in  line.split()]
        row = int(vals[0])
        rowvals = [(int(vals[i]),vals[i+1]) for i in xrange(1,len(vals),2)]
        if mtype==1:
            # rowvals are the entries in the row
            # we output the entire row for each column
            for val in rowvals:
                # reorganize data by columns
                yield (val[0], (row, val[1]))
        else:
            yield (row, (rowvals,))
            
    def joinred(self, key, vals):
        # each key is a column of the matrix.
        # and there are two types of values:
        #  len == 2 (1, row, A_row,key) # a column of A
        #  len == 1 rowvals # a row of B
        
        # load the data into memory       
        brow = []
        acol = []
        for val in vals:
            if len(val) == 1:
                brow.extend(val[0])
            else:
                acol.append(val)
        
        for (bcol,bval) in brow:
            for (arow,aval) in acol:
                yield ((arow,bcol), aval*bval)
    
    def sumred(self, key, vals):
        yield (key, sum(vals))
        
    def rowgroupmap(self, key, val):
        yield key[0], (key[1], val)
        
    def appendred(self, key, vals):
        yield key, list(itertools.chain.from_iterable(vals))
        
    def steps(self):
        return [self.mr(mapper=self.joinmap, reducer=self.joinred),
            self.mr(mapper=None, reducer=self.sumred),
            self.mr(mapper=self.rowgroupmap, reducer=self.appendred)]

if __name__=='__main__':
    SparseMatMatMult.run()        
