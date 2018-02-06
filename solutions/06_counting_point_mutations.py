from rosalind.mathtools import hamming_distance


def solve(dataset):
    lines = dataset.split('\n')

    a = lines[0].rstrip()
    b = lines[1].rstrip()

    return str(hamming_distance(a, b))
