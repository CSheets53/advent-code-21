from collections import defaultdict
from os import dup

def main():
    f = open("../inputs/d12.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    neighbors = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        neighbors[a] += [b]
        neighbors[b] += [a]

    p1 = part1("start", set(), neighbors)
    print(f"Part 1: {p1}")
    p2 = part2("start", set(), neighbors, None)
    print(f"Part 2: {p2}")

# implementation inspired by u/mcpower_ on Reddit
def part1(current, seen, neighbors):
    """Count the number of paths visiting small caves once only"""
    if current == "end":
        return 1

    if current.islower() and current in seen:
        return 0

    seen = seen | {current}
    count = 0
    for n in neighbors[current]:
        count += part1(n, seen, neighbors)

    return count

def part2(current, seen, neighbors, duplicate):
    """Count the number of paths while being able to visit one small cave twice"""
    if current == "end":
        return 1

    if current == "start" and seen:
        return 0

    if current.islower() and current in seen:
        if duplicate is None: # There can only be one cave visited twice
            duplicate = current
        else:
            return 0

    seen = seen | {current}
    count = 0
    for n in neighbors[current]:
        count += part2(n, seen, neighbors, duplicate)

    return count

if __name__ == "__main__":
    main()