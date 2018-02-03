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

from math import factorial

def weighted_binom(n, k):
    if not n > 0 or not k >= 0:
        print n, k
        raise ValueError
    binom = factorial(n) / (factorial(k) * factorial(n-k))
    weight = (.25**k) * (.75**(n-k))
    return binom * weight

k = 2 # number of generations
N = 1 # desired number of offspring of type {Aa, Bb}
gen = (2**k)


normalizing_constant = sum(weighted_binom(gen, i) for i in xrange(gen+1))
mass_above_N = sum(weighted_binom(gen, i) for i in xrange(N, gen+1))

print mass_above_N*1.0/normalizing_constant
