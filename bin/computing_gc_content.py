from rosalind.iotools import read_fasta
from rosalind.genetools import gc_content

fasta = {}
with open('../data/rosalind_gc.txt') as fp:
    for name, seq in read_fasta(fp):
        fasta[name] = seq
        # fasta.append((name, seq))
    fp.close

# print fasta
# key = raw_input("input key: ")
# key = '>Rosalind_0808'

max_gc = 0
for key in fasta:
    if gc_content(fasta[key]) > max_gc:
        max_gc, max_key = gc_content(fasta[key]), key

print max_key,  max_gc
