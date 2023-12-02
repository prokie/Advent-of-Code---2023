import re
from collections.abc import Iterable
from pathlib import Path


def main(lines: Iterable[str]) -> int:
    sum = 0
    for line in lines:
        numbers = re.sub(r"\D", "", line)
        sum += int(numbers[0] + numbers[-1])

    return sum


if __name__ == "__main__":
    input_file = Path(__file__).parent / "example_part1.txt"

    # Test example code
    with input_file.open("r") as f:
        lines = f.readlines()

    assert main(lines) == 142

    # Real input

    input_file = Path(__file__).parent / "input.txt"

    with input_file.open("r") as f:
        lines = f.readlines()
    print(main(lines))
