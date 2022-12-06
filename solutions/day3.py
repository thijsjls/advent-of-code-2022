# Day 3
with open('inputs/input3.txt') as f:
    rucksacks = f.read().split('\n')
    doubles = [list(set(r[:len(r)//2]).intersection(r[len(r)//2:])) for r in rucksacks]
    badges = [list(set(rucksacks[i-2]) & set(rucksacks[i-1]) & set(rucksacks[i])) for i, r in enumerate(rucksacks) if i%3==2]
    print(f"Part One: {sum([ord(d[0])-38 if d[0].isupper() else ord(d[0])-96 for d in doubles])}")
    print(f"Part Two: {sum([ord(b[0])-38 if b[0].isupper() else ord(b[0])-96 for b in badges])}")