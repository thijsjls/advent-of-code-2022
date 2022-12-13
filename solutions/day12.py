# Day 12
from pathlib import Path
import numpy as np
from numpy import ndarray
from typing import Tuple, List


class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position


def parse(input_: str) -> Tuple[ndarray, Tuple[int, int], Tuple[int, int]]:
    startstate = (0, 0)
    goalstate = (0, 0)
    lines = input_.split('\n')
    map_ = np.zeros((len(lines), len(lines[0])), dtype=int)
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            val = ord(char) - 97
            if val == -14:
                startstate = (x, y)
                map_[x, y] = 0
            elif val == -28:
                goalstate = (x, y)
                map_[x, y] = 26
            else:
                map_[x, y] = val
    return map_, startstate, goalstate

def parse_all_a(input_: str) -> Tuple[ndarray, List[Tuple[int, int]], Tuple[int, int]]:
    startstates = []
    goalstate = (0, 0)
    lines = input_.split('\n')
    map_ = np.zeros((len(lines), len(lines[0])), dtype=int)
    for x, line in enumerate(lines):
        for y, char in enumerate(line):
            val = ord(char) - 97
            if val == -14 or val == 0:
                startstates.append((x, y))
                map_[x, y] = 0
            elif val == -28:
                goalstate = (x, y)
                map_[x, y] = 26
            else:
                map_[x, y] = val
    return map_, startstates, goalstate


def get_all_indices(a: np.array) -> list:
    indices = []
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            indices.append((j,i))
    return indices


def get_candidates(heightmap: np.array, state: Tuple[int, int]) -> list:
    result = []
    y, x = state
    max_y, max_x = heightmap.shape
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            if 0 <= i < max_y and 0 <= j < max_x and (i == y or j == x) and (i,j) != (y,x):
                if heightmap[y,x] - heightmap[i,j] <= 1:
                    result.append((i, j))
    return result


def bf_search(heightmap: np.array, startstate: Tuple[int, int], goalstate: Tuple[int, int],  max_depth=1000, verbose=False) -> int:
    startnode = Node(None, startstate)
    queue = [startnode]
    queue_idx =  [startstate]
    depth = 0
    while queue:
        current = queue.pop(0)
        del queue_idx[0]
        if current.position == goalstate:
            path = []
            while current is not None:
                path.append(current.position)
                current = current.parent
            # print(f"DONE: {len(path)}")
            return len(path)
        for candidate in get_candidates(heightmap, current.position):
            child = Node(current, candidate)
            if current.parent:
                if current.parent == child:
                    continue
            if child.position not in queue_idx:
                queue.append(child)
                queue_idx.append(child.position)
    if verbose and depth%100==0:
        print(f"DEPTH {depth}; Current={current.position} NumChildren={len(queue)}")
    if depth > max_depth:
        print("MAX DEPTH REACHED -- ENDING SEARCH")
        return 500
    depth += 1


def part_one(file) -> int:
    with open(file) as f:
        map_, start, goal = parse(f.read())
        return bf_search(map_, goal, start, max_depth=500, verbose=True)


def part_two(file) -> int:
    with open(file) as f:
        map_, starts, goal = parse_all_a(f.read())
        paths = [100]
        for i, s in enumerate(starts):
            # print(f"\nRunning start {i}/{len(starts)} ; start_pos={s}")
            paths.append(bf_search(map_, goal, s, max_depth=min(paths), verbose=False))
        return min(paths)

def main():
    input_ = Path(__file__).parent.parent.resolve() / "inputs/input12.txt"
    print(f"Part One: {part_one(input_)}")
    print(f"Part Two: {part_two(input_)}")


if __name__ == '__main__':
    main()
