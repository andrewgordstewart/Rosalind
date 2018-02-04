import sys

from rosalind.mathtools import generalized_fib
from rosalind.solution import Solution

PROBLEM_PREFIX = "04"


def solve(dataset):
    months, offspring_factor = [int(datum) for datum in dataset.split(' ')]
    return str(generalized_fib(months, offspring_factor))


if __name__ == "__main__":
    Solution(solve, PROBLEM_PREFIX).solve(test="test" in sys.argv)
