# from __future__ import print_function
from rosalind.genetools import is_a_substring as _is_a_substring

f = open('../data/rosalind_subs.txt', 'r')

bigstring = f.readline().strip()
substring = f.readline().strip()

locations = []
for i in range(len(bigstring) - len(substring)):
    # print i, _is_a_substring(bigstring, substring, i)
    if _is_a_substring(bigstring, substring, i):
        locations.append(i+1)       # account for different start index

for i in locations:
    print i,
