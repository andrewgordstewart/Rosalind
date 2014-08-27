def mortal_fib(months, lifespan):
    population = [0 for i in range(lifespan)]
    population[0] = 1


    for i in xrange(1, months):
        # print i, population
        temp = sum(population[j] for j in xrange(1, lifespan))
        for j in range(1, lifespan)[::-1]:
            population[j] = population[j-1]
        population[0] = temp

    return population


if __name__ == '__main__':
    import os
    n = sum(i for i in mortal_fib(80, 20))

    cmd = 'echo %s | tr -d "\n" | pbcopy' % str(n)
    os.system(cmd)
