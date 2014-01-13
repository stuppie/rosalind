# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 12:07:54 2014

@author: Edison Lab
"""
import numpy as np
with open('rosalind_spec.txt') as f:
    n=map(float, f.readlines())

am=makeAAdict()
masses=np.diff(n)
protein=[]
for aa in masses:
    protein.append(np.array(am.keys())[abs(am.values() - aa) < .001][0])

print ''.join(protein)