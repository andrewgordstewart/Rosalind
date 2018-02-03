from rosalind.iotools import read_fasta as _read_fasta
from rosalind.genetools import profile_matrix as _profile_matrix
fasta = []
with open('../data/rosalind_cons.txt', 'r') as fp:
    for name, seq in _read_fasta(fp):
        fasta.append(seq)

# print fasta

profile = _profile_matrix(fasta)

# print profile[0]
consensus = [0 for i in range(len(profile))]
count = 0
for d in profile:
    max = 0
    for key in d:
        if d[key] > max:
            max = d[key]
            consensus[count] = key
    count += 1


def string_sum(li):
    s = ''
    for string in li:
        s = s + string
    return s

print string_sum(consensus)
for key in profile[0]:
    print key + ': ',
    for d in profile:
        print d[key],
    print ''
