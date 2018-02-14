def equals(left, right, tol=0.001):
    """
    Tests equality of left and right

    Rosalind allows for a default [absolute] error of 0.001 in decimal
    answers unless otherwise stated.
    """
    try:
        left = left.strip()
        right = right.strip()
    except AttributeError:
        pass

    try:
        left = float(left)
        right = float(right)
        return abs(left - right) <= tol
    except ValueError:
        return left == right


def all_equals(solution1, solution2, tol=0.001):
    """
    Tests equality of all tokens in two solutions.

    Rosalind allows for a default [absolute] error of 0.001 in all decimal
    answers unless otherwise stated.
    """
    tokens1 = solution1.split()
    tokens2 = solution2.split()

    for token1, token2 in zip(tokens1, tokens2):
        if not equals(token1, token2, tol=tol):
            print(token1, token2)
            return False

    return True
