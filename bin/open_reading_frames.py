from rosalind.iotools import read_complete_fasta as read_fasta
from rosalind.genetools import dna_to_protein
from rosalind.genetools import reverse_compliment

with open('../data/fasta_dna_sample.txt', 'r') as fp:
    dna = read_fasta(fp)

dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

protein = dna_to_protein(dna)
rev_comp = reverse_compliment(dna)
rev_protein = dna_to_protein(rev_comp)

proteins = [dna_to_protein(dna[i:]) for i in range(3)]
proteins.extend([dna_to_protein(rev_comp[i:]) for i in range(3)])

matches = set()
for p in proteins:
    for i, c in enumerate(p):
        if c == 'M':
            for j, d in enumerate(p[i:]):
                if d == '*':
                    matches.add(p[i:i+j])
                    break

for m in matches:
    print m
