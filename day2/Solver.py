from Game import Game
from available_blocks import available_blocks


class Solver:
    def __init__(self, raw_input):
        self.input = raw_input.splitlines()

    def part_1(self) -> int:

        sum_possible_game_ids = 0

        for line in self.input:
            game = Game(line)

            game_max_colors = game.get_max_colors()

            if game_max_colors["red"] <= available_blocks["red"] and \
               game_max_colors["blue"] <= available_blocks["blue"] and \
               game_max_colors["green"] <= available_blocks["green"]:

                sum_possible_game_ids += game.get_game_id()

        return sum_possible_game_ids

    def part_2(self) -> int:
        sum_powers = 0

        for line in self.input:
            game = Game(line)
            sum_powers += game.get_power()

        return sum_powers



