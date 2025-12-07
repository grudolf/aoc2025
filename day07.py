import logging
from functools import cache


def part1(lines):
    # count splits
    w = len(lines[0])
    h = len(lines)
    display(lines)
    hit = 0
    for l in range(0, h - 1):
        for c in range(w):
            if lines[l][c] == 'S':
                lines[l + 1][c] = '|'
            if lines[l][c] == '^':
                if c > 0 and lines[l + 1][c - 1] == '.':
                    lines[l + 1][c - 1] = '|'
                if c < w - 1 and lines[l + 1][c + 1] == '.':
                    lines[l + 1][c + 1] = '|'
            elif lines[l][c] == '|':
                if lines[l + 1][c] == '.':
                    lines[l + 1][c] = '|'
                elif lines[l + 1][c] == '^':
                    hit += 1
    display(lines)
    return hit


def part2(lines):
    # count all possible paths from top to bottom,
    # every split (^) creates a left and right branch
    w = len(lines[0])
    h = len(lines) - 1

    @cache
    def count_paths(pos):
        # logging.debug(f'Counting from position {pos}')
        row, col = pos
        # out of bounds
        if col < 0 or col >= w:
            logging.debug(f'Out of bounds at {pos}')
            return 0
        # reached end
        if row == h:
            logging.debug(f'Reached end at {pos}')
            return 1
        row += 1
        cell = lines[row][col]
        if cell == '.':
            # continue down
            return count_paths((row, col))
        elif cell == '^':
            # split left and right
            # logging.debug(f'Split left and right at {pos}')
            left = count_paths((row, col - 1))
            right = count_paths((row, col + 1))
            return left + right
        else:
            return 0

    start = (0, lines[0].index('S'))
    total_paths = count_paths(start)
    logging.info(count_paths.cache_info())
    return total_paths


def to_array(lines):
    return [list(l) for l in lines]


def display(arr):
    for l in arr:
        print(''.join(l))


def test1():
    lines = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".split('\n')
    inp = to_array(lines)
    print('Test')
    result = part1(inp)
    print('Part 1:', result)
    assert result == 21
    result = part2(lines)
    print('Part 2:', result)
    assert result == 40


def main():
    with open('data/day07.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    inp = to_array(lines)
    print('Main')
    result = part1(inp)
    print('Part 1:', result)
    result = part2(lines)
    print('Part 2:', result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
