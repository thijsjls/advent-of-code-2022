from pathlib import Path
from typing import Tuple


def part_one(program: list) -> int:
    X = 1
    i = 0
    current_add = [-1, 0]
    signal_strengths = []
    for cycle in range(1, 221):
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle*X)
        if current_add[0] == i:
            X += current_add[1]
            i += 1
        else:
            instruction = program[i].split()
            if instruction[0] == 'addx':
                current_add = [i, int(instruction[1])]
            elif instruction[0] == 'noop':
                i += 1
    return sum(signal_strengths)


def get_pixel(cycle: int, X: int) -> Tuple[int, str]:
    pixel = cycle%40-1
    if pixel in [X-1, X, X+1]:
        return pixel, "#"
    else:
        return pixel, '.'


def part_two(program: list) -> str:
    X = 1
    i = 0
    current_add = [-1, 0]
    line = ""
    cycle = 0
    while True:
        cycle+=1
        pixel, char = get_pixel(cycle, X)
        if pixel == 0:
            print(line)
            line = "#"
        else:
            line += char
        if i >= len(program):
            break
        # print(f"During cycle  {cycle}: CRT prints pixel in position {pixel}")
        # print(f"Current CRT row: {line}")
        if current_add[0] == i:
            X += current_add[1]
            i += 1
        else:
            instruction = program[i].split()
            if instruction[0] == 'addx':
                current_add = [i, int(instruction[1])]
            elif instruction[0] == 'noop':
                i += 1
        # print(f"End of cycle  {cycle}: finish executing {program[i][:-1]} (Register X is now {X})")
        # print(f"Sprite position: {'.'*(X-1)+'###'+'.'*(40-X+1)}\n")
    return "See above"


_input = Path(__file__).parent.parent.resolve() / 'inputs/input10.txt'

with open(_input) as f:
    program = f.readlines()
    print(f"Part One: {part_one(program)}")
    print(f"Part Two: {part_two(program)}")
