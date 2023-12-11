from Classes.Solver import Solver
from Inputs5.inputs import main_input, test_input


def solve(org_input):
    solver = Solver(org_input)

    print(f"The answer to part 1 is: {solver.part1()}")

    print(f"The answer to part 2 is: {solver.part2()}")


if __name__ == '__main__':
    solve(main_input)
