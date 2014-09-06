from nose.tools import *
import rosalind.genetools

def valid_sequence_test():
    assert_equals(rosalind.genetools.valid_sequence('ABCD', 'dna'), False)
    assert_equals(rosalind.genetools.valid_sequence('ACGTGC', 'dna'), True)
    assert_equals(rosalind.genetools.valid_sequence('ACGBTGC', 'dna'), False)
    assert_equals(rosalind.genetools.valid_sequence('ACGUUGUC', 'rna'), True)
    assert_equals(rosalind.genetools.valid_sequence('ACGRB', 'rna'), False)
    assert_equals(rosalind.genetools.valid_sequence('ABC', 'protein'), False)
    assert_equals(rosalind.genetools.valid_sequence('MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK', 'protein'), True)

def dna_profile_test():
    assert_equals(rosalind.genetools.dna_profile('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'), [20, 12, 17, 21])

def dna_to_rna_test():
    assert_equals(rosalind.genetools.dna_to_rna('GATGGAACTTGACTACGTAAATT'),
                                                    'GAUGGAACUUGACUACGUAAAUU')

def reverse_compliment_test():
    assert_equals(rosalind.genetools.reverse_compliment('AAAACCCGGT'), 'ACCGGGTTTT')
    assert_equals(rosalind.genetools.reverse_compliment('GTCA'), 'TGAC')
    # assert_equals(rosalind.genetools.reverse_compliment( )
    # assert_equals(rosalind.genetools.reverse_compliment( )
    # assert_equals(rosalind.genetools.reverse_compliment( )

def gc_content_test():
    error = 100*rosalind.genetools.gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT') - 60.919540
    assert -.001 < error < .001

def rna_to_protein_test():
    s1 = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    s2 = 'MAMAPRTEINSTRING'

    assert_equals(rosalind.genetools.rna_to_protein(s1), s2)
