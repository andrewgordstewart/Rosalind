import pytest
from rosalind import genetools


@pytest.mark.parametrize("sequence,sequence_type,valid", [
    ('ACGTGC', 'dna', True),
    ('ACGUUGUC', 'rna', True),
    ('MKNKFKTQEELVNHLKTVGFVFANSEIYNGLANAWDYGPLGVLLKNNLKNLWWKEFVTKQKDVVGLDSAIILNPLVWKASGHLDNFSDPLIDCKNCKARYRADKLIESFDENIHIAENSSNEEFAKVLNDYEISCPTCKQFNWTEIRHFNLMFKTYQGVIEDAKNVVYLRPETAQGIFVNFKNVQRSMRLHLPFGIAQIGKSFRNEITPGNFIFRTREFEQMEIEFFLKEESAYDIFDKYLNQIENWLVSACGLSLNNLRKHEHPKEELSHYSKKTIDFEYNFLHGFSELYGIAYRTNYDLSVHMNLSKKDLTYFDEQTKEKYVPHVIEPSVGVERLLYAILTEATFIEKLENDDERILMDLKYDLAPYKIAVMPLVNKLKDKAEEIYGKILDLNISATFDNSGSIGKRYRRQDAIGTIYCLTIDFDSLDDQQDPSFTIRERNSMAQKRIKLSELPLYLNQKAHEDFQRQCQK', 'protein', True)
])
def test_validate_sequence_when_valid(sequence, sequence_type, valid):
    assert genetools.validate_sequence(sequence, sequence_type) == valid


@pytest.mark.parametrize("sequence,sequence_type", [
    ('ABCD', 'dna'),
    ('ACGRB', 'rna'),
    ('ABC', 'protein'),
    ('ACGBTGC', 'dna')
])
def test_validate_sequence_when_invalid(sequence, sequence_type):
    with pytest.raises(ValueError):
        genetools.validate_sequence(sequence, sequence_type)


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
    dna_sequence = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
    assert 100*genetools.gc_content(dna_sequence) == pytest.approx(60.919540, 0.001)


@pytest.mark.parametrize("rna,protein", [
    ('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA', 'MAMAPRTEINSTRING*'),
    ('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAAUGGCC', 'MAMAPRTEINSTRING*MA'),
])
def test_rna_to_protein(rna, protein):
    assert genetools.rna_to_protein(rna) == protein


def test_monoisotopic_mass():
    protein = 'SKADYEK'
    mass = 821.392
    assert genetools.monoisotopic_mass(protein, 'protein') == pytest.approx(mass, 0.001)


def test_reverse_palindrome():
    dna = 'ATGCAT'
    assert genetools.reverse_palindrome(dna) is True
