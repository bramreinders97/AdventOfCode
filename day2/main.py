from Solver import Solver
from inputs import test_input, main_inupt


def solve(org_input: str):
    solver = Solver(org_input)

    print(f"The answer to part 1 is {solver.part_1()}")
    print(f"The answer to part 2 is {solver.part_2()}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve(main_inupt)
