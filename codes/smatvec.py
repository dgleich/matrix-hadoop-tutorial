#!/usr/bin/env python

from mrjob.job import MRJob

class SparseMatVec(MRJob):
    """ First join the vector to the matrix based on columns,
    (joinmap, joinred) then actually do the 
    multiplication (multmap, multred) """
    
    def joinmap(self, key, line):
        vals = [float(v) for v in  line.split()]
        if len(vals) == 2:
            # this is a piece of the vector
            yield (vals[0], (vals[1],))
        else:
            # this is a piece of the matrix
            row = vals[0]
            for i in xrange(1,len(vals),2):
                yield (vals[i], (row, vals[i+1]))

    def joinred(self, key, vals):
        # align all data on columns
        # find the vector, and form all the products
        # this code suffers from a large value problem,
        # you could fix that with a secondary sort
        vecval = 0. # setup default val to support sparse vectors
        matvals = []
        for val in vals:
            if len(val) == 1:
                vecval += val[0]
            else:
                matvals.append(val)
                
        for val in matvals:
            yield (val[0], val[1]*vecval)
        
    def sumred(self, key, vals):
        yield (key, sum(vals))
        
    def steps(self):
        return [self.mr(mapper=self.joinmap, reducer=self.joinred),
            self.mr(mapper=None, reducer=self.sumred)]
    

if __name__=='__main__':
    SparseMatVec.run()        
