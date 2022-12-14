# Day 14

from pathlib import Path
import numpy as np


def connect_nd(ends: np.array) -> np.array:
    d = np.diff(ends, axis=0)[0]
    j = np.argmax(np.abs(d))
    D = d[j]
    aD = np.abs(D)
    return ends[0] + (np.outer(np.arange(aD + 1), d) + (aD//2)) // aD


def parse_rocks(file, mode=1) -> np.array:
    rocks = []
    min_xy = [1000,1000]
    max_xy = [0,0]
    for line in file.read().split('\n'):
        coordinates = np.array([(int(item.split(',')[0]), int(item.split(',')[1])) for item in line.split(' -> ')])
        if coordinates[:,0].min() < min_xy[0]: min_xy[0] = coordinates[:,0].min()
        if coordinates[:,0].max() > max_xy[0]: max_xy[0] = coordinates[:,0].max()
        if coordinates[:,1].min() < min_xy[1]: min_xy[1] = coordinates[:,1].min()
        if coordinates[:,1].max() > max_xy[1]: max_xy[1] = coordinates[:,1].max()
        rocks.append(coordinates.tolist())
    if mode == 2:
        min_xy[0]-=200000
        max_xy[0]+=200000
    print(f"Rock dims: max(x,y)={max_xy}, min(x,y)={min_xy}")
    cave = np.zeros((max_xy[1]+1, max_xy[0]-min_xy[0]+1), dtype=int)
    if mode == 2: cave = np.vstack((cave, np.vstack((np.zeros(cave.shape[1]), np.ones(cave.shape[1])))))
    sand_pos = 500-min_xy[0]
    print(f"Cave dims: {cave.shape}, Sand pos: ({sand_pos}, 0)")
    for rock in rocks:
        for i, coo in enumerate(rock):
            if i+1 < len(rock):
                nxt_coo = np.array(rock[i+1])
                coo = np.array(coo)
                for x, y in connect_nd(np.vstack((coo, nxt_coo))).tolist():
                    cave[y, x-min_xy[0]] = 1
    return cave, [0,sand_pos]


def print_cave(cave: np.array) -> int:
    s = ''
    for row in cave:
        for pixel in row:
            if pixel == 1:
                s+='# '
            elif pixel == 2:
                s+='O '
            else:
                s+='. '
        s+='\n'
    print(s)
    return 0


def step(sand_xy: list, cave: np.array) -> list | int:
    """Step function for sand, returns 1 if sand has come to rest, -1 if sand fell into the abyss,
    otherwise returns the new sand position"""
    y,x = sand_xy
    for coo in [[y+1, x], [y+1, x-1], [y+1, x+1]]:
        if coo[0] >= cave.shape[0] or coo[1] >= cave.shape[1] or coo[1] < 0:
            return -1
        if cave[coo[0],coo[1]] == 0:
            return coo
    return 1


def part_one(file) -> int:
    with open(file) as f:
        cave, sand_start_pos = parse_rocks(f)
        print_cave(cave)
        num_settled = 0
        pos = sand_start_pos
        while True:
            tmp = step(pos, cave)
            if tmp == -1:
                return num_settled
            if tmp == 1:
                num_settled += 1
                cave[pos[0],pos[1]] = 2
                pos = sand_start_pos
                print_cave(cave)
            else:
                pos = tmp


def part_two(file) -> int:
    with open(file) as f:
        cave, sand_start_pos = parse_rocks(f, mode=2)
        num_settled = 0
        pos = sand_start_pos
        while True:
            tmp = step(pos, cave)
            if tmp == 1:
                num_settled += 1
                cave[pos[0],pos[1]] = 2
                if pos == sand_start_pos:
                    return num_settled
                pos = sand_start_pos
            else:
                pos = tmp


def main():
    input_ = Path(__file__).parent.parent.resolve() / "inputs/input14.txt"
    print(f"Part One: {part_one(input_)}")
    print(f"Part Two: {part_two(input_)}")

if __name__ == "__main__":
    main()