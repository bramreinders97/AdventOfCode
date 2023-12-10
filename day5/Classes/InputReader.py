from .Map import SourceToDestMap
from typing import List


class InputReader:
    def __init__(self, raw_input):
        self.input = raw_input.splitlines()
        self.seeds = []
        self.maps = []

    def read_input(self):
        for line in self.input:
            self.read_line(line)

    def read_line(self, line: str):
        if line == '':
            return

        elif '-' in line:
            self.deal_with_map_title(line)

        elif line[0].isdigit():
            self.deal_with_map_numbers(line)

        else:
            self.deal_with_seeds(line)

    def deal_with_map_title(self, line: str):
        self.maps.append(SourceToDestMap())

    def deal_with_seeds(self, line: str):
        self.seeds = line.split(' ')[1:]

    def deal_with_map_numbers(self, line: str):
        [dest_range_start, source_range_start, range_len] = line.split(' ')
        curr_map = self.maps[-1]
        curr_map.add_range_map({
            "source_range_start": int(source_range_start),
            "source_range_end": int(source_range_start) + int(range_len),
            "destination_delta": int(dest_range_start) - int(source_range_start)
        })
        self.maps[-1] = curr_map

    def get_seeds(self) -> List[int]:
        return self.seeds

    def get_maps(self) -> List[SourceToDestMap]:
        return self.maps
