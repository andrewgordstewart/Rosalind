import pytest


from rosalind.mathtools import hamming_distance, weighted_binom
from rosalind import equality


@pytest.mark.parametrize("left,right,distance", [
    ('abcd', 'abdc', 2),
    ('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT', 7)
])
def test_hamming_distance(left, right, distance):
    assert hamming_distance(left, right) == distance


@pytest.mark.parametrize("n,k,p,res", [
    (2, 1, 0.25, .375),
    (5, 3, 0.3, 0.1323)
])
def test_weighted_binom(n, k, p, res):
    assert equality.equals(weighted_binom(n, k, p=p), res)
