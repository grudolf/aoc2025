import logging


def part1(lines):
    results = []
    for line in lines:
        values = [int(v) for v in line]
        first = max(values[:-1])
        ind = values.index(first)
        second = max(values[ind + 1:])
        logging.debug("%s %i%i", values, first, second)
        results.append(10 * first + second)
    return results, sum(results)


def part2(lines):
    results = []
    for line in lines:
        values = [int(v) for v in line]
        start = 0
        end = len(values) - 12
        result = ""
        for _ in range(12):
            ix = max(range(start, end + 1), key=lambda x: values[x])
            char = values[ix]
            start = ix + 1
            end += 1
            result += str(char)
        logging.debug("%s %s", values, result)
        results.append(int(result))
    return results, sum(results)


def test1():
    lines = """987654321111111
811111111111119
234234234234278
818181911112111""".split('\n')
    print('Test')
    results, total = part1(lines)
    print("Part 1:", total)
    assert results == [98, 89, 78, 92]
    assert total == 357
    results, total = part2(lines)
    print("Part 2:", total)
    assert total == 3121910778619


def main():
    with open('data/day03.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Main')
    _, total = part1(lines)
    print("Part 1:", total)
    _, total = part2(lines)
    print("Part 2:", total)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
