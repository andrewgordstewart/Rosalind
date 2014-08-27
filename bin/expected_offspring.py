# pop1: genotype pairing AA-AA
# pop2: genotype pairing AA-Aa
# pop3: genotype pairing AA-aa
# pop4: genotype pairing Aa-Aa
# pop5: genotype pairing Aa-aa
# pop6: genotype pairing aa-aa
# capital letters correspond to dominant genotype
def expected_dom_offspring(population):
    return 2*(population[0] + population[1] + population[2]
              + .75*population[3] + .5*population[4]
             )


if __name__ == '__main__':

    # print expected_dom_offspring([1, 0, 0, 1, 0, 1])
    print 'Please input the number of couples of each type.'
    couple_profile = map(int, raw_input("> ").split(" "))

    print expected_dom_offspring(couple_profile)
