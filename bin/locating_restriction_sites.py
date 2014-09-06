from rosalind.genetools import reverse_compliment
from rosalind.iotools import read_complete_fasta

with open('../data/rosalind_revp.txt', 'r') as fp:
    protein = read_complete_fasta(fp)[0][1]

rev_comp = reverse_compliment(protein)


n = len(protein)
locations = []
for i in range(0, n):
    for j in range(i+4, n+1):
        if protein[i:j] == rev_comp[n-j:n-i]:
            locations.append((i+1, j-i))



for i, j in locations:
    print i, j
