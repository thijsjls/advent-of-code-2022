# Day 4
with open('inputs/input4.txt') as f:
    overlap = []
    for line in f.read().split('\n'):
        elf1 = list(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1))
        elf2 = list(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))
        overlap.append((elf1, elf2, list(set(elf1).intersection(elf2))))
    print(f"Part One: {sum([1 for elf1, elf2, o in overlap if o == elf1 or o == elf2 ])}")
    print(f"Part Two: {sum([1 for _, _, o in overlap if o])}")