from rosalind.mathtools import hamming_distance

f = open('../data/rosalind_hamm.txt', 'r')

a = f.readline().rstrip()
b = f.readline().rstrip()

print hamming_distance(a, b)
