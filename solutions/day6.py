# Day 6
from pathlib import Path

input = Path(__file__).parent.parent.resolve() / "inputs/input6.txt"

def start_of_packet(input: str) -> int:
    for i, char in enumerate(input[:-3]):
        if len(set(char + input[i+1:i+4])) == 4:
            return i+4

def start_of_message(input: str) -> int:
    for i, char in enumerate(input[:-13]):
        if len(set(char + input[i+1:i+14])) == 14:
            return i+14

with open(input) as f:
    input = f.read()
    print(f"Part One: {start_of_packet(input)}")
    print(f"Part Two: {start_of_message(input)}")