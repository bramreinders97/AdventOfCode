class DigitChecker:
    def __init__(self, actual_string: str, integer_string: str, read_from_left: bool):
        self.actual_string = actual_string
        self.integer_string = integer_string
        self.read_from_left = read_from_left
        self.substring_left = actual_string

    def get_needed_char(self) -> str:
        return self.substring_left[0 if self.read_from_left else -1]

    def update_substring_left(self, success: bool, found_char: str):
        # Need found_char for the edge case that we do not get the expected
        # letter, but instead find the first letter of the word we're looking for
        # (e.g. we need the "w" of "two", but we find "t" -> we only need "wo"
        # now again instead of the entire word "two").
        if success:
            self.substring_left = self.substring_left[1:] if self.read_from_left \
                else self.substring_left[:-1]
        else:
            if found_char == self.actual_string[0 if self.read_from_left else -1]:
                # in given example, we'd change it to "wo"
                self.substring_left = self.actual_string[1:] if self.read_from_left \
                    else self.actual_string[:-1]
            else:
                # in given example we'd change it to "two"
                self.substring_left = self.actual_string

    def process_char(self, found_char: str):
        char_needed = self.get_needed_char()
        right_char_found = (char_needed == found_char)
        self.update_substring_left(success=right_char_found, found_char=found_char)

    def check_if_digit_is_found(self) -> bool:
        return self.substring_left == ''

    def get_integer_string(self) -> str:
        return self.integer_string
