# Day 15

from pathlib import Path
from typing import List, Tuple
from dataclasses import dataclass
import re
import numpy as np
from tqdm import tqdm


@dataclass
class Sensor:
    position : Tuple[int,int]
    distance : int

    def in_range(self, xy: List[int]) -> bool:
        dx = abs(xy[0] - self.position[0])
        dy = abs(xy[1] - self.position[1])
        return (dx <= self.distance - dy) and (dy <= self.distance - dx)

    def get_outer_corners(self) -> List[List[int]]:
        corners = [
            [self.position[0] + self.distance + 1, self.position[1]],
            [self.position[0], self.position[1] - self.distance - 1],
            [self.position[0] - self.distance - 1, self.position[1]],
            [self.position[0], self.position[1] + self.distance + 1]
        ]
        return corners

    def get_outer_edges(self) -> List[List[int]]:
        corners = self.get_outer_corners()
        edges = []
        edges.extend(connect_nd(np.vstack((np.array(corners[0]), np.array(corners[1])))).tolist())
        edges.extend(connect_nd(np.vstack((np.array(corners[1]), np.array(corners[2])))).tolist())
        edges.extend(connect_nd(np.vstack((np.array(corners[2]), np.array(corners[3])))).tolist())
        edges.extend(connect_nd(np.vstack((np.array(corners[3]), np.array(corners[0])))).tolist())
        return edges


def connect_nd(ends: np.array) -> np.array:
    d = np.diff(ends, axis=0)[0]
    j = np.argmax(np.abs(d))
    D = d[j]
    aD = np.abs(D)
    return ends[0] + (np.outer(np.arange(aD + 1), d) + (aD//2)) // aD


def manhattan(coordinates: List[int]) -> int:
    x0, y0, x1, y1 = coordinates
    return abs(x0-x1) + abs(y0-y1)


def parse_(data: str) -> List[Sensor]:
    sensors = []
    for line in data.split('\n'):
        tmp = [int(x) for x in re.findall(r'-?\d+', line)]
        sensors.append(Sensor(position=(tmp[0], tmp[1]), distance=manhattan(tmp)))
    return sensors


def count_beacons(data: str, line_y: int = 2000000) -> int:
    beacons = 0
    beacons_seen = set()
    for line in data.split('\n'):
        tmp = [int(x) for x in re.findall(r'-?\d+', line)]
        if tmp[3] == line_y and ((tmp[2],tmp[3]) not in beacons_seen):
            beacons += 1
            beacons_seen.add((tmp[2],tmp[3]))
    return beacons


def get_intersects(sensor: Sensor, line_y: int = 2000000) -> List[int]:
    intersects = []
    dy = abs(sensor.position[1] - line_y)
    overlap = max(-1, sensor.distance - dy)
    for i in range(overlap+1):
        intersects.extend([sensor.position[0]-i, sensor.position[0]+i])
    return list(set(intersects))


def part_one(file) -> int:
    total = []
    with open(file) as f:
        data = f.read()
        sensors = parse_(data)
        for sen in sensors:
            tmp = get_intersects(sen)
            total.extend(tmp)
    return len(list(set(total))) - count_beacons(data)


def part_two(file) -> int:
    with open(file) as f:
        data = f.read()
        sensors = parse_(data)
        for sen in sensors:
            print(f"Sensor: {sen.position}, {sen.distance}, edges: {len(sen.get_outer_edges())}")
            candidates = sen.get_outer_edges()
            for point in tqdm(candidates):
                if all([not s.in_range(point) for s in sensors]):
                    return 4000000*point[0] + point[1]
    return -1


def main():
    input_ = Path(__file__).parent.parent.resolve() / 'inputs/input15.txt'
    print(f"Part One: {part_one(input_)}")
    print(f"Part Two: {part_two(input_)}")


if __name__ == "__main__":
    main()