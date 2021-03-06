"""
Created on Mon Dec 02 23:56:59 2013
@author: Greg
http://rosalind.info/problems/cons/
Returns a consensus string and profile matrix for a series of fasta strings
"""

from Bio import SeqIO
from collections import Counter

s=[]
handle = open('rosalind_cons.txt', "rU")
for record in SeqIO.parse(handle, "fasta"):
    s.append(str(record.seq))
handle.close()

a=[Counter([seq[x] for seq in s]) for x in range(len(s[0]))]
print ''.join([a[x].most_common(1)[0][0] for x in range(len(a))])
print 'A: ' + ' '.join([str(a[x]['A']) for x in range(len(a))])
print 'C: ' + ' '.join([str(a[x]['C']) for x in range(len(a))])
print 'G: ' + ' '.join([str(a[x]['G']) for x in range(len(a))])
print 'T: ' + ' '.join([str(a[x]['T']) for x in range(len(a))])