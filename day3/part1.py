import re
from pathlib import Path

number_pattern = re.compile(r"(\d+)")
dot_pattern = re.compile(r"(\.+)")
symbol_pattern = re.compile(r"([^0-9.\n])")


class Symbol:
    def __init__(self, x: int, y: int, value: str) -> None:
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self) -> str:
        return f"({self.x},{self.y}): {self.value}"


class Number:
    def __init__(self, x: int, y: int, value: int, width: int) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.width = width

    def __repr__(self) -> str:
        return f"({self.x},{self.y}): {self.value}"


class Grid:
    def __init__(self) -> None:
        self.points: list[Symbol | Number | None] = []

    def get_symbol(self, x: int, y: int) -> None:
        for point in self.points:
            if point.x == x and point.y == y:
                return point
        return None

    def has_adjacent_symbol(self, number: Number):
        for x in range(number.x - 1, number.x + number.width + 1, 1):
            for y in [number.y - 1, number.y, number.y + 1]:
                if number.x == x and number.y == y:
                    continue
                if self.get_symbol(x=x, y=y):
                    return True
        return False


def sum_part_numbers(text_file: str) -> int:
    input_file = Path(__file__).parent / text_file
    with input_file.open("r") as f:
        lines = f.readlines()

    grid = Grid()

    for y, line in enumerate(lines):
        for number in number_pattern.finditer(line):
            grid.points.append(
                Number(
                    x=number.start(),
                    y=y,
                    value=int(number.group(0)),
                    width=number.end() - number.start(),
                )
            )

        for symbol in symbol_pattern.finditer(line):
            grid.points.append(Symbol(x=symbol.start(), y=y, value=symbol.group(0)))

    sum = 0
    for number in grid.points:
        if isinstance(number, Number) and grid.has_adjacent_symbol(number):
            sum += number.value

    return sum


if __name__ == "__main__":
    assert sum_part_numbers("example_part1.txt") == 4361
    print(sum_part_numbers("input.txt"))
