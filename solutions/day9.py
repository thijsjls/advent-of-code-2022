# Day 9
from pathlib import Path
from typing import Tuple, List
import numpy as np


def step(x: int) -> int:
    # if -1 <= x <= 1: return 0
    if x == 0: return 0
    s = 1-(x<0)
    if s == 0: s = -1
    return s


def adjacent(H: List[int], T: List[int]) -> bool:
    adj = np.array([[[x,y] for y in range(H[1]-1, H[1]+2)] for x in range(H[0]-1, H[0]+2)])
    adj = adj.reshape(adj.shape[0]*adj.shape[1], 2).tolist()
    return T in adj


def dist(H: List[int], T: List[int]) -> List[int]:
    return list(np.array(H) - np.array(T))


def print_grid(coordinates: List[List[int]], grid_size: Tuple[int], origin=Tuple[int]) -> None:
    grid = np.zeros(grid_size, dtype=str)
    for i, [x,y] in enumerate(coordinates):
        x+=origin[0]
        y+=origin[1]
        if i == 0:
            grid[y,x] = 'H'
        elif grid[y,x] == '':
            grid[y,x] = str(i)
    for row in np.flip(grid, axis=0):
        s = ''
        for element in row:
            if element == '':
                s+='.'
            else:
                s+=element
        print(s)
    print()


def move_head(H: List[int], direction: str, num_moves: int) -> List[int]:
    for x in range(num_moves):
        match direction:
            case 'R':
                H[0] += 1
            case 'L':
                H[0] -= 1
            case 'U':
                H[1] += 1
            case 'D':
                H[1] -= 1
    return H


def move_head_once(H: List[int], direction: str) -> List[int]:
    match direction:
        case 'R':
            H[0] += 1
        case 'L':
            H[0] -= 1
        case 'U':
            H[1] += 1
        case 'D':
            H[1] -= 1
    return H


def move_tail_once(H: List[int], T: List[int]) -> List[int]:
    dx, dy = dist(H, T)
    return [T[0]+step(dx), T[1]+step(dy)]


def move_tail(H: List[int], T: List[int], tail_moves: List[List[int]]) -> Tuple[List[int],List[List[int]]]:
    while not adjacent(H, T):
        T = move_tail_once(H, T)
        if T not in tail_moves: tail_moves.append(T)
    return T, tail_moves


def move(H: List[int], T: List[int], tail_moves: List[List[int]], direction: str, num_moves: int) -> Tuple[List[int],List[int],List[List[int]]]:
    H = move_head(H, direction, num_moves)
    T, tail_moves = move_tail(H, T, tail_moves)
    return H, T, tail_moves


def part_one(data):
    H, T = [0,0], [0,0]
    t_moves = [T]
    for line in data.split('\n'):
        d, nm = line.split()
        H, T, t_moves = move(H, T, t_moves, d, int(nm))
    return len(t_moves)


def part_two(data):
    knots = [[0,0] for x in range(10)]
    t_moves = [[0,0]]
    for k, line in enumerate(data.split('\n')):
        d, nm = line.split()
        for j in range(int(nm)):
            knots[0] = move_head_once(knots[0], d)
            for i, knot in enumerate(knots[1:]):
                i += 1
                if i == 9:
                    knots[i], t_moves = move_tail(knots[i-1], knot, t_moves)
                else:
                    knots[i], _ = move_tail(knots[i-1], knot, [])
    return len(t_moves)


_input = Path(__file__).parent.parent.resolve() /"inputs/input9.txt"

with open(_input) as f:
    data = f.read()[:-1]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")