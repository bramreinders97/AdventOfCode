class SourceToDestMap:
    def __init__(self):
        self.range_maps = []

    def add_range_map(self, map_to_add: dict):
        self.range_maps.append(map_to_add)

    def get_destination(self, source: int) -> int:
        for range_map in self.range_maps:
            if range_map["source_range_start"] <= source < range_map["source_range_end"]:
                return source + range_map["destination_delta"]

        # If no range map is found -> source == destination
        return source
