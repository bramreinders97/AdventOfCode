from typing import List, Tuple


def remove_card_number(line: str) -> str:
    return line.split(':')[1]


def split_numbers_string(number_string: str) -> Tuple[str, str]:
    (winning_numbers_string, own_numbers_string) = number_string.split('|')
    return winning_numbers_string, own_numbers_string


def get_list_from_string(number_string: str) -> List[str]:
    splitted_str = number_string.split(' ')
    empty_strings_removed = [number for number in splitted_str if number != '']
    return empty_strings_removed


class Card:
    def __init__(self, raw_line: str):
        self.raw_line = raw_line
        self.winning_numbers = []
        self.own_numbers = []
        self.n_instances = 1

    def transform_raw(self):
        card_number_removed = remove_card_number(self.raw_line)
        winning_numbers_str, own_numbers_str = split_numbers_string(card_number_removed)
        self.winning_numbers = get_list_from_string(winning_numbers_str)
        self.own_numbers = get_list_from_string(own_numbers_str)

    def get_num_duplicates(self) -> int:
        return len(set(self.winning_numbers).intersection(self.own_numbers))

    def get_points(self) -> int:
        n_duplicates = self.get_num_duplicates()
        return int(min(1, n_duplicates) * 2**(n_duplicates-1))

    def increase_n_instances(self, n_new: int):
        self.n_instances += n_new

    def get_n_instances(self) -> int:
        return self.n_instances
