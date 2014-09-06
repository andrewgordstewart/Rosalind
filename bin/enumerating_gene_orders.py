from itertools import permutations

n = 7
p = permutations(range(n), n)

fp = open('../data/permutations.txt', 'w')

count = 0
result = ''
for perm in p:
    subcount = 0
    for i in perm:
        result = result + str(i+1)
        if subcount < n:
            result = result + ' '
    result = result + '\n'
    count += 1

print count
print result

fp.write(str(count) + '\n')
fp.write(result)
