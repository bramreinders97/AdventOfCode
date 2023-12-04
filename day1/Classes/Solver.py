from typing import List
from .Line import Line


def split_lines(raw_input: str) -> List[str]:
    return raw_input.splitlines()


class Solver:
    def __init__(self, raw_input):
        self.raw_input = raw_input

    def solve(self, part_1: bool) -> int:
        list_of_lines = split_lines(self.raw_input)

        result = 0
        for line in list_of_lines:
            line_instance = Line(line)
            result += int(line_instance.get_number(part_1=part_1))

        return result

