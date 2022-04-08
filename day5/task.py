from collections import namedtuple
from typing import List
from utils import print_results

Point = namedtuple('Point', ['x', 'y'])
Segment = namedtuple('Segment', ['p1', 'p2'])


def parse_input() -> List[Segment]:
    input_segments = []
    with open('tmp-data.txt', 'r') as f:
        for line in f.readlines():
            segment_tokens = line.split(' -> ')
            p1_tokens = segment_tokens[0].split(',')
            p2_tokens = segment_tokens[1].split(',')
            p1 = Point(int(p1_tokens[0]), int(p1_tokens[1]))
            p2 = Point(int(p2_tokens[0]), int(p2_tokens[1]))
            input_segments.append(Segment(p1, p2))
    return input_segments


def make_line(segment: Segment) -> List[Point]:
    values = []
    if abs(segment.p1.x - segment.p2.x) == abs(segment.p1.y - segment.p2.y):
        start_l, end_l = segment.p1.x, segment.p2.x
        step_l = -1 if start_l > end_l else 1
        start_r, end_r = segment.p1.y, segment.p2.y
        step_r = -1 if start_r > end_r else 1
        values = list(zip(range(start_l, end_l + step_l, step_l), range(start_r, end_r + step_r, step_r)))
    elif segment.p1.x == segment.p2.x:
        const = segment.p1.x
        start = min(segment.p1.y, segment.p2.y)
        end = max(segment.p1.y, segment.p2.y)
        left = [const] * (abs(start - end) + 1)
        values = list(zip(left, range(start, end + 1)))
    elif segment.p1.y == segment.p2.y:
        const = segment.p1.y
        start = min(segment.p1.x, segment.p2.x)
        end = max(segment.p1.x, segment.p2.x)
        right = [const] * (abs(start - end) + 1)
        values = list(zip(range(start, end + 1), right))
    return list(map(lambda p: Point(*p), values))


def increase_count(points: List[Point], table: dict) -> None:
    for p in points:
        table.setdefault(p.x, {})
        table[p.x].setdefault(p.y, 0)
        table[p.x][p.y] += 1


def count_above_two(table: dict) -> int:
    count = 0
    for x in table.keys():
        for y in table[x]:
            if table[x][y] >= 2:
                count = count + 1
    return count


def part_one() -> int:
    segments = parse_input()
    table = {}
    for segment in segments:
        if segment.p1.x == segment.p2.x or segment.p1.y == segment.p2.y:
            points_covered = make_line(segment)
            increase_count(points_covered, table)
    return count_above_two(table)


def part_two() -> int:
    segments = parse_input()
    table = {}
    for segment in segments:
        points_covered = make_line(segment)
        increase_count(points_covered, table)

    return count_above_two(table)


if __name__ == '__main__':
    print_results(part_one_solve=part_one, part_two_solve=part_two)
