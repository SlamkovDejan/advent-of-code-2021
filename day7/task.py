import math
from typing import List
from utils import print_results


def parse_input() -> List[int]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    return [int(x) for x in lines[0].split(',')]


def part_one():
    positions = parse_input()
    for p in positions:
        ...


def part_two():
    ...


if __name__ == '__main__':
    ...
