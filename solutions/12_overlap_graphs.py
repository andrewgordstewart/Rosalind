from rosalind.genetools import does_overlap
from rosalind.iotools import read_fasta as read_fasta

k = 3


def solve(dataset):
    fasta = [f for f in read_fasta(dataset)]
    result = []
    for s in fasta:
        for t in fasta:
            if does_overlap(s[1], t[1], k):
                result.append(s[0] + ' ' + t[0])

    return '\n'.join(result)
