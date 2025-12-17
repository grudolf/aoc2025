import logging
import re
from itertools import combinations
from ortools.linear_solver import pywraplp


def part1(all_states, all_buttons):
    total_presses = []
    for state, buttons in zip(all_states, all_buttons):
        desired_state, button_values = convert_to_bits(state, buttons)

        print(state, buttons)
        print(bin(desired_state), [bin(v) for v in button_values])
        found = set()
        for i in range(len(button_values)):
            combs = combinations(button_values, i + 1)
            for c in combs:
                new_state = 0
                for i, v in enumerate(c):
                    new_state = new_state ^ v
                    if new_state == desired_state:
                        used = c[:i+1]
                        if used not in found:
                            found.add(used)
                            print(bin(new_state), "Found with", [bin(vv) for vv in used])
                        break
        if found:
            shortest = min(found, key=len)
            total_presses.append(len(shortest))
    print("Total presses: ", total_presses)
    return sum(total_presses)


def convert_to_bits(state, buttons):
    desired_state = 0
    for s in state:
        desired_state += s
        desired_state *= 2 #shift left
    desired_state //= 2 #one shift too many

    button_values = []
    for button in buttons:
        button_value = 0
        for b in button:
            bit = len(state) - b - 1
            button_value += 2 ** bit
        button_values.append(button_value)
    return desired_state, button_values


def part2(all_buttons, all_joltages):
    total_presses = []
    for buttons, joltage in zip(all_buttons, all_joltages):
        result = solve_part2(buttons, joltage)
        total_presses.append(result)
    print("Total presses: ", total_presses)
    return sum(total_presses)


def solve_part2(buttons, joltage):
    solver = pywraplp.Solver.CreateSolver('SAT')
    logging.info(f'Buttons: {buttons}')
    logging.info(f'Joltage: {joltage}')
    # buttons: [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
    # build variables: how many presses for each of the buttons
    solver_vars = []
    for i in range(len(buttons)):
        v = solver.IntVar(0, solver.infinity(), f'x{i}')
        solver_vars.append(v)
    # joltage: [3, 5, 4, 7]
    # formulas for joltage: sum of button presses increasing joltage == joltage
    # presses for button[4](0, 2) + button[5](0, 1) == joltage[0] -> x4 + x5 = 3
    # presses for button[1](1, 3) + button[5](0, 1) == joltage[1] -> x1 + x5 = 5
    for j in range(len(joltage)):
        expr = sum(solver_vars[i] for i in range(len(buttons)) if j in buttons[i])
        solver.Add(expr == joltage[j])
    solver.Minimize(solver.Sum(solver_vars))
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        logging.info(f'Presses: {[int(v.solution_value()) for v in solver_vars]}')
        logging.info(f'Result : {int(solver.Objective().Value())}')
        return int(solver.Objective().Value())
    else:
        logging.warning('No optimal solution.')
        return 0


def to_input(lines):
    state = []
    buttons = []
    joltage = []
    for line in lines:
        sp = re.findall(r'\[(.*)\] (.*) {(.*)}', line)[0]
        st = [1 if c == '#' else 0 for c in sp[0]]
        b = [list(map(int, b.split(','))) for b in re.findall(r'\((.*?)\)', sp[1])]
        j = [int(i) for i in sp[2].split(',')]
        state.append(st)
        buttons.append(b)
        joltage.append(j)
        logging.debug("%s %s %s", st, b, j)
    return state, buttons, joltage


def test1():
    lines = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}""".split('\n')
    state, buttons, joltage = to_input(lines)
    print('Test')
    result = part1(state, buttons)
    print('Part 1:', result)
    assert result == 7
    result = part2(buttons, joltage)
    print('Part 2:', result)
    assert result == 33


def main():
    with open('data/day10.txt', 'rt') as f:
        lines = [line.rstrip('\n') for line in f]
    state, buttons, joltage = to_input(lines)
    print('Main')
    result = part1(state, buttons)
    print('Part 1:', result)
    result = part2(buttons, joltage)
    print('Part 2:', result)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    test1()
    main()
