from rosalind.genetools import dna_to_protein
from rosalind.iotools import read_complete_fasta as read_fasta

with open('../data/rosalind_splc.txt', 'r') as fp:
    fasta = read_fasta(fp)
dna = fasta[0][1]
print len(dna)

introns = []
for i in range(1, len(fasta)):
    introns.append(fasta[i][1])

from rosalind.genetools import splice

protein = splice(dna, introns)

from rosalind.iotools import copy_to_clipboard
copy_to_clipboard(protein)
