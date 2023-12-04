from Classes.Solver import Solver
from Inputs.input import main_input, test_input, test_input_2, test_input_3, input_dion


def solve(input_1, input_2):
    solver1 = Solver(input_1, debug=False)
    solver2 = Solver(input_2, debug=True)

    print(f"The answer to part 1 is {solver1.solve(part_1=True)}")
    print(f"The answer to part 2 is {solver2.solve(part_1=False)}")


if __name__ == '__main__':
    solve(main_input, main_input)
