def equals(solution1, solution2, tol=0.001):
    """
    Tests equality of all tokens in two solutions.

    Rosalind allows for a default [absolute] error of 0.001 in all decimal
    answers unless otherwise stated.
    """
    tokens1 = solution1.split()
    tokens2 = solution2.split()

    for token1, token2 in zip(tokens1, tokens2):
        try:
            token1 = float(token1)
            token2 = float(token2)
            if abs(token1 - token2) > tol:
                return False
        except ValueError:
            if token1 != token2:
                return False

    return True


if __name__ == "__main__":
    print(equals("1", "  1"))
    print(equals("1", "  1"))
    print(equals("Rosalind_0808\n60.919540", "Rosalind_0808\n60.91954022988506"))
