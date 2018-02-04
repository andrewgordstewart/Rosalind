from rosalind.mathtools import generalized_fib


def solve(dataset):
    months, offspring_factor = [int(datum) for datum in dataset.split(' ')]
    return str(generalized_fib(months, offspring_factor))
