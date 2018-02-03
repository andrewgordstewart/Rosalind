from rosalind.genetools import does_overlap
from rosalind.iotools import read_complete_fasta as _read_fasta

with open('../data/rosalind_grph.txt', 'r') as fp:
    fasta = _read_fasta(fp)

k = 3
for s in fasta:
    for t in fasta:
        if does_overlap(s[1], t[1], k):
            print s[0][1:], t[0][1:]




