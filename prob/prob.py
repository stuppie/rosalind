# -*- coding: utf-8 -*-
"""
Created on Tue Dec 03 00:26:09 2013

@author: Greg
"""

with open('rosalind_prob.txt') as f:
    s = f.readline().strip()
    gcs = f.readline()
    gcs = map(float,gcs.split())



a=[sum(log10(array([gc/2 if letter in 'GC' else (1-gc)/2 for letter in s]))) for gc in gcs]

print ' '.join(["%0.3f" % i for i in a])