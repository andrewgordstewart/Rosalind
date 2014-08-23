from nose.tools import *
import rosalind.dnatools

def valid_sequence_test():
    assert_equals(rosalind.dnatools.valid_sequence('ABCD', 'dna'), False)
    assert_equals(rosalind.dnatools.valid_sequence('ACGTGC', 'dna'), True)
    assert_equals(rosalind.dnatools.valid_sequence('ACGBTGC', 'dna'), False)
    assert_equals(rosalind.dnatools.valid_sequence('ACGUUGUC', 'rna'), True)
    assert_equals(rosalind.dnatools.valid_sequence('ACGRB', 'rna'), False)

def dna_profile_test():
    assert_equals(rosalind.dnatools.dna_profile('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'), [20, 12, 17, 21])

def dna_to_rna_test():
    assert_equals(rosalind.dnatools.dna_to_rna('GATGGAACTTGACTACGTAAATT'),
                                                    'GAUGGAACUUGACUACGUAAAUU')

def reverse_compliment_test():
    assert_equals(rosalind.dnatools.reverse_compliment('AAAACCCGGT'), 'ACCGGGTTTT')
    assert_equals(rosalind.dnatools.reverse_compliment('GTCA'), 'TGAC')
    # assert_equals(rosalind.dnatools.reverse_compliment( )
    # assert_equals(rosalind.dnatools.reverse_compliment( )
    # assert_equals(rosalind.dnatools.reverse_compliment( )
