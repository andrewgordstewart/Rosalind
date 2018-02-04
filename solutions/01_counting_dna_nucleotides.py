from rosalind.genetools import dna_profile

def solve(dna_string):
    return ' '.join(str(num) for num in dna_profile(dna_string.strip()))
