import logging


def part1(coords):
    max_size = 0
    for i, c1 in enumerate(coords):
        for c2 in coords[i + 1:]:
            size = (1 + abs(c2[0] - c1[0])) * (1 + abs(c2[1] - c1[1]))
            logging.debug("%s %s %i", c1, c2, size)
            max_size = max(max_size, size)
    return max_size


def to_coords(lines):
    return [(x, y) for x, y in (map(int, l.split(',')) for l in lines)]


def test1():
    lines = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3""".split('\n')
    coords = to_coords(lines)
    print('Test')
    result = part1(coords)
    print('Part 1:', result)
    assert result == 50
    # result = part2(coords)
    # print('Part 2:', result)
    # assert result == 25272


def main():
    with open('data/day09.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    coords = to_coords(lines)
    print('Main')
    result = part1(coords)
    print('Part 1:', result)
    # result = part2(coords)
    # print('Part 2:', result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
