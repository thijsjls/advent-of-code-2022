# Day 1
from pathlib import Path

input = Path(__file__).parent.parent.resolve() / "inputs/input.txt"

with open(input) as f:
    elves = [sum(map(int, elf.split('\n'))) for elf in f.read().split('\n\n')]
    print(f"Part One: {max(elves)}")
    print(f"Part Two: {sum(sorted(elves)[-3:])}")