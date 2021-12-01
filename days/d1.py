def main():
    f = open('../inputs/d1.txt')
    lines = [int(line) for line in f.readlines()]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def part1(lines):
    increased_count = 0

    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            increased_count += 1

    return increased_count

def part2(lines):
    increased_count = 0

    for i in range(1, len(lines) - 2):
        if sum(lines[i:i+3]) > sum(lines[i-1:i+2]):
            increased_count += 1

    return increased_count

if __name__ == "__main__":
    main()