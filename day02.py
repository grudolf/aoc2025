import logging


def part1(lines):
    results = []
    for fr, to in lines:
        print(fr, to)
        for i in range(int(fr), int(to) + 1):
            text = str(i)
            l = len(text)
            if l % 2 == 0:
                if text[0:l // 2] == text[l // 2:]:
                    results.append(text)
                    logging.debug("%s", text)
    return results, sum(map(int, results))


def part2(lines):
    results = []
    for fr, to in lines:
        print(fr, to)
        for i in range(int(fr), int(to) + 1):
            text = str(i)
            s = set()
            for j in range(len(text), 1, -1):
                if len(text) % j == 0:
                    k_len = len(text) // j
                    if all(text[k * k_len:(k + 1) * k_len] == text[0:k_len] for k in range(1, j)):
                        s.add(text)  # set, because 222222 is counted as 2, 4 and 6
                        logging.debug("%s", text)
            results.extend(s)
    return results, sum(map(int, results))


def split_line(line):
    results = []
    for l in line.split(','):
        results.append(l.split('-'))
    return results


def test1():
    line = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    print('Test')
    lines = split_line(line)
    results, total = part1(lines)
    print("Part 1:", total)
    assert results == ['11', '22', '99', '1010', '1188511885', '222222', '446446', '38593859']
    assert total == 1227775554
    results, total = part2(lines)
    print("Part 2:", total)
    assert total == 4174379265


def main():
    with open('data/day02.txt', 'rt') as f:
        line = f.readline()
    lines = split_line(line)
    print('Main')
    _, total = part1(lines)
    print("Part 1:", total)
    _, total = part2(lines)
    print("Part 2:", total)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
