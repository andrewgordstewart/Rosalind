import sys

import rosalind.genetools

if len(sys.argv) > 1 and sys.argv[1] == "test":
    sample_in = input("Please enter the sample input:\n")
    sample_out = input("Please enter the sample output:\n")

    answer = rosalind.genetools.dna_profile(sample_in)

    try:
        assert sample_out == ' '.join(str(num) for num in answer)
    except AssertionError:
        print(sample_out, rosalind.genetools.dna_profile(sample_in))
    else:
        print("Success")
else:
    with open('../input/01.txt', 'r') as f_in:
        dna_string = f_in.read()

        with open('../output/01.txt', 'w+') as f_out:
            for codon in rosalind.genetools.dna_profile(dna_string):
                f_out.write(str(codon))
                f_out.write(' ')
