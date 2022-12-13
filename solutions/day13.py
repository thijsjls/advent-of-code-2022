# Day 13

from pathlib import Path


def compare(left: list | int, right: list | int, verbose=False) -> int:
    if verbose: print(f"- Compare {left} vs {right}")
    # If Both integers return and left < right 1
    if isinstance(left, int) and isinstance(right, int):
        return (left < right) - (left > right)
    # Else if only left is int, turn it into list and recurse
    elif isinstance(left, int):
        return compare([left], right, verbose=verbose)
    # Other way around
    elif isinstance(right, int):
        return compare(left, [right], verbose=verbose)
    # If either is empty use lenght as int
    elif not left or not right:
        return compare(len(left), len(right), verbose=verbose)
    # If both are lists compare first element
    else:
        return compare(left[0], right[0], verbose=verbose) or compare(left[1:], right[1:], verbose=verbose)


def pack_sort(packets: list) -> list:
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in range(len(packets)):
            if i + 1 < len(packets):
                if compare(packets[i], packets[i+1]) != 1:
                    sorted_ = False
                    packets[i], packets[i+1] = packets[i+1], packets[i]
    return packets


def part_one(file) -> int:
    with open(file) as f:
        result = 0
        verbose = False
        for i, pair in enumerate(f.read().split('\n\n')):
            if verbose: print(f"== Pair {i+1} ==")
            left, right = pair.split('\n')
            if compare(eval(left), eval(right)) == 1:
                result += i+1
    return result


def part_two(file) -> int:
    with open(file) as f:
        dividers = [[[2]], [[6]]]
        packets = [eval(line) for line in f.readlines() if line != '\n'] + dividers
        packets = pack_sort(packets)
    return (packets.index(dividers[0])+1)*(packets.index(dividers[1])+1)


def main():
    input_ = Path(__file__).parent.parent.resolve() / 'inputs/input13.txt'
    print(f"Part One: {part_one(input_)}")
    print(f"Part Two: {part_two(input_)}")


if __name__ == "__main__":
    main()
