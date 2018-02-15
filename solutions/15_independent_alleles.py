'''
Tom is an animal with two traits corresponding to alleles A and B. He
himself is heterozygous in both traits, that is to say he is of type
{Aa, Bb}. He mates with a black-box mate, of type {Aa, Bb}, as do each
of his descendents. The problem is to determine the probability that
at least N of his ancestors at level k are heterozygous in both traits.

Mende's second law states that the two traits A and B are inhereted
by offspring independently; moreover, ANY organism, whether of type
{Aa}, {AA}, or {aa}, has a 1/2 chance of producing an offspring of
type {Aa} if they reproduce with a heterozygous mate. (Check it!)

Thus, each organism at level k has a 1/2 chance of being type {Aa}.
Since the two traits are independent, each organism at level k is of
type {Aa, Bb} with probability 1/4. So all we really need to do is
a simple combinatorial calculation...
'''
from rosalind.mathtools import weighted_binom


def solve(dataset):
    # k: number of generations
    # N: desired number of offspring of type {Aa, Bb}
    k, N = [int(s) for s in dataset.split(' ')]
    gen = (2**k)

    normalizing_constant = sum(
        weighted_binom(gen, i, p=0.25)
        for i in range(gen+1)
    )

    mass_above_N = sum(
        weighted_binom(gen, i, p=0.25)
        for i in range(N, gen+1)
    )

    return(str(mass_above_N*1.0/normalizing_constant))
