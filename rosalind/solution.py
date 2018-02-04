from time import time


class Solution():
    def __init__(self, solve, problem_prefix):
        self._solve = solve
        self.problem_prefix = problem_prefix

    def solve(self, test=False):
        if test:
            sample_in = input("Please enter sample input\n")
            sample_out = input("Please enter sample output\n")

            assert sample_out == self._solve(sample_in)
            print("Success")
        else:
            with open(f"./data/input/{self.problem_prefix}.txt") as f_in:
                dataset_in = f_in.read()
            output_filename = f"./data/output/{self.problem_prefix}.txt"
            with open(output_filename, "w+") as f_out:
                t1 = time()
                solution = self._solve(dataset_in)
                t2 = time()

                f_out.write(solution)

            secs = t2 - t1
            print(f"Solved in {secs} seconds")
