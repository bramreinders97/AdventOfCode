from tqdm import tqdm


class Map:
    def __init__(self):
        self.range_dict = []
        # self.map = np.arange(100) # Old
        self.map = {}  # New

    def add_range_map(self, map_to_add: dict):
        self.range_dict.append(map_to_add)

    def fill_specifics(self):
        for range_dict in self.range_dict:
            for i in tqdm(range(range_dict['range_length'])):
                self.map[str(range_dict['source_range_start'] + i)] = \
                    range_dict['destination_range_start'] + i

    def get_full_map(self):
        self.fill_specifics()
        return self.map
