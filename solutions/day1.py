# Day 1
with open('inputs/input.txt') as f:
    elves = [sum(map(int, elf.split('\n'))) for elf in f.read().split('\n\n')]
    print(f"Part One: {max(elves)}")
    print(f"Part Two: {sum(sorted(elves)[-3:])}")