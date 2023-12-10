from typing import List
from Race import Race


def extract_list(raw_str: str) -> List[str]:
    return [num for num in raw_str.split(":")[1].split(' ') if num != '']

def extract_str_from_list(list_of_str: List[str]) -> int:
    final_str = ''

    for str in list_of_str:
        final_str += str

    return int(final_str)


class Solver:

    def __init__(self, raw_input: str):
        [self.times_raw, self.distances_raw] = raw_input.splitlines()

        self.times = extract_list(self.times_raw)
        self.distances = extract_list(self.distances_raw)

    def part_1(self):
        prod_beat_records = 1

        for i in range(len(self.times)):
            race = Race(self.times[i], self.distances[i])

            prod_beat_records = prod_beat_records * race.get_num_beat_record()

        return prod_beat_records

    def part_2(self):
        time = extract_str_from_list(self.times)
        distance = extract_str_from_list(self.distances)

        race = Race(time, distance)
        return race.get_num_beat_record()
