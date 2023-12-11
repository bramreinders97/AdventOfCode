import numpy as np
from .InputReader import InputReader
from .Map import SourceToDestMap
from typing import List, Tuple
from math import inf


def find_overlap_and_non_overlap(x, y):
    """
    return:
     - part of x that overlaps with y
     - part(s) of x that do not overlap with y
    """
    start_x, end_x = x
    start_y, end_y = y

    # Check if there is no overlap
    if end_x <= start_y or end_y <= start_x:
        return None, [x]  # No overlap, so x is non-overlapping

    # Calculate the overlapping range
    overlap_start = max(start_x, start_y)
    overlap_end = min(end_x, end_y)

    overlap = (overlap_start, overlap_end)

    # Calculate the non-overlapping parts
    non_overlap_parts = []

    if start_x < overlap_start:
        non_overlap_parts.append((start_x, overlap_start))

    if end_x > overlap_end:
        non_overlap_parts.append((overlap_end, end_x))

    return overlap, non_overlap_parts


class Solver:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input
        self.seeds, self.maps = self.read_input()
        self.seed_ranges = self.get_seed_ranges()

    def get_seed_ranges(self) -> List[Tuple[int, int]]:
        seed_ranges = []
        for i in range(0, len(self.seeds), 2):
            seed_range_start, seed_range_len = self.seeds[i:i + 2]
            seed_ranges.append((int(seed_range_start), int(seed_range_start) + int(seed_range_len) - 1))
        return seed_ranges

    def read_input(self) -> Tuple[List[int], List[SourceToDestMap]]:
        input_reader = InputReader(self.raw_input)
        input_reader.read_input()
        seeds = input_reader.get_seeds()
        maps = input_reader.get_maps()
        return seeds, maps

    def part1(self):
        locations = np.array([])

        for seed in self.seeds:

            next_source = int(seed)

            for next_map in self.maps:
                next_source = next_map.get_destination(next_source)

            locations = np.append(locations, next_source)

        return int(min(locations))

    def part2(self):
        """
        Not written as cleanly as I would like, but at least it works and is fast.
        I've been stuck trying it without recursion for too long, and now i don't
        feel like cleaning up.
        """
        source_ranges_next_map = []

        for source_to_dest_map in self.maps:
            if len(source_ranges_next_map) == 0:
                source_ranges_this_map = self.seed_ranges
            else:
                source_ranges_this_map = source_ranges_next_map
                source_ranges_next_map = []

            map_ranges = source_to_dest_map.get_range_maps()

            def get_destination_ranges(source_range, map_range_index):
                try:
                    map_range = map_ranges[map_range_index]
                    overlap, non_overlap_parts = find_overlap_and_non_overlap(
                        source_range, (map_range["source_range_start"], map_range["source_range_end"] - 1))
                except IndexError:
                    return [source_range]

                to_return = []

                if len(non_overlap_parts) > 0:
                    for non_overlap_part in non_overlap_parts:
                        to_return += get_destination_ranges(non_overlap_part, map_range_index + 1)

                if overlap:
                    to_return += [
                        (overlap[0] + map_range["destination_delta"], overlap[1] + map_range["destination_delta"])]

                return to_return

            for source_range in source_ranges_this_map:
                source_ranges_next_map += get_destination_ranges(source_range, 0)

        min_loc = inf
        for loc_range in source_ranges_next_map:
            min_loc = loc_range[0] if loc_range[0] < min_loc else min_loc

        return min_loc
