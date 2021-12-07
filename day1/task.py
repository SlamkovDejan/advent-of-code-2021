from typing import List
from utils import print_results


def parse_input() -> List[int]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = [int(x) for x in f.readlines()]
    return lines


def count_increases(measurements: List[int]) -> int:
    return sum([1 for i in range(1, len(measurements)) if measurements[i] > measurements[i - 1]])


def part_one() -> int:
    measurements = parse_input()
    return count_increases(measurements)


def part_two() -> int:
    measurements = parse_input()
    measurements_transformed = [
        sum([measurements[i], measurements[i + 1], measurements[i + 2]]) for i in range(0, len(measurements) - 2)
    ]
    return count_increases(measurements_transformed)


if __name__ == '__main__':
    print_results(part_one, part_two)
