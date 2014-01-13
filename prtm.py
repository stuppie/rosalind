# -*- coding: utf-8 -*-
"""
Created on Thu Jan 09 18:14:44 2014

@author: Edison Lab
"""
reverseMap = {}
for protein, mass in proteinMass.iteritems():
    reverseMap["{0:.4f}".format(mass)] = protein

def makeAAdict():
    am=dict()
    with open('aa.txt') as f:
        for line in f:
            line=line.split()
            am[line[0]]=float(line[1])
    return am

if __name__ == "__main__":
    protein='WMQS'
    mass=0
    for aa in protein:
        mass+=am[aa]
