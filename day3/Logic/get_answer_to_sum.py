from typing import Tuple, List
from Logic.get_locations_to_check import get_symbol_locations, get_gear_ratio, get_locations_to_check_around_symbol
"""
given a coordinate:
- check left, check right, add together
- create {number: number: line: row_number, start_col: start_col}
"""


def append_digits(line: str, start_digit: str, start_col: int, left: bool) -> Tuple[str, int]:
    # add digits to left or right of start
    check_distance = 1
    number_to_return = start_digit

    while True:
        try:
            col_to_check = start_col + check_distance * (-1 if left else 1)
            char_found = line[col_to_check]
            if char_found.isdigit():
                number_to_return = (char_found + number_to_return) if left else (number_to_return + char_found)
                check_distance += 1
            else:
                return number_to_return, col_to_check

        except IndexError:
            return number_to_return, start_col


def get_number_object(line: str, line_number: int, start_col: int) -> dict or None:
    start_digit = line[start_col]

    # If nothing to find, return
    if not start_digit.isdigit():
        return

    number, left_digit = append_digits(line, start_digit, start_col, True)
    number, _ = append_digits(line, number, start_col, False)

    return {
        "number": number,
        "line": line_number,
        "start_col": min(start_col, left_digit)
    }


def get_sum(list_of_engine_parts: List[dict]) -> int:
    result = 0

    for engine_part in list_of_engine_parts:
        result += int(engine_part["number"])

    return result


def get_answer_part_2(list_of_lines: List[str]):
    """
    for each symbol location
    - get locations to check around symbol: get_locations_to_check_around_symbol
    - get all numbers around: get_number_object for each location from prev step
    - call get_gear_ratio to get the gear ratio of each symbol, add to result var
    """
    symbol_locs = get_symbol_locations(list_of_lines)
    sum_of_ratios = 0

    for symbol_loc in symbol_locs:
        locs_to_check = get_locations_to_check_around_symbol(symbol_loc[0], symbol_loc[1])

        adjacent_engine_parts = []

        for loc_to_check in locs_to_check:
            adjacent_engine_part = get_number_object(list_of_lines[loc_to_check[0]], loc_to_check[0], loc_to_check[1])

            if adjacent_engine_part and adjacent_engine_part not in adjacent_engine_parts:
                adjacent_engine_parts.append(adjacent_engine_part)

        sum_of_ratios += get_gear_ratio(adjacent_engine_parts)

    return sum_of_ratios
