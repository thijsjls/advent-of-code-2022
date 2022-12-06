# Day 2
round_to_score_one = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}
round_to_score_two = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}
with open('inputs/input2.txt') as f:
    rounds = f.read().split('\n')
    print(f"Part One: {sum([round_to_score_one[ro] for ro in rounds])}")
    print(f"Part Two: {sum([round_to_score_two[ro] for ro in rounds])}")