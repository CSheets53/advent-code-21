from collections import defaultdict
from copy import deepcopy

def main():
    f = open("../inputs/d14.txt")
    template = None
    rules = {}
    for line in f:
        l = line.rstrip('\n')
        if l:
            if "->" in l:
                pair, letter = l.split(" -> ")
                rules[pair] = letter
            else:
                template = l
    f.close()

    print(f"Part 1: {part1(template, rules, 10)}")
    print(f"Part 2: {part1(template, rules, 40)}")

def part1(template, rules, num_times):
    """Apply num_times steps of insertion and return the difference between the most and least common letters"""
    # Keep track of character counts and pair counts
    counts = defaultdict(lambda: 0)
    pair_counts = {key: 0 for key in rules.keys()}

    # Translate template to pair counts
    for i in range(len(template) - 1):
        counts[template[i]] += 1
        pair = ''.join([template[i], template[i + 1]])
        pair_counts[pair] += 1

    counts[template[len(template) - 1]] += 1

    for i in range(num_times):
        new_pair_counts = deepcopy(pair_counts)
        for key, val in pair_counts.items():
            new_letter = rules[key]
            counts[new_letter] += val

            new_left_pair = f"{key[0]}{new_letter}"
            new_right_pair = f"{new_letter}{key[1]}"

            new_pair_counts[key] -= val
            new_pair_counts[new_left_pair] += val
            new_pair_counts[new_right_pair] += val

        pair_counts = new_pair_counts

    return max(counts.values()) - min(counts.values())

if __name__ == "__main__":
    main()
