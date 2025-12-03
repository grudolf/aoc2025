import logging


def part1(lines):
    position = 50
    zero_cnt = 0
    for line in lines:
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            position -= distance
        else:
            position += distance
        position = position % 100
        if position == 0:
            zero_cnt += 1
    return zero_cnt


def part2(lines):
    position = 50
    zero_click = 0
    for line in lines:
        prev = position
        direction, distance = line[0], int(line[1:])

        zero_click += (distance // 100)
        distance = distance % 100

        if direction == 'L':
            if position != 0 and position - distance < 0:
                zero_click += 1
            position -= distance
            if position < 0:
                position += 100
        else:
            position += distance
            if position > 100:
                position -= 100
                zero_click += 1
        if position == 0 or position == 100:
            zero_click += 1
        position = position % 100
        print(prev, direction, distance, position, zero_click)
    return zero_click


def test1():
    lines = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".split('\n')
    print('Test')
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


def main():
    with open('data/day01.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Main')
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))
    # not 6355 - too low
    # not 6917 - too high


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
