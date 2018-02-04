from rosalind.genetools import dna_to_rna


def solve(dna_string):
    return dna_to_rna(dna_string.rstrip())
