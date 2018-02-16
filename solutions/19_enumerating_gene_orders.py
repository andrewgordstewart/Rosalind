from itertools import permutations


def solve(dataset):
    n = int(dataset.strip())
    perms = permutations(range(n), n)

    perms = [' '.join(str(i+1) for i in perm) for perm in perms]
    return str(len(perms)) + '\n' + '\n'.join(perms)
