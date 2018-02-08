from rosalind.genetools import rna_to_protein


def solve(dataset):
    return rna_to_protein(dataset.strip())
