from typing import List, Tuple
from utils import print_results


def parse_input() -> Tuple[List[List[List[int]]], List[int]]:
    lines = []
    with open('data.txt', 'r') as f:
        lines = f.readlines()

    input_numbers_drawn = [int(x) for x in lines[0].split(',')]
    input_boards, curr_board = [], []
    for line in lines[2:]:
        if line.strip() == '':  # new board
            input_boards.append(curr_board[:])
            curr_board = []
            continue
        curr_board.append([int(x.strip()) for x in line.split(' ') if x.strip() != ''])
    input_boards.append(curr_board)

    return input_boards, input_numbers_drawn


def mark_number(board: List[List[int]], number_drawn: int) -> None:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == number_drawn:
                board[i][j] = -1
                break


def has_bingo(board: List[List[int]]) -> bool:
    return \
        len([row for row in board if sum(row) == -len(row)]) > 0 \
        or \
        len([i for i in range(len(board[0])) if sum([row[i] for row in board]) == -len(board[0])]) > 0


def get_points(winning_board: List[List[int]], last_number_drawn: int) -> int:
    return sum(map(lambda row: sum([x for x in row if x != -1]), winning_board)) * last_number_drawn


def part_one() -> int:
    boards, numbers_drawn = parse_input()
    bingo, points = False, 0
    for number in numbers_drawn:
        for board in boards:
            mark_number(board, number)
            if has_bingo(board):
                points = get_points(board, number)
                bingo = True
                break
        if bingo:
            break

    return points


def part_two() -> int:
    boards, numbers_drawn = parse_input()
    winning_boards, last_board_points = [], 0
    for order, number in enumerate(numbers_drawn):
        if len(boards) == len(winning_boards):
            last_board = boards[winning_boards[-1]]
            last_number = numbers_drawn[order - 1]
            last_board_points = get_points(last_board, last_number)
            break
        for i, board in enumerate(boards):
            if i not in winning_boards:
                mark_number(board, number)
                if has_bingo(board):
                    winning_boards.append(i)

    return last_board_points


if __name__ == '__main__':
    print_results(part_two_solve=part_one, part_one_solve=part_two)
