from typing import Callable


def print_results(part_one_solve: Callable[[], int] = None, part_two_solve: Callable[[], int] = None) -> None:
    if part_one_solve:
        part_one_result = part_one_solve()
        print(f'PART 1: {part_one_result}')

    if part_two_solve:
        part_two_result = part_two_solve()
        print(f'PART 2: {part_two_result}')
