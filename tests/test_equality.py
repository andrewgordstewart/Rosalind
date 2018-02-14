import pytest
from rosalind import equality


@pytest.mark.parametrize("left,right,equals", [
    ('ACGTGC', 'ACGTGC', True),
    ('1', '1', True),
    ('BCA DCB', 'BCA   DCB', True),
    ('BCA\nDCB', 'BCA   \nDCB', True),
    ('1 \n2.03', '1   \n2.03', True),
    ('1 2.0000001', '1   2', True),
    ("Rosalind_0808\n60.919540", "Rosalind_0808\n60.91954022988506", True),
])
def test_all_equals(left, right, equals):
    assert equality.all_equals(left, right) == equals


@pytest.mark.parametrize("left,right,equals", [
    ('ACGTGC', 'ACGTGC', True),
    ('1', '1', True),
    ('1', '   1', True),
    (1.2, 1.19999999, True),
    (1.2, 1.19, False),
])
def test_equals(left, right, equals):
    assert equality.equals(left, right) == equals
