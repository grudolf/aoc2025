import logging
from math import prod


def part1(lines):
    values = [l.split() for l in lines[:-1]]
    operators = lines[-1].split()
    num_cols = len(operators)
    total = 0
    for col in range(num_cols):
        params = [int(v[col]) for v in values]
        if operators[col] == '*':
            result = prod(params)
        elif operators[col] == '+':
            result = sum(params)
        else:
            result = 0
        logging.debug("%s %s = %i", params, operators[col], result)
        total += result
    return total


def part2(lines):
    # go from right to left column
    col = len(lines[0]) - 1
    value_rows = len(lines) - 1
    params = []
    total = 0
    while col >= 0:
        param_str = ''.join(lines[row][col] for row in range(value_rows))
        params.append(int(param_str))
        operator = lines[value_rows][col]
        col -= 1
        if operator == ' ':
            continue
        if operator == '*':
            result = prod(params)
        elif operator == '+':
            result = sum(params)
        else:
            result = 0
        logging.debug("%s %s = %i", params, operator, result)
        total += result
        params.clear()
        col -= 1
    return total

def test1():
    lines = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """.split('\n')
    print('Test')
    result = part1(lines)
    print('Part 1:', result)
    assert result == 4277556
    result = part2(lines)
    print('Part 2:', result)
    assert result == 3263827


def main():
    with open('data/day06.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Main')
    result = part1(lines)
    print('Part 1:', result)
    result = part2(lines)
    print('Part 2:', result)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
