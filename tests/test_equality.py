import pytest
from rosalind import equality

@pytest.mark.parametrize("left,right,equals", [
    ('ACGTGC', 'ACGTGC', True),
    ('1', '1', True),
    ('BCA DCB', 'BCA   DCB', True),
    ('BCA\nDCB', 'BCA   \nDCB', True),
    ('1 \n2.03', '1   \n2.03', True),
    ('1 2.0000001', '1   2', True),
])
def test_equals(left, right, equals):
    assert equality.equals(left, right) == equals
