# id lcsm

from rosalind.iotools import read_complete_fasta as read_fasta
fasta = read_fasta(open('../data/rosalind_lcsm.txt', 'r'))
# print fasta[0][1]
li = []
for i in range(len(fasta)):
    li.append(fasta[i][1])

from suffix_tree import GeneralisedSuffixTree


stree = GeneralisedSuffixTree(li)

max_len = 0
for shared in stree.sharedSubstrings():
    for seq, start, stop in shared:
        if max_len < stop - start:
            max_len = stop - start
            # max_substr = fasta[seq][1][start:stop]
            max_substr = li[seq][start:stop]

print max_substr
