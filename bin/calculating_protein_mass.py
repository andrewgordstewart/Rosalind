from rosalind.genetools import monoisotopic_mass

protein = 'SKADYEK'
with open('../data/rosalind_prtm.txt', 'r') as fp:
    protein = fp.readline().rstrip()


mass = monoisotopic_mass(protein, 'protein')

mass = ("%.3f" % mass)

from rosalind.iotools import copy_to_clipboard

copy_to_clipboard(mass)
