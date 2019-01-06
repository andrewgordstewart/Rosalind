from itertools import zip_longest, islice, chain
import functools


class SuffixArray():
    def __init__(self, strings):
        self.sentinels = dict(
            (i, Sentinel(i))
            for i in range(len(strings))
        )

        self.strings = [
            list(string) + [self.sentinels[i]]
            for i, string in enumerate(strings)
        ]

        self.chained_strings = list(chain.from_iterable(self.strings))

        self.int_keys = to_int_keys(self.chained_strings)

        self.suffix_array = suffix_array(self.chained_strings)
        self.lcp_array = compute_lcp(self.chained_strings, self.suffix_array)

    def shared_substrings(self):
        pass

    def longest_common_substrings(self):
        num_seqs = len(self.strings)
        lcp = self.lcp_array
        suffixes = [
            s[i:]
            for s in self.strings
            for i in range(len(s))
        ]

        sorted_suffixes = sorted(suffixes)
        left, right = num_seqs, num_seqs
        sentinel_counts = dict(
            (s, 0) for s in self.sentinels
        )
        max_w = 0
        max_indexes = []
        finished = False
        while not finished:
            # advance right until the interval of suffixes contains
            # at least one suffix from each substring
            # TODO: optimize clause
            while 0 in sentinel_counts.values():
                if right == len(sorted_suffixes):
                    finished = True
                    break

                suffix = sorted_suffixes[right]
                sentinel_counts[suffix[-1].size] += 1
                right += 1

            if 0 not in sentinel_counts.values():
                # the longest prefix among the (left)-th to (right-1)-th sorted
                # suffixes is the minimum of the longest common prefix.
                w = min(lcp[left:right])

                if w == max_w:
                    max_indexes.append((left, right-1))
                if w > max_w:
                    print("MAXED: ", w)
                    max_w = w
                    max_indexes = [(left, right-1)]

            sentinel_counts[sorted_suffixes[left][-1].size] -= 1
            left += 1

        ans = []
        for left, _ in max_indexes:
            ans.append(''.join(sorted_suffixes[left][:max_w]))
        return ans


@functools.total_ordering
class Sentinel():
    def __init__(self, size):
        if type(size) != int:
            raise ValueError(f"size must be an integer")

        self.size = size

    def __lt__(self, other):
        if type(other) == str:
            return True
        elif type(other) == type(self):
            return self.size < other.size

    def __eq__(self, other):
        return type(other) == Sentinel and self.size == other.size

    def __repr__(self):
        return f'Sentinel<{self.size}>'

    def __hash__(self):
        return hash(repr(self))


def to_int_keys(l):
    """
    l: iterable of keys
    returns: a list with integer keys
    """
    seen = set()
    ls = []
    for e in l:
        if e not in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]


def suffix_array(s):
    """
    suffix array of s
    O(n * log(n)^2)
    """
    n = len(s)
    k = 1
    line = to_int_keys(s)
    while max(line) < n - 1:
        line = to_int_keys(
            [
                a * (n + 1) + b + 1
                for (a, b) in
                zip_longest(line, islice(line, k, None), fillvalue=-1)
            ]
        )
        k <<= 1
    return line


def compute_lcp(s, pos):
    """
    lcp array of s
    expects pos to be the suffix array of s

    lcp[i] = length of longest common prefix between s[i:] and s[j:],
    where j = rank[pos[i] + 1] is the index, in s, of the suffix
    following s[i:] lexicographically

    O(n)
    """
    n = len(s)

    rank = [0]*n
    for i in range(n):
        rank[pos[i]] = i

    h = 0
    lcp = [None]*n
    for i in range(n):
        if pos[i] < n - 1:
            k = rank[pos[i] + 1]

            while s[i+h] == s[k+h]:
                h += 1
            lcp[pos[i]] = h
            if h > 0:
                h -= 1
    return lcp
