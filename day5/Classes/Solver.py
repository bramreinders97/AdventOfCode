import numpy as np
from .InputReader import InputReader


class Solver:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input

    def part1(self):
        input_reader = InputReader(self.raw_input)
        input_reader.read_input()
        seeds = input_reader.get_seeds()
        maps = input_reader.get_maps()

        locations = np.array([])

        for seed in seeds:

            next_seed = int(seed)
            next_source = next_seed

            for next_map in maps:
                next_source = next_map.get_destination(next_source)

            locations = np.append(locations, next_source)

        return int(min(locations))
