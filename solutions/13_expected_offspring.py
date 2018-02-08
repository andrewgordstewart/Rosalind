def solve(dataset):
    population = [int(num) for num in dataset.split()]
    NUM_OFFSPRING = 2

    return NUM_OFFSPRING * (
        population[0]        # AA-AA
        + population[1]      # AA-Aa
        + population[2]      # AA-aa
        + .75*population[3]  # Aa-Aa
        + .5*population[4]   # Aa-aa
        + 0*population[5]    # aa-aa
    )
