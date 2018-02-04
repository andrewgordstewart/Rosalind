from rosalind.iotools import parse_fasta
from rosalind.genetools import validate_sequence
import urllib

# Get the names of the proteins
name_list = open('../data/rosalind_mprt.txt', 'r').readlines()
for name in name_list: name = name.rstrip()

# Create a list of urls to the fasta sequences
url_list = ['http://www.uniprot.org/uniprot/' + name.rstrip() + '.fasta' for name in name_list]

# Grab the protein fastas and parse them
protein_fasta_list = [urllib.urlopen(url).read() for url in url_list]
pure_protein_list = [parse_fasta(protein)[1] for protein in protein_fasta_list]


"""
Look for a particular protein motif in a protein sequence.
- A protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
- The motif parameter should be a list with elements of the form
  (quality, acid)
  e.g. the above motif N{P}[ST]{P} would be written as
    [('is', ['N']),
     ('is not', ['P']),
     ('is', [S, T]),
     ('is not', [P])]
"""
def look_for_motif(sequence, motif):
    validate_sequence(sequence, 'protein')

    # print 'checking %s for %s' % (sequence, motif)

    def check_motif(string):
        if len(string) != len(motif):
            raise ValueError

        for i, x in enumerate(motif):
            if (x[0] == 'is' and string[i] not in x[1]
                or
                x[0] == 'is not' and string[i] in x[1]):
                return False
        return True

    a = len(sequence)
    b = len(motif)
    result = []

    for i in xrange(a-b):
        if check_motif(sequence[i:i+b]):
            result.append(i+1)

    return result

motif = [('is', ['N']),
     ('is not', ['P']),
     ('is', ['S', 'T']),
     ('is not', ['P'])]

for i, protein in enumerate(pure_protein_list):
    x = look_for_motif(protein, motif)
    if x:
        print name_list[i],
        for i in x: print i,
        print ''
        # print x

if __name__ == '__main__':
    pass
