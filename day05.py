import logging


def split_input(lines):
    fresh = []
    available = []
    mode = 0
    for l in lines:
        if l == '':
            mode = 1
            continue
        if mode == 0:
            fresh.append([int(x) for x in l.split('-')])    #F-T
        else:
            available.append(int(l.strip()))    #A
    return fresh, available


def count_fresh(fresh, available):
    cnt = 0
    for i in available:
        if any(i in range(f, t+1) for f,t in fresh):
            cnt += 1
    return cnt


def merge_overlaps(fresh):
    FROM = 0
    TO = 1
    fresh.sort()
    merged = []
    for ing in fresh:
        f, t = ing[FROM], ing[TO]
        if merged and merged[-1][TO] >= f:
            merged[-1][TO] = max(merged[-1][TO], t)
        else:
            merged.append([f, t])
    cnt = 0
    for i in merged:
        cnt += i[TO] - i[FROM] + 1
    return merged, cnt


def test1():
    lines = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".split('\n')
    fresh, available = split_input(lines)
    print('Test')
    cnt = count_fresh(fresh, available)
    print('Part 1:', cnt)
    assert cnt == 3
    merged, cnt2 = merge_overlaps(fresh)
    print('Part 2:', cnt2)
    assert cnt2 == 14


def main():
    with open('data/day05.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    fresh, available = split_input(lines)
    print('Main')
    cnt = count_fresh(fresh, available)
    print('Part 1:', cnt)
    merged, cnt2 = merge_overlaps(fresh)
    print('Part 2:', cnt2)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
