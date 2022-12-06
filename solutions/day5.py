# Day 5
def parse(input: str) -> (list, list):
    crates, _ = input.split('\n\n')
    stacks = [[char for char in reversed(x) if char.isupper()] for *x, y in zip(*crates.split('\n')) if y.isdigit()]
    moves = [[int(d)-1 for d in line.split() if d.isdigit()] for line in input.split('\n') if line and line[0] == 'm']
    return stacks, moves

def part_one(input: str) -> list:
    stacks, moves = parse(input)
    for mov in moves:
        for n in range(mov[0]+1):
            crate = stacks[mov[1]].pop(-1)
            stacks[mov[2]].append(crate)
    return stacks

def part_two(input: str) -> list:
    stacks, moves = parse(input)
    for mov in moves:
        num_crates = mov[0]+1
        crates = stacks[mov[1]][-num_crates:]
        stacks[mov[2]].extend(crates)
        del stacks[mov[1]][-num_crates:]
    return stacks

with open('inputs/input5.txt') as f:
    input = f.read()
    print(f"Part One: {''.join([s[-1] for s in part_one(input)])}")
    print(f"Part Two: {''.join([s[-1] for s in part_two(input)])}")