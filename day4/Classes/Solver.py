from typing import List
from .Card import Card


def split_raw_into_lines(raw_input: str) -> List[str]:
    return raw_input.splitlines()


def get_list_of_cards(list_of_lines: List[str]) -> List[Card]:
    list_of_cards = []

    for line in list_of_lines:
        card = Card(line)
        card.transform_raw()
        list_of_cards.append(card)

    return list_of_cards


class Solver:

    def __init__(self, raw_input: str):
        self.raw_input = raw_input

    def part_1(self) -> int:
        list_of_lines = split_raw_into_lines(self.raw_input)

        # for each line -> give raw input -> get points
        total_points = 0

        for raw_line in list_of_lines:
            card_instance = Card(raw_line)
            card_instance.transform_raw()
            total_points += card_instance.get_points()

        return total_points

    def part_2(self) -> int:
        list_of_lines = split_raw_into_lines(self.raw_input)

        list_of_cards = get_list_of_cards(list_of_lines)

        n_cards = len(list_of_cards)

        for current_card_index in range(n_cards):
            current_card = list_of_cards[current_card_index]
            n_instances_current_card = current_card.get_n_instances()
            n_duplicates_current_card = current_card.get_num_duplicates()

            # Create range that specifies the indexes of the next cards
            # to create copies for. The min() is included to makes sure
            # we do not try to go out of the list
            start_range = min(n_cards, current_card_index + 1)
            end_range = min(n_cards, current_card_index + n_duplicates_current_card + 1)

            for next_card_index in range(start_range, end_range):
                next_card = list_of_cards[next_card_index]
                next_card.increase_n_instances(n_instances_current_card)

        result = 0

        for card in list_of_cards:
            result += card.get_n_instances()

        return result

