from rosalind.iotools import read_fasta

fasta = []
with open('../data/test.fasta') as fp:
    for name, seq in read_fasta(fp):
        fasta.append((name, seq))
