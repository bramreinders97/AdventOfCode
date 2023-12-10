import re


def get_n_cubes_color(color: str, set_str: str) -> int:
    match = None

    if color == 'red':
        match = re.search(r'(\d+)\s+red', set_str)
    elif color == 'green':
        match = re.search(r'(\d+)\s+green', set_str)
    elif color == 'blue':
        match = re.search(r'(\d+)\s+blue', set_str)

    if match:
        return int(match.group(1))
    else:
        return 0


class Game:

    def __init__(self, raw_line):
        self.splitted = raw_line.split(';')
        self.max_red = 0
        self.max_blue = 0
        self.max_green = 0

        self.calc_max_colors()

    def get_game_id(self) -> int:
        # Use re.findall to find all matches in the text
        return int(re.findall(r"Game (\d+):", self.splitted[0])[0])

    def calc_max_colors(self):
        for set_str in self.splitted:
            n_red = get_n_cubes_color("red", set_str)
            n_blue = get_n_cubes_color("blue", set_str)
            n_green = get_n_cubes_color("green", set_str)

            self.max_red = max(self.max_red, n_red)
            self.max_blue = max(self.max_blue, n_blue)
            self.max_green = max(self.max_green, n_green)

    def get_max_colors(self) -> dict:
        return {
            "red": self.max_red,
            "blue": self.max_blue,
            "green": self.max_green
        }

    def get_power(self) -> int:
        return self.max_red * self.max_blue * self.max_green
