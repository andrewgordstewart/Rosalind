from rosalind.genetools import rna_to_protein
from rosalind.iotools import copy_to_clipboard

print('Please input GNA strand')
strand = raw_input("> ")

print(rna_to_protein(strand))
copy_to_clipboard(rna_to_protein(strand))
