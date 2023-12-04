from Logic.split_lines import split_lines
from Logic.get_locations_to_check import get_locations_to_check
from Logic.get_answer_to_sum import get_number_object, get_sum, get_answer_part_2
from Input.input import input


def part_1(org_input: str):

    list_of_lines, n_rows, n_cols = split_lines(org_input)

    locations_to_check_matrix = get_locations_to_check(list_of_lines, n_rows, n_cols)

    found_engine_parts = []

    for loc in locations_to_check_matrix:
        number_obj = get_number_object(list_of_lines[loc[0]], loc[0], loc[1])

        if number_obj and not (number_obj in found_engine_parts):
            found_engine_parts.append(number_obj)

    answer = get_sum(found_engine_parts)

    print(f"The answer to part 1 is {answer}")


def part_2(org_input: str):
    print(f"The answer to part 2 is {get_answer_part_2(org_input.splitlines())}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part_1(input)
    part_2(input)
