import sys

def main():
    f = open("../inputs/d7.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    seq = [int(x) for x in lines[0].split(',')]

    print(f"Part 1: {part1(seq)}")
    print(f"Part 2: {part2(seq)}")

def part1(seq):
    """Find the lowest fuel cost to get the crabs all in the same position"""
    lowest_fuel = sys.maxsize
    for new_pos in range(max(seq) + 1):
        differences = [abs(new_pos - pos) for pos in seq]
        new_fuel_cost = sum(differences)

        if new_fuel_cost < lowest_fuel:
            lowest_fuel = new_fuel_cost

    return lowest_fuel

def part2(seq):
    """Find the lowest fuel cost to get the crabs in the same position, but using triangle sums instead of differences"""
    lowest_fuel = sys.maxsize
    for new_pos in range(max(seq) + 1):
        tri_sums = []
        for pos in seq:
            n = abs(new_pos - pos)
            tri_sums.append((n * (n+1)) // 2)

        new_fuel_cost = sum(tri_sums)

        if new_fuel_cost < lowest_fuel:
            lowest_fuel = new_fuel_cost
        
    return lowest_fuel

if __name__ == "__main__":
    main()
