import logging

def count_neighbors(arr, x, y):
    h = len(arr)
    w = len(arr[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if x + i < 0 or x + i >= w or y + j < 0 or y + j >= h:
                continue
            if arr[y + j][x + i] == '@' or arr[y + j][x + i] == 'x':
                count += 1
    return count


def display(arr):
    for l in arr:
        print(''.join(l))


def clear(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == 'x':
                arr[y][x] = '.' # remove


def part1(arr):
    h = len(arr)
    w = len(arr[0])
    cnt = 0
    for y in range(h):
        for x in range(w):
            if arr[y][x] == '@':
                neighbors = count_neighbors(arr, x, y)
                if neighbors < 4:
                    arr[y][x] = 'x' # mark for removal
                    cnt+=1
    return cnt


def part2(arr):
    total = 0
    steps = 0
    while True:
        removed = part1(arr)
        clear(arr)
        total += removed
        steps += 1
        if removed == 0:
            break
    return total, steps

def to_array(lines):
    return [list(l) for l in lines]

        
def test1():
    lines = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".split('\n')
    print('Test')
    arr = to_array(lines)
    total = part1(arr)
    display(arr)
    print("Part 1:", total)
    assert total == 13

    arr = to_array(lines)
    total, steps = part2(arr)
    display(arr)
    print("Part 2:", total, steps)
    assert total == 43


def main():
    with open('data/day04.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    print('Main')
    arr = to_array(lines)
    total = part1(arr)
    display(arr)
    print("Part 1:", total)

    arr = to_array(lines)
    total, steps = part2(arr)
    display(arr)
    print("Part 2:", total, steps)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
