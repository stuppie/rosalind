

from Bio import SeqIO
s=[]
for record in SeqIO.parse(open('rosalind_grph.txt', "rU"), "fasta"):
    s.append((record.name,str(record.seq)))

for num in range(len(s)):
    a=[x[1][:3] for x in s]
    b=s[num][1][-3:]
    ii=[i for i, x in enumerate(a) if x == b]
    ii=[x for x in ii if x != num]
    
    for x in ii:
        print s[num][0] + ' ' + s[x][0]