import logging
from math import sqrt, prod


def part1(coords, moves):
    circuits = {c: [c] for c in coords}
    distances = calculate_and_sort_distances(coords)

    eliminated = []
    cnt = 0
    while distances and cnt < moves:
        dist, c1, c2 = distances.pop(0)
        logging.debug("%s %s %s", dist, c1, c2)
        cnt += 1
        if c2 in circuits[c1] or c1 in circuits[c2]:
            continue
        for c in circuits[c2]:
            circuits[c1].append(c)
            eliminated.append(c)
            circuits[c] = circuits[c1]

    # for k, v in circuits.items():
    #     if k not in eliminated:
    #         print(k, v)

    remaining = [v for k, v in circuits.items() if k not in eliminated]
    remaining.sort(key=lambda x: len(x), reverse=True)
    return prod([len(v) for v in remaining[:3]])


def part2(coords):
    circuits = {c: [c] for c in coords}
    distances = calculate_and_sort_distances(coords)

    eliminated = []
    while distances:
        dist, c1, c2 = distances.pop(0)
        logging.debug("%s %s %s", dist, c1, c2)
        if c2 in circuits[c1] or c1 in circuits[c2]:
            continue
        for c in circuits[c2]:
            circuits[c1].append(c)
            eliminated.append(c)
            circuits[c] = circuits[c1]
        if len(circuits[c1]) == len(coords):
            print(f"Single circuit on connection of {c1} and {c2}")
            return c1[0] * c2[0]

    print("No single circuit")
    return 0


def calculate_and_sort_distances(coords) -> list[tuple[float, tuple[int, int, int], tuple[int, int, int]]]:
    # calculate distances between coords, return sorted list of (distance, coord1, coord2) tuples
    distances = []
    for i, c1 in enumerate(coords):
        for c2 in coords[i + 1:]:
            dist = distance(c1, c2)
            distances.append((dist, c1, c2))

    distances.sort()
    return distances


def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def to_coords(lines):
    return [(x, y, z) for x, y, z in (map(int, l.split(',')) for l in lines)]


def display(arr):
    for l in arr:
        print(l)


def test1():
    lines = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689""".split('\n')
    coords = to_coords(lines)
    # display(coords)
    print('Test')
    result = part1(coords, 10)
    print('Part 1:', result)
    assert result == 40
    result = part2(coords)
    print('Part 2:', result)
    assert result == 25272


def main():
    with open('data/day08.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    coords = to_coords(lines)
    print('Main')
    result = part1(coords, 1000)
    print('Part 1:', result)
    result = part2(coords)
    print('Part 2:', result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    test1()
    main()
