from importlib import import_module
import os
import sys
from time import time

from rosalind.equality import all_equals


class Solution():
    def __init__(self, solve, problem_prefix):
        self._solve = lambda x: str(solve(x))
        self.problem_prefix = problem_prefix

    def solve(self, test=False):
        if test:
            with open(f"./test_data/input/{self.problem_prefix}.txt") as f_in:
                sample_in = f_in.read()
            with open(f"./test_data/output/{self.problem_prefix}.txt") as f_out:
                sample_out = f_out.read()

            solution = self._solve(sample_in)
            try:
                assert all_equals(sample_out, solution)
            except AssertionError:
                print("Failure", sample_out, solution)
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
    solution_number = sys.argv[1]
    solutions = os.listdir('solutions')
    solution_filename = next(s for s in solutions if s.startswith(solution_number))
    solution = solution_filename.replace(".py", "")

    solution_module = import_module(f'solutions.{solution}')

    Solution(solution_module.solve, solution_number).solve(test="test" in sys.argv)
