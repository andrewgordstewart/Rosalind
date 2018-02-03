import rosalind.tables
import rosalind.genetools

# the number of choices of codons for a given protein code
table = rosalind.tables.reverse_codon_table()
choice_table = {}
for c in table:
    choice_table[c] = len(table[c])

protein = open('../data/rosalind_mrna.txt', 'r').read().rstrip()

n = 1000000
choices = 1
for c in protein:
    # print c, choices, choice_table[c], (choices*choice_table[c])%n, '\n', '-'*79
    choices = (choices*choice_table[c]) % n

print (choices*3)%n         # account for the 3 choices of the stop codon
