import math
import functools
from typing import List
from utils import print_results


def parse_input() -> List[str]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def part_one() -> int:
    params = parse_input()
    num_par, num_digits = len(params), len(params[0])
    gama, epsilon = list(map(lambda x: int(x, 2), functools.reduce(
        lambda x, y: (x[0] + y[0], x[1] + y[1]),  # concat
        [('1', '0') if sum(map(lambda x: int(x[i]), params)) > num_par // 2 else ('0', '1') for i in range(num_digits)],
        ('', '')
    )))
    return gama * epsilon


def part_two() -> int:
    parameters = parse_input()
    current_position = 0
    oxygen_parameters, co2_parameters = parameters[:], parameters[:]
    while True:
        if len(oxygen_parameters) == 1 and len(co2_parameters) == 1:
            break
        if len(oxygen_parameters) != 1:
            keep_digit = 1 if sum(map(lambda x: int(x[current_position]), oxygen_parameters)) >= (
                math.ceil(len(oxygen_parameters) / 2)) else 0
            oxygen_parameters = list(filter(lambda x: int(x[current_position]) == keep_digit, oxygen_parameters))
        if len(co2_parameters) != 1:
            keep_digit = 0 if sum(map(lambda x: int(x[current_position]), co2_parameters)) >= \
                              (math.ceil(len(co2_parameters) / 2)) else 1
            co2_parameters = list(filter(lambda x: int(x[current_position]) == keep_digit, co2_parameters))
        current_position = current_position + 1
    o, co2 = int(oxygen_parameters[0], 2), int(co2_parameters[0], 2)
    return o * co2


if __name__ == '__main__':
    print_results(part_one_solve=part_one, part_two_solve=part_two)
