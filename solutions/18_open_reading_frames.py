from rosalind.iotools import read_fasta
from rosalind.genetools import candidate_proteins


def solve(dataset):
    dna = list(read_fasta(dataset))[0][1]

    proteins = candidate_proteins(dna, 'dna')
    answer = ''.join(p + '\n' for p in proteins)

    answer.rstrip()
    return answer
