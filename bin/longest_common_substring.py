from rosalind.iotools import read_complete_fasta as read_fasta
from rosalind.iotools import copy_to_clipboard

with open('../data/rosalind_lcsm.txt', 'r') as fp:
    strings = [c for i, c in read_fasta(fp)]


def longest_common_substring(strings):
    strings = sorted(strings)
    short_string = strings[0]
    other_strings = strings[1:]

    # print 'here'

    l = len(short_string)
    m = ''
    for i in range(0, l):
        for j in range(l, i + len(m), -1):
            s1 = short_string[i:j]

            matched_all = True
            # print 'checking %s' % s1
            for s2 in other_strings:
                if s1 not in s2:
                    matched_all = False
                    break

            if matched_all:
                m = s1
                break

    return m


if __name__ == "__main__":

    longest_common_substring = longest_common_substring(strings)
    print longest_common_substring
    copy_to_clipboard(longest_common_substring)
