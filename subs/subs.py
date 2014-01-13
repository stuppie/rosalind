# -*- coding: utf-8 -*-
"""
Created on Mon Dec 02 23:45:20 2013

@author: Greg
"""
with open('rosalind_subs.txt') as f:
    s=f.readline()
    t=f.readline()

out=sorted(list(set([s.find(t, x)+1 for x in range(len(s)) if t in s[x:]])))
print ' '.join(map(str, out))