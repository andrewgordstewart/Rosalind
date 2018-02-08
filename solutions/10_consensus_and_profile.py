from rosalind.iotools import read_fasta as read_fasta
from rosalind.genetools import dna_profile_matrix


NUCLEOTIDES_IDX = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def solve(dataset):
    dna_strings = [seq for _, seq in read_fasta(dataset)]

    profile = dna_profile_matrix(dna_strings)

    consensus = ''.join(nucleotide(counts) for counts in profile.transpose())

    result = consensus
    for idx, counts in enumerate(profile):
        counts = list(str(c) for c in counts)
        result = result + f"\n{NUCLEOTIDES_IDX[idx]}: {' '.join(counts)}"

    return result


def nucleotide(counts):
    return NUCLEOTIDES_IDX[counts.argmax()]
