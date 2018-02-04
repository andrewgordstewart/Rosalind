import pytest
from rosalind import genetools

@pytest.mark.parametrize("sequence,sequence_type,valid", [
    ('ABCD', 'dna', False),
    ('ACGTGC', 'dna', True),
    ('ACGBTGC', 'dna', False),
    ('ACGUUGUC', 'rna', True),
    ('ACGRB', 'rna', False),
    ('ABC', 'protein', False),
    ('MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK', 'protein', True)
])
def test_valid_sequence(sequence, sequence_type, valid):
    assert genetools.valid_sequence(sequence, sequence_type) == valid

def test_dna_profile():
    assert genetools.dna_profile('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') == [20, 12, 17, 21]

def test_dna_to_rna():
    assert genetools.dna_to_rna('GATGGAACTTGACTACGTAAATT') == 'GAUGGAACUUGACUACGUAAAUU'

@pytest.mark.parametrize("dna,rna", [
    ('AAAACCCGGT', 'ACCGGGTTTT'),
    ('GTCA', 'TGAC')
])
def test_reverse_compliment(dna, rna):
    assert genetools.reverse_compliment(dna) == rna

def test_gc_content():
   assert 100*genetools.gc_content('CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT') == pytest.approx(60.919540, 0.001)

def test_rna_to_protein():
    s1 = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    s2 = 'MAMAPRTEINSTRING*'

    assert genetools.rna_to_protein(s1) == s2

def test_monoisotopic_mass():
    protein = 'SKADYEK'
    mass = 821.392
    assert genetools.monoisotopic_mass(protein, 'protein') == pytest.approx(mass, 0.001)

def test_reverse_palindrome():
    dna = 'ATGCAT'
    assert genetools.reverse_palindrome(dna) is True
