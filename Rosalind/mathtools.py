from math import factorial


def generalized_fib(n, k):
    a, b = 0, 1
    counter = 0
    while counter < n-1:    # need to subtract one since the initialization
                            # ate up a generation
        a, b = b, k*a + b
        counter += 1

    return b


def hamming_distance(seq1, seq2):
    assert len(seq1) == len(seq2)

    max_length = max(len(seq1), len(seq2))
    dist = 0

    for i in range(max_length):
        if seq1[i] == seq2[i]:
            dist += 1

    return max_length - dist


def weighted_binom(n, k):
    if not n > 0 or not k >= 0:
        raise ValueError
    binom = factorial(n) / (factorial(k) * factorial(n-k))
    weight = (.25**k) * (.75**(n-k))
    return binom * weight


if __name__ == '__main__':
    print(hamming_distance('abcd', 'abdc'))
    print(hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))
