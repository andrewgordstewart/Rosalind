CODON_TABLE = {
    'GUC': 'V',
    'ACC':  'T',
    'GUA':  'V',
    'GUG':  'V',
    'GUU':  'V',
    'AAC':  'N',
    'CCU':  'P',
    'UGG':  'W',
    'AGC':  'S',
    'AUC':  'I',
    'CAU':  'H',
    'AAU':  'N',
    'AGU':  'S',
    'ACU':  'T',
    'CAC':  'H',
    'ACG':  'T',
    'CCG':  'P',
    'CCA':  'P',
    'ACA':  'T',
    'CCC':  'P',
    'GGU':  'G',
    'UCU':  'S',
    'GCG':  'A',
    'UGC':  'C',
    'CAG':  'Q',
    'GAU':  'D',
    'UAU':  'Y',
    'CGG':  'R',
    'UCG':  'S',
    'AGG':  'R',
    'GGG':  'G',
    'UCC':  'S',
    'UCA':  'S',
    'GAG':  'E',
    'GGA':  'G',
    'UAC':  'Y',
    'GAC':  'D',
    'GAA':  'E',
    'AUA':  'I',
    'GCA':  'A',
    'CUU':  'L',
    'GGC':  'G',
    'AUG':  'M',
    'CUG':  'L',
    'CUC':  'L',
    'AGA':  'R',
    'CUA':  'L',
    'GCC':  'A',
    'AAA':  'K',
    'AAG':  'K',
    'CAA':  'Q',
    'UUU':  'F',
    'CGU':  'R',
    'CGA':  'R',
    'GCU':  'A',
    'UGU':  'C',
    'AUU':  'I',
    'UUG':  'L',
    'UUA':  'L',
    'CGC':  'R',
    'UUC':  'F'
}


def reverse_codon_table():
    '''
    The reverse of the codon table. Since the codon table is not bijective,
    each amino acid corresponds to a list of precursor codons.
    '''
    table = CODON_TABLE
    reverse_table = {}
    for codon in table:
        reverse_table[table[codon]] = []

    for codon in table:
        reverse_table[table[codon]].append(codon)
    return reverse_table


def monoisotopic_mass_table():
    '''
    Masses of the monoisotopic versions of amino acids. Monoisotopic amino
    acids are assumed to consist of the most common isotope of each atom,
    which is typically the lightest isotope.

    http://en.wikipedia.org/wiki/Monoisotopic_mass
    '''
    table = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }

    return table


if __name__ == '__main__':
    print(codon_table())
    print('-'*79)
    print(reverse_codon_table())
