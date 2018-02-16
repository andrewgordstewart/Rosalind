import string

import numpy as np

from .tables import CODON_TABLE, monoisotopic_mass_table

# TODO: Optimize using numpy arrays/matrices

NUCLEOTIDES_IDX = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def validate_sequence(sequence, sequence_type):
    if sequence_type not in ['dna', 'rna', 'protein']:
        raise ValueError(f"Invalid sequence type: {sequence_type}")

    if not sequence:
        raise ValueError(f"Empty sequence")

    if sequence_type == 'dna':
        symbols = ['A', 'C', 'G', 'T']
    elif sequence_type == 'rna':
        symbols = ['A', 'C', 'G', 'U']
    elif sequence_type == 'protein':
        alphabet = string.ascii_uppercase
        symbols = [letter for letter in alphabet]
        not_symbols = 'BJOUXZ'
        for letter in not_symbols:
            symbols.remove(letter)

    for s in sequence:
        if s not in symbols:
            raise ValueError(f"Invalid {sequence_type} sequence: {sequence}")

    return True


def dna_profile(dna_sequence):
    validate_sequence(dna_sequence, 'dna')

    profile = dict(A=0, C=0, G=0, T=0)
    symbols = ['A', 'C', 'G', 'T']

    for s in dna_sequence:
        profile[s] = profile[s] + 1

    return [profile[i] for i in symbols]


def dna_profile_matrix(dna_sequences):
    """
    Computes the frequencies of each nucleotide in a list of dna sequences.
    :param dna_sequences: list(str)
        List of dna sequences. Must all be valid dna sequences, of the same
        length.

    :return: matrix counts of nucleotide i in position j
             nucleotides are index, in order, by 'ACGT'.
             IE, 'C' is nucleotide 1.
    :rtype: np.matrix
    """
    length = len(dna_sequences[0])

    for seq in dna_sequences:
        validate_sequence(seq, 'dna')
        if len(seq) != length:
            raise ValueError("All sequences must be the same length")

    profile = np.full((4, length), 0)

    # TODO: Optimize this horrible mess with numpy!
    for seq in dna_sequences:
        for i in range(length):
            idx = NUCLEOTIDES_IDX[seq[i]]
            profile[idx][i] += 1

    return profile


def gc_content(dna_sequence):
    validate_sequence(dna_sequence, 'dna')

    content = (dna_sequence.count('C') + dna_sequence.count('G'))
    content = content / float(len(dna_sequence))
    return content


def rna_to_dna(rna_sequence):
    validate_sequence(rna_sequence, 'rna')

    dna_sequence = ''
    for s in rna_sequence:
        if s == 'U':
            dna_sequence = dna_sequence + 'T'
        else:
            dna_sequence = dna_sequence + s
    return dna_sequence


def dna_to_rna(dna_sequence):
    validate_sequence(dna_sequence, 'dna')

    return dna_sequence.replace('T', 'U')


def reverse_compliment(dna_sequence):
    validate_sequence(dna_sequence, 'dna')

    s = dna_sequence[::-1]
    result = ''
    for i in range(len(s)):
        if s[i] == 'A':
            result = result + 'T'
        elif s[i] == 'T':
            result = result + 'A'
        elif s[i] == 'C':
            result = result + 'G'
        elif s[i] == 'G':
            result = result + 'C'

    return result


def rna_to_protein(rna_sequence):
    validate_sequence(rna_sequence, 'rna')

    table = CODON_TABLE

    protein = ''
    for i in range(len(rna_sequence))[::3]:
        try:
            a, b, c = rna_sequence[i], rna_sequence[i+1], rna_sequence[i+2]
            codon = a+b+c
            if codon in ['UAA', 'UAG', 'UGA']:  # codons for end of rna code
                protein = protein + '*'
            elif codon in table:
                protein = protein + table[codon]
            else:
                raise ValueError(f"Invalid codon: {codon}")
        except IndexError:
            pass

    return protein


def dna_to_protein(dna_sequence):
    validate_sequence(dna_sequence, 'dna')

    rna = dna_to_rna(dna_sequence)
    return rna_to_protein(rna)


def does_overlap(s, t, k):

    return s[-(k):] == t[:k] and s != t


def candidate_proteins(sequence, sequence_type='dna'):
    if sequence_type == 'dna':
        pass
    elif sequence_type == 'rna':
        sequence = rna_to_dna(sequence)
    else:
        raise ValueError('Invalid sequence type')

    rev_comp = reverse_compliment(sequence)

    proteins = [dna_to_protein(sequence[i:]) for i in range(3)]
    proteins.extend([dna_to_protein(rev_comp[i:]) for i in range(3)])

    matches = set()

    for p in proteins:
        for i, c in enumerate(p):
            if c == 'M':
                for j, d in enumerate(p[i:]):
                    if d == '*':
                        matches.add(p[i:i+j])
                        break

    return matches


def monoisotopic_mass(sequence, sequence_type='dna'):
    if sequence_type == 'dna':
        protein = dna_to_protein(sequence)
    elif sequence_type == 'rna':
        protein = rna_to_protein(sequence)
    elif sequence_type == 'protein':
        protein = sequence
    else:
        raise ValueError('Invalid sequence type')

    table = monoisotopic_mass_table()

    mass = 0
    for p in protein:
        mass = mass + table[p]

    return mass


def reverse_palindrome(sequence, sequence_type='dna'):
    if sequence_type == 'rna':
        dna = rna_to_dna(sequence)
    elif sequence_type == 'dna':
        dna = sequence
    else:
        raise ValueError('Invalid sequence type')

    rev_comp = reverse_compliment(dna)

    return rev_comp == dna


def splice(sequence, introns, sequence_type='dna'):
    '''
    Splices _sequence_, given a list _introns_ of introns.
    Each intron in _introns_ is removed from _sequence_, and
    the result is returned.
    '''
    if sequence_type == 'rna':
        dna = rna_to_dna(sequence)
    elif sequence_type == 'dna':
        dna = sequence
    else:
        raise ValueError('Invalide sequence type')

    for intron in introns:
        marker = 0
        while marker != -1:
            marker = dna.find(intron)
            dna = dna.replace(intron, '')

    protein = dna_to_protein(dna).replace('*', '')
    return protein
