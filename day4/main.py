from Classes.Solver import Solver
from Input.inputs import main_input, test_input


def solve(input):
    solver = Solver(input)

    print(f"The answer to part 1 is {solver.part_1()}")

    print(f"The answer to part 2 is {solver.part_2()}")


if __name__ == '__main__':
    solve(main_input)



