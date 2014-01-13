# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:13:05 2014

@author: Edison Lab
"""

from Bio import SeqIO
ss=[]
file = open("rosalind_lcsm.txt", "r")
for record in SeqIO.parse(file, "fasta"):
    ss.append(str(record.seq))

def containsSS(ss, l):
    for i in range(len(ss[0])-l+1):
         if all([s.find(ss[0][i:i+l]) > -1 for s in ss]):
             return ss[0][i:i+l]
    return False

#for l in xrange(2,min(map(len,ss))):
#    if not containsSS(ss, l):
#        l=l-1
#        print containsSS(ss,l)
#        break

#binary search
l=int(ceil(min(map(len,ss))/2))
mid=l
left=0
right=min(map(len,ss))

while right-left>1:
    print l
    if containsSS(ss,l):
        left=l
        l=left+int(floor((right-left)/2))
    else:
        right=l
        l=left+int(floor((right-left)/2))
print containsSS(ss,l)