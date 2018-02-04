import sys

from rosalind.genetools import reverse_compliment
from rosalind.solution import Solution

PROBLEM_PREFIX = "03"


def solve(dna_string):
    return reverse_compliment(dna_string.strip())


if __name__ == "__main__":
    Solution(solve, PROBLEM_PREFIX).solve(test="test" in sys.argv)
