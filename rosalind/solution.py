import sys
from importlib import import_module
from time import time


class Solution():
    def __init__(self, solve, problem_prefix):
        self._solve = solve
        self.problem_prefix = problem_prefix

    def solve(self, test=False):
        if test:
            sample_in = input("Please enter sample input\n")
            sample_out = input("Please enter sample output\n")

            solution = self._solve(sample_in)
            try:
                assert sample_out == solution
            except AssertionError:
                print("Failure: ", sample_out, solution)
            else:
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


if __name__ == "__main__":
    solution_module_name = sys.argv[1]
    solution_module = import_module(f'solutions.{solution_module_name}')
    PROBLEM_PREFIX = solution_module_name[0:2]

    Solution(solution_module.solve, PROBLEM_PREFIX).solve(test="test" in sys.argv)
