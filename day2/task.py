from typing import List
from utils import print_results


def parse_input() -> List[str]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    return lines


def part_one() -> int:
    commands = parse_input()
    horizontal, depth = 0, 0
    for command in commands:
        tokens = command.split(' ')
        direction, unit = tokens[0], int(tokens[1])
        if direction == 'forward':
            horizontal = horizontal + unit
        elif direction == 'up':
            depth = depth - unit
        elif direction == 'down':
            depth = depth + unit
    return horizontal * depth


def part_two() -> int:
    commands = parse_input()
    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        tokens = command.split(' ')
        direction, unit = tokens[0], int(tokens[1])
        if direction == 'forward':
            horizontal = horizontal + unit
            depth = depth + (aim * unit)
        elif direction == 'up':
            aim = aim - unit
        elif direction == 'down':
            aim = aim + unit
    return horizontal * depth


if __name__ == '__main__':
    print_results(part_one, part_two)
