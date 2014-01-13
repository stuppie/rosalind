# -*- coding: utf-8 -*-
"""
Created on Sun Dec 08 21:01:54 2013

@author: Greg
"""
import pdb, traceback, sys
def lssidx(a,b):
        longest=0
        for i in range(len(a)):
            for j in range(i, len(a)):
                if j-i< ceil(len(a)/2):
                    continue
                if longest<j-i and a[i:j] in b:
                    longest=j-i
                    longestidx=(i,j)
        if longest==0:
            return (0,0)
        else:
            return longestidx

def lss(a,b):
    idx=lssidx(a,b)
    if idx[0]==0:
        ls=b+a[idx[1]:]
    elif idx[1]==len(a)-1:
        ls=a+b[idx[1]-idx[0]+1:]
    else:
        ls=a
    return ls
    
from Bio import SeqIO
s=[]
for record in SeqIO.parse(open('rosalind_long.txt', "rU"), "fasta"):
    s.append((record.name,str(record.seq)))

i=0
ls=''
while i < len(s):
    ls=lss(ls,s[i][1])
    i=i+1

from Tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(ls)
r.destroy()