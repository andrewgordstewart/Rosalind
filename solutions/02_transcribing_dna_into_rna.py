import sys

from rosalind.genetools import dna_to_rna
from rosalind.solution import Solution

PROBLEM_PREFIX = "02"


def solve(dna_string):
    return dna_to_rna(dna_string.rstrip())


if __name__ == "__main__":
    Solution(solve, PROBLEM_PREFIX).solve(test="test" in sys.argv)
