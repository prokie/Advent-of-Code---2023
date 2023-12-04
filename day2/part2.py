import re
from pathlib import Path

game_pattern = re.compile(r"Game (\d+):")
blue_pattern = re.compile(r"(\d+) blue")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")


class GameSet:
    def __init__(self, set_string: str) -> None:
        self.blue: int = 0
        self.red: int = 0
        self.green: int = 0

        if blue_match := blue_pattern.search(set_string):
            self.blue = int(blue_match.group(1))

        if red_match := red_pattern.search(set_string):
            self.red = int(red_match.group(1))

        if green_match := green_pattern.search(set_string):
            self.green = int(green_match.group(1))


class Game:
    def __init__(
        self, game_string: str, red_cubes: int, blue_cubes: int, green_cubes: int
    ) -> None:
        self.red_cubes = red_cubes
        self.blue_cubes = blue_cubes
        self.green_cubes = green_cubes
        self.id = int(game_pattern.search(game_string).group(1))
        self.game_sets: list[GameSet] = []

        set_strings = game_string.split(":")[-1].strip().split(";")

        for set_string in set_strings:
            self.game_sets.append(GameSet(set_string))

    def is_valid(self) -> bool:
        return all(
            self.red_cubes >= game_set.red
            and self.blue_cubes >= game_set.blue
            and self.green_cubes >= game_set.green
            for game_set in self.game_sets
        )

    def fewest_cubes(self) -> int:
        return (
            max(game_set.red for game_set in self.game_sets)
            * max(game_set.blue for game_set in self.game_sets)
            * max(game_set.green for game_set in self.game_sets)
        )


if __name__ == "__main__":
    input_file = Path(__file__).parent / "example_part1.txt"
    with input_file.open("r") as f:
        lines = f.readlines()

    sum_fewest_cubes = 0

    for x in lines:
        game = Game(
            x,
            red_cubes=12,
            blue_cubes=14,
            green_cubes=13,
        )

        sum_fewest_cubes += game.fewest_cubes()

    print(sum_fewest_cubes)

    input_file = Path(__file__).parent / "input.txt"
    with input_file.open("r") as f:
        lines = f.readlines()

    sum_fewest_cubes = 0

    for x in lines:
        game = Game(
            x,
            red_cubes=12,
            blue_cubes=14,
            green_cubes=13,
        )

        sum_fewest_cubes += game.fewest_cubes()

    print(sum_fewest_cubes)
