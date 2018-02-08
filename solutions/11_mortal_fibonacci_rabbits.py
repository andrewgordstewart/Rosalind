from collections import defaultdict


def solve(dataset):

    months, lifespan = map(int, dataset.split())
    print(months, lifespan)

    return(str(mortal_fib(months, lifespan)))


def mortal_fib(months, lifespan):
    ages = defaultdict(int)
    ages[0] = 1

    i = 1
    while i < months:
        i += 1
        ages = make_babies_and_kill_rabbits(ages, lifespan)

    return(sum(ages.values()))


def make_babies_and_kill_rabbits(ages, lifespan):

    # Take count of number of mature pairs of rabbits
    # of array, indicating a newborn pair of rabbits.
    num_babies = sum(ages[i] for i in range(1, lifespan))

    # Increment each age by 1
    for i in range(lifespan-1, 0, -1):
        ages[i] = ages[i-1]

    ages[0] = num_babies

    return ages
