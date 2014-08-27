from rosalind.genetools import dna_to_rna

# print dna_to_rna('GATGGAACTTGACTACGTAAATT')

f = open('data/rosalind_rna.txt', 'r')
s = f.read().rstrip()

print dna_to_rna(s)
