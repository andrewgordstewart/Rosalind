import rosalind.genetools, sys

f = open('../data/rosalind_dna.txt', 'r')
s = f.read()
for c in rosalind.genetools.dna_profile(s):
    sys.stdout.write(str(c))
    sys.stdout.write(' ')
