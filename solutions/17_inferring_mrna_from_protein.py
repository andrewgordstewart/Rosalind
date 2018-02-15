from rosalind.tables import REVERSE_CODON_TABLE

MODULUS = 1000000


def solve(dataset):
    protein = dataset.rstrip()
    # the number of choices of codons for a given protein code
    table = REVERSE_CODON_TABLE
    choice_table = {}
    for c in table:
        choice_table[c] = len(table[c])

    choices = 1
    for c in protein:
        choices = (choices*choice_table[c]) % MODULUS

    return (choices*3) % MODULUS  # account for the 3 choices of the stop codon
