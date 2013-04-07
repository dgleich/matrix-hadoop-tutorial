Matrix Methods in Hadoop
========================

### David F. Gleich, Computer Science, Purdue University

These codes accompany my presentation on
[Matrix Methods in Hadoop](http://www.slideshare.net/dgleich)
at the BIGDATA Techcon in Boston, MA in April 2013. I suspect 
they'll be used in other presentations as well.  


Overview
--------

The goal in these slides is to demonstrate how to implement 
simple matrix computations in Hadoop using 
Yelp's [mrjob](http://www.github.com/mrjob) system.

* Sparse matrix-vector products
* Matrix-matrix products
* A recommender system for epinions data

Getting started
---------------

1. Get mrjob working. Nothing here will require an actual MapReduce
cluster, but feel free to use one if you wish! I setup a virtualenv
for this and use pip.

    mkdir envs
    virtualenv envs/mrjob
    source envs/mrjob/bin/activate
    pip install mrjob

2. Get the datasets for the recommender system

    make getdata
    
3.     
