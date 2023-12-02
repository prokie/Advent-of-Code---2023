import re
from collections.abc import Iterable
from enum import Enum
from pathlib import Path


class Numbers(Enum):
    one = "one1one"
    two = "two2two"
    three = "three3three"
    four = "four4four"
    five = "five5five"
    six = "six6six"
    seven = "seven7seven"
    eight = "eight8eight"
    nine = "nine9nine"


def main(lines: Iterable[str]) -> int:
    sum = 0
    for line in lines:
        numbers = line
        for number in Numbers:
            numbers = numbers.replace(number.name, number.value)

        numbers = re.sub(r"\D", "", numbers)
        sum += int(numbers[0] + numbers[-1])

    return sum


if __name__ == "__main__":
    input_file = Path(__file__).parent / "example_part2.txt"

    # Test example code
    with input_file.open("r") as f:
        lines = f.readlines()

    assert main(lines) == 281

    # Real input

    input_file = Path(__file__).parent / "input.txt"

    with input_file.open("r") as f:
        lines = f.readlines()
    print(main(lines))
