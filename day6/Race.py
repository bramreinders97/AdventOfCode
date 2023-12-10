from numpy import roots, array
from math import ceil


class Race:

    def __init__(self, race_length, max_dist_record):
        self.race_length = int(race_length)
        self.max_dist_record = int(max_dist_record)

        self.num_beat_record = 0

    def get_num_beat_record(self) -> int:
        """
        Avoid doing an expensive loop, by looking at the maths of when a
        record is broken.

        The record is broken if:
            record_distance < distance_travelled
            record_distance < button_hold_time * (race_length - button_hold_time)
            -button_hold_time^2 + race_length*button_hold_time - record_distance > 0

        -> Calculate the (rounded) intersections of this quadratic formula, and take the absolute
        value between them to find the number of times we beat the record
        """
        [lower_bound, upper_bound] = roots(array([-1, self.race_length,  -1*self.max_dist_record]))
        return abs(ceil(upper_bound) - ceil(lower_bound))
