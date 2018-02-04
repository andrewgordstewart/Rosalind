import sys

from rosalind.genetools import dna_profile
from rosalind.solution import Solution

PROBLEM_PREFIX = "01"


def solve(dna_string):
    return ' '.join(str(num) for num in dna_profile(dna_string.strip()))


if __name__ == "__main__":
    Solution(solve, PROBLEM_PREFIX).solve(test="test" in sys.argv)
