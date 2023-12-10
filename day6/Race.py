class Race:

    def __init__(self, max_time, max_dist_record):
        self.max_time = int(max_time)
        self.max_dist_record = int(max_dist_record)

        self.num_beat_record = 0

    def calc_num_beat_record(self):
        for speed in range(0, self.max_time + 1):
            dist = speed * (self.max_time - speed)

            if dist > self.max_dist_record:
                self.num_beat_record += 1

    def get_num_beat_record(self) -> int:
        return self.num_beat_record
