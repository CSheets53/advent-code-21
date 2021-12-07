def main():
    f = open("../inputs/d5.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def map_line(x1, y1, x2, y2, vent_map, map_diagonals=False):
    if x1 == x2:
        row = x1

        lower = 0
        upper = 0
        if y1 < y2:
            lower = y1
            upper = y2
        else:
            lower = y2
            upper = y1

        for col in range(lower, upper + 1):
            vent_map[row][col] += 1
    elif y1 == y2:
        col = y1

        lower = 0
        upper = 0
        if x1 < x2:
            lower = x1
            upper = x2
        else:
            lower = x2
            upper = x1

        for row in range(lower, upper + 1):
            vent_map[row][col] += 1
    else:
        if not map_diagonals:
            return

        row = x1
        col = y1
        while row != x2 and col != y2:
            vent_map[row][col] += 1

            if x1 < x2:
                row += 1
            else:
                row -= 1

            if y1 < y2:
                col += 1
            else:
                col -= 1

        vent_map[row][col] += 1

def count_overlapping_pts(vent_map):
    count = 0
    for row in vent_map:
        for val in row:
            if val > 1:
                count += 1

    return count

def part1(instructions):
    """Using the map of vents, and mapping only horizontally and vertically, find how many points at least two vent lines overlap"""
    vent_map = []
    for _ in range(1000):
        vent_map.append([0] * 1000)

    for instr in instructions:
        instr_split = instr.split('->')
        x1, y1 = instr_split[0].split(',')
        x1 = int(x1)
        y1 = int(y1)

        x2, y2 = instr_split[1].split(',')
        x2 = int(x2)
        y2 = int(y2)

        map_line(x1, y1, x2, y2, vent_map)

    overlap_count = count_overlapping_pts(vent_map)
    return overlap_count

def part2(instructions):
    """Using the map of vents, and mapping horizontally, vertically, and diagonally, find how many points at least two vent lines overlap"""
    vent_map = []
    for _ in range(1000):
        vent_map.append([0] * 1000)

    for instr in instructions:
        instr_split = instr.split('->')
        x1, y1 = instr_split[0].split(',')
        x1 = int(x1)
        y1 = int(y1)

        x2, y2 = instr_split[1].split(',')
        x2 = int(x2)
        y2 = int(y2)

        map_line(x1, y1, x2, y2, vent_map, map_diagonals=True)

    overlap_count = count_overlapping_pts(vent_map)
    return overlap_count

if __name__ == "__main__":
    main()
