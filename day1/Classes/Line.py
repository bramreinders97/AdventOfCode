from typing import List
from .DigitChecker import DigitChecker


def get_digit_checkers(left: bool) -> List[DigitChecker]:
    strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    digit_checkers = []

    for i in range(len(strings)):
        string = strings[i]
        number = numbers[i]
        digit_checkers.append(DigitChecker(string, number, left))
        digit_checkers.append(DigitChecker(number, number, left))

    return digit_checkers


class Line:
    def __init__(self, raw_line):
        self.raw_line = raw_line
        self.length = len(raw_line)

    def get_outer_digit_part_1(self, left: bool) -> str:
        for i in range(self.length):
            char = self.raw_line[i if left else self.length - i - 1]
            if char.isdigit():
                return char

    def get_number(self, part_1: bool) -> str:
        if part_1:
            left_digit = self.get_outer_digit_part_1(left=True)
            right_digit = self.get_outer_digit_part_1(left=False)

        else:
            left_digit = self.get_outer_digit_part_2(left=True)
            right_digit = self.get_outer_digit_part_2(left=False)

        return left_digit + right_digit

    def get_outer_digit_part_2(self, left: bool) -> str:
        digit_checkers_list = get_digit_checkers(left)
        for i in range(self.length):
            char = self.raw_line[i if left else self.length - i - 1]

            for digit_checker in digit_checkers_list:
                digit_checker.process_char(char)

                if digit_checker.check_if_digit_is_found():
                    return digit_checker.get_integer_string()
