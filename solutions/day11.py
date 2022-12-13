# Day 11
from pathlib import Path

def parse_monkeys(file):
    monkeys = []
    data = file.read().split('\n\n')
    for monkey in data:
        _, items, operation, test, cond1, cond2 = monkey.split('\n')
        monkeys.append({
            'items' : [int(item) for item in items[18:].replace(',', '').split()],
            'operation' : operation[19:],
            'test' : int(test.split()[-1]),
            'if_true' : int(cond1.split()[-1]),
            'if_false' : int(cond2.split()[-1]),
            'num_inspected' : 0
        })
    return monkeys


def part_one(monkeys, verbose=False):
    for round in range(20):
        if verbose: print(f"\n\n=== ROUND {round+1} ===\n")
        for i, monkey in enumerate(monkeys):
            if verbose: print(f"Monkey {i}:")
            for old in monkey['items']:
                if verbose: print(f"  Monkey inspects an item with a worry level of {old}.")
                monkey['num_inspected'] += 1
                new = eval(monkey['operation'])
                if verbose: print(f"    Worry level is _ by _ to {new}.")
                not_damaged = int(new/3)
                if verbose: print(f"    Monkey gets bored with item. Worry level is divided by 3 to {not_damaged}.")
                test = not_damaged%monkey['test'] == 0
                if verbose: print(f"    Current worry level divisible by {monkey['test']}: {test}")
                if test:
                    next_monkey = monkey['if_true']
                    monkeys[next_monkey]['items'].append(not_damaged)
                else:
                    next_monkey = monkey['if_false']
                    monkeys[next_monkey]['items'].append(not_damaged)
                if verbose: print(f"    Item with worry level {not_damaged} is thrown to monkey {next_monkey}.")
            monkey['items'] = []
    result = [monkey['num_inspected'] for monkey in monkeys]
    return sorted(result)[-1]*sorted(result)[-2]


def get_worry_mod(monkeys):
    all_mods = list(m['test'] for m in monkeys)
    worry_mod = 1
    for m in all_mods:
        worry_mod *= m
    return worry_mod

def part_two(monkeys, verbose=False):
    worry_mod = get_worry_mod(monkeys)
    for round in range(10**4):
        for i, monkey in enumerate(monkeys):
            for old in monkey['items']:
                monkey['num_inspected'] += 1
                new = eval(monkey['operation'])
                new %= worry_mod
                if new%monkey['test'] == 0:
                    monkeys[monkey['if_true']]['items'].append(new)
                else:
                    monkeys[monkey['if_false']]['items'].append(new)
            monkey['items'] = []
        result = [monkey['num_inspected'] for monkey in monkeys]
        if verbose and round%1000==0:
            print(f"\n== After round {round} ==")
            for i, r in enumerate(result):
                print(f"Monkey {i} inpected items {r} times.")
    return sorted(result)[-1]*sorted(result)[-2]


input_ = Path(__file__).parent.parent.resolve() / "inputs/input11.txt"

print(f"Part One: {part_one(parse_monkeys(open(input_)), verbose=False)}")
print(f"Part Two: {part_two(parse_monkeys(open(input_)), verbose=False)}")
