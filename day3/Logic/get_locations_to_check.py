from typing import List, Tuple
import numpy as np
"""
Logica van welke functie waar staat is ver te zoeken, maar daar heb ik geen 
zin meer in
"""


def get_locations_to_check_around_symbol(row_value: int, col_value: int) -> List[Tuple[int, int]]:
    """
    Given the location of a symbol, return all locations
    around the symbol that need to be checked for Engine
    Parts.
    """
    return [
        (row_value - 1, col_value - 1),
        (row_value - 1, col_value),
        (row_value - 1, col_value + 1),
        (row_value, col_value - 1),
        (row_value, col_value + 1),
        (row_value + 1, col_value - 1),
        (row_value + 1, col_value),
        (row_value + 1, col_value + 1)
    ]


def get_locations_to_check(list_of_lines: List[str], n_rows: int, n_cols: int) -> List[Tuple[int, int]]:
    """
    - loop over lines
    - for each line, call get_locations_to_check_around_symbol for found symbols
    - for the returned locations, add a 1 matrix

    - get all locations where there is a 1, and return these in a list form
    """
    locations_to_check_matrix = np.zeros((n_rows, n_cols))

    for line_number in range(len(list_of_lines)):
        line = list_of_lines[line_number]
        for col_value in range(len(line)):
            char = line[col_value]
            if char != '.' and not char.isdigit():
                locs_to_check = get_locations_to_check_around_symbol(
                    row_value=line_number,
                    col_value=col_value
                )

                for loc in locs_to_check:
                    try:
                        locations_to_check_matrix[loc] = 1
                    except IndexError:
                        continue

    # Find all locations where there is a 1
    non_zero_coordinates = np.where(locations_to_check_matrix == 1)

    # Zip the row and column indices to get the coordinates
    return list(zip(non_zero_coordinates[0], non_zero_coordinates[1]))


def get_gear_ratio(engine_parts: List[dict]):
    """
    check if more than two numbers: if so, return multiplication
    otherwise: return o
    """
    product = 1
    num_parts = 0

    for part in engine_parts:
        if part:
            product *= int(part["number"])
            num_parts += 1

    if num_parts > 1:
        return product
    else:
        return 0


def get_symbol_locations(list_of_lines: List[str]) -> List[Tuple[int, int]]:
    symbol_locs = []

    for line_number in range(len(list_of_lines)):
        line = list_of_lines[line_number]
        for col_value in range(len(line)):
            char = line[col_value]
            if char == '*':
                symbol_locs.append((line_number, col_value))

    return symbol_locs



