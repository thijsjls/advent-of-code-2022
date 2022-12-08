# Day 8
from pathlib import Path
import numpy as np


def check_visibility(t: np.array, v: np.array) -> np.array:
    for i, row in enumerate(t):
        max_tree = row.max()
        for j in range(len(row)):
            window = row[:j]
            if window.max(initial=-1) == max_tree: break
            if row[j] > window.max(initial=-1): v[i, j] = 1
        for j in range(len(row), 0, -1):
            window = row[j:]
            if window.max(initial=-1) == max_tree: break
            if row[j - 1] > window.max(initial=-1): v[i, j - 1] = 1
    return v


def scenic_score(ty: int, tx: int, wood: np.array) -> int:
    left, right = view_distance(tx, wood[ty, tx], wood[ty, :])
    up, down = view_distance(ty, wood[ty, tx], wood[:, tx])
    return left * right * up * down


def view_distance(i: int, height: int, row: np.array) -> (int, int):
    left = 0
    for l in [x - 1 for x in range(len(row[:i]), 0, -1)]:
        if row[l] >= height:
            left += 1
            break
        left += 1
    right = 0
    for r in [x for x in range(i + 1, len(row))]:
        if row[r] >= height:
            right += 1
            break
        right += 1
    return left, right


input = Path(__file__).parent.parent.resolve() / "inputs/input8.txt"

with open(input) as f:
    data = f.read()
    trees = np.array([[np.array(d) for d in row] for row in data.split('\n')], dtype=int)
    visible = np.zeros(trees.shape, dtype=int)
    print(f"Part One: {check_visibility(trees.T, check_visibility(trees, visible).T).T.sum()}")
    print(
        f"Part Two: {np.array([np.array([scenic_score(ty, tx, trees) for tx in range(trees.shape[1])]) for ty in range(trees.shape[0])]).max(initial=0)}")
