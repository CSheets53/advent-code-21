def main():
    f = open("../inputs/d2.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def part1(lines):
    """Calculate the horizontal position and depth, then return their product"""
    depth = 0
    horiz = 0

    for line in lines:
        instr = line.split(' ')
        direction = instr[0]
        amt = int(instr[1])

        if direction == "forward":
            horiz += amt
        elif direction == "down":
            depth += amt
        else:
            depth -= amt

    return depth * horiz

def part2(lines):
    """Calculates the horizontal position and depth, while also tracking aim, and return their product"""
    aim = 0
    depth = 0
    horiz = 0

    for line in lines:
        instr = line.split(' ')
        direction = instr[0]
        amt = int(instr[1])

        if direction == "forward":
            horiz += amt
            depth += (aim * amt)
        elif direction == "down":
            aim += amt
        else:
            aim -= amt

    return horiz * depth

if __name__ == "__main__":
    main()
