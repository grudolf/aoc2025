import logging
from functools import cache
from math import prod


def part12(nodes, par_edges, mode=1):
    if "out" not in nodes:
        nodes.append("out")
        par_edges.append(())
    node_dict = {}
    for i, n in enumerate(nodes):
        node_dict[n] = i
    edges = []
    for node_edges in par_edges:
        edges.append([node_dict[n] for n in node_edges])

    logging.debug(node_dict)
    logging.debug(edges)

    @cache
    def dfs(start, end):
        if start == end:
            return 1
        tot = 0
        for nxt in edges[start]:
            tot = tot + dfs(nxt, end)
        return tot

    # part 1
    if mode == 1:
        result = dfs(node_dict["you"], node_dict["out"])
        return result

    # part 2
    # A way
    result_a = [
        dfs(node_dict["svr"], node_dict["fft"]),
        dfs(node_dict["fft"], node_dict["dac"]),
        dfs(node_dict["dac"], node_dict["out"])
    ]
    print("svr -> fft -> dac -> out", result_a, prod(result_a))

    # B way
    result_b = [
        dfs(node_dict["svr"], node_dict["dac"]),
        dfs(node_dict["dac"], node_dict["fft"]),
        dfs(node_dict["fft"], node_dict["out"])
    ]
    print("svr -> dac -> fft -> out", result_b, prod(result_b))
    return prod(result_a) + prod(result_b)


def to_input(lines):
    nodes = []
    edges = []
    for line in lines:
        n, e = line.split(': ')
        nodes.append(n)
        edges.append(tuple(e.split()))
    return nodes, edges


def test1():
    lines = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".split('\n')
    nodes, edges = to_input(lines)
    print('Test')
    print(nodes, edges)
    result = part12(nodes, edges, 1)
    print('Part 1:', result)
    assert result == 5
    lines = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".split('\n')
    nodes, edges = to_input(lines)
    result = part12(nodes, edges, 2)
    print('Part 2:', result)
    assert result == 2


def main():
    with open('data/day11.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    nodes, edges = to_input(lines)
    print('Main')
    result = part12(nodes, edges, 1)
    print('Part 1:', result)
    result = part12(nodes, edges, 2)
    print('Part 2:', result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
