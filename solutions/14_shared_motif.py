from rosalind.iotools import read_fasta


def solve(dataset):
    dna_sequences = [fasta[1] for fasta in read_fasta(dataset)]

    s0 = dna_sequences[0]
    s1 = dna_sequences[1]

    left0, left1 = 0, 0

    common_substrings = set()
    for left0 in range(len(s0)):
        for left1 in range(len(s1)):
            i = 0
            while left0 + i < len(s0) and left1 + i < len(s1) and s0[left0 + i] == s1[left1 + i]:
                i += 1
            common_substrings.add(s0[left0:left0 + i])

    common_substrings = list(common_substrings)
    common_substrings.sort(key=lambda s: -len(s))

    for cs in common_substrings:
        for seq in dna_sequences:
            if all(cs in seq for seq in dna_sequences):
                return cs
