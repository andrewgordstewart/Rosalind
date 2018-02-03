from rosalind.genetools import reverse_compliment

f = open('../data/rosalind_revc.txt', 'r')
s = f.read().rstrip()

print reverse_compliment(s)
