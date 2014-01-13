# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 18:31:56 2014
@author: Edison Lab
Speeding Up Motif Finding
http://rosalind.info/problems/kmp/
Returns the failure array of the sequence.

Example input:
>Rosalind_87
CAGCATGGTATCACAGCAGAG
Example output:
0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
"""

with open('rosalind_kmp.txt') as f:
    f.readline()
    s=f.read().replace('\n','')

#s='CAGCATGGTATCACAGCAGAG'
failure=[0] * len(s)
for i in range(1,len(s)):
    s1=s[0:i+1]
    f=failure[i-1]+1
    while f > 0:
        if s1[0:f]==s1[-f:]:
            failure[i]=f
            f=0
        else:
            f-=1

fs= ' '.join(map(str, failure))