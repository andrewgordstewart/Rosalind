from rosalind.iotools import read_complete_fasta as read_fasta
from rosalind.genetools import candidate_proteins

with open('../data/rosalind_orf.txt', 'r') as fp:
    dna = read_fasta(fp)[0][1]


proteins = candidate_proteins(dna, 'dna')
answer = ''
for p in proteins:
    answer = answer + p + '\n'


answer.rstrip()
print answer

# from rosalind.iotools import copy_to_clipboard

# copy_to_clipboard(answer)

