from codon_table import codon_table

def valid_sequence(sequence, sequence_type):
    if not sequence_type in ['dna', 'rna']:
        return False

    if sequence_type == 'dna':
        symbols = ['A', 'C', 'G', 'T']
    elif sequence_type == 'rna':
        symbols = ['A', 'C', 'G', 'U']

    for s in sequence:
        if not s in symbols:
            return False

    return True

def dna_profile(dna_sequence):
    if not valid_sequence(dna_sequence, 'dna'):
        raise ValueError

    profile = dict(A=0, C=0, G=0, T=0)
    symbols = ['A', 'C', 'G', 'T']

    for s in dna_sequence:
        profile[s] = profile[s] + 1

    return [profile[i] for i in symbols]

def gc_content(dna_sequence):
    if not valid_sequence(dna_sequence, 'dna'):
        raise ValueError

    content = (dna_sequence.count('C') + dna_sequence.count('G'))
    content = content / float(len(dna_sequence))
    return content

def rna_to_dna(rna_sequence):
    if not valid_sequence(dna_sequence, 'dna'):
            raise ValueError

    dna_sequence = ''
    for s in rna_sequence:
        if s == 'U':
            dna_sequence = dna_sequence + 'T'
        else:
            dna_sequence = dna_sequence + s
    return dna_sequence

def dna_to_rna(dna_sequence):
    if not valid_sequence(dna_sequence, 'dna'):
            raise ValueError

    rna_sequence = ''
    for s in dna_sequence:
        if s == '\n':
            pass
        if s == 'T':
            rna_sequence = rna_sequence + 'U'
        else:
            rna_sequence = rna_sequence + s
    return rna_sequence

def reverse_compliment(dna_sequence):
    if not valid_sequence(dna_sequence, 'dna'):
        raise ValueError

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
    if not valid_sequence(rna_sequence, 'rna') or len(rna_sequence)%3 != 0:
        raise ValueError

    table = codon_table()

    protein = ''
    for i in range(len(rna_sequence))[::3]:
        a, b, c = rna_sequence[i], rna_sequence[i+1], rna_sequence[i+2]
        codon = a+b+c
        # print i, codon
        if codon in ['UAA', 'UAG', 'UGA']: #codons for end of rna code
            return protein
        elif codon in table:
            # print codon, table[codon]
            protein = protein + table[codon]
        else:
            raise ValueError

    return protein


def is_a_substring(s, t, k):

    return None



if __name__ == '__main__':
    # print dna_profile('CACGT')
    # print dna_profile('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')?
    # print dna_to_rna('GATGGAACTTGACTACGTAAATT')
    # print reverse_compliment('AAAACCCGGT')

    # error = 100*gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT') - 60.919540
    # in_threshold = (-0.001 < error < 0.001)
    # print error, in_threshold
    # print rna_to_protein('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')

    pass
