from typing import List, Dict
from utils import print_results


def parse_input() -> List[int]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    return [int(x) for x in lines[0].split(',')]


def model(days: int) -> Dict[int, int]:
    state = dict.fromkeys(range(9), 0)
    initial_state = parse_input()
    for day in initial_state:
        state[day] += 1
    for _ in range(days):
        new_kids = 0
        for i in range(9):
            if i == 0:
                new_kids = state[i]
            else:
                state[i - 1] += state[i]
            state[i] = 0
        state[8] += new_kids
        state[6] += new_kids
    return state


def part_one():
    state = model(80)
    return sum(state.values())


def part_two():
    state = model(256)
    return sum(state.values())


if __name__ == '__main__':
    print_results(part_one_solve=part_one, part_two_solve=part_two)
