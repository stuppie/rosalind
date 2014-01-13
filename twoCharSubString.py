# -*- coding: utf-8 -*-
"""
Created on Mon Dec 02 00:11:10 2013

@author: Greg
"""

def doIt(line):
    length=len(line)
    while length>1:
        for start in reversed(range(len(line)-length+1)):
            if len(set(line[start:start+length]))==2:
                return line[start:start+length]
        length-=1
        
line='aabbbcc'
print doIt(line)