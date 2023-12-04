from typing import List


def split_lines(str_input: str) -> (List[str], int, int):
    list_of_lines = str_input.splitlines()
    n_rows = len(list_of_lines)
    n_cols = len(list_of_lines[0])

    return list_of_lines, n_rows, n_cols
