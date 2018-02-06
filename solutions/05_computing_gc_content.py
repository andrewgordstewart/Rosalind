from rosalind.iotools import read_fasta
from rosalind.genetools import gc_content


def solve(dataset):
    fasta = {}
    for name, seq in read_fasta(dataset):
        fasta[name] = seq

    max_gc = 0
    for key in fasta:
        if gc_content(fasta[key]) > max_gc:
            max_gc, max_key = gc_content(fasta[key]), key

    return "\n".join((max_key, str(100*max_gc)))
