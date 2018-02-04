import sys
import timeit

import rosalind.genetools


def solve():
    with open('./data/input/01.txt', 'r') as f_in:
        dna_string = f_in.read().strip()

        with open('./data/output/01.txt', 'w+') as f_out:
            for codon in rosalind.genetools.dna_profile(dna_string):
                f_out.write(str(codon))
                f_out.write(' ')


if "test" in sys.argv:
    sample_in = input("Please enter the sample input:\n")
    sample_out = input("Please enter the sample output:\n")

    answer = rosalind.genetools.dna_profile(sample_in)

    try:
        assert sample_out == ' '.join(str(num) for num in answer)
    except AssertionError:
        print(sample_out, answer)
    else:
        print("Success")
else:
    secs = timeit.timeit("solve()",  setup="from __main__ import solve", number=1)
    print(f"Solved in {secs} seconds")
