def main():
    f = open("../inputs/test.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    p1_start_pos = int(lines[0].split(": ")[1])
    p2_start_pos = int(lines[1].split(": ")[1])

    print(f"Part 1: {part1(p1_start_pos, p2_start_pos)}")
    print(f"Part 2: {part2(p1_start_pos, p2_start_pos)}")

def part1(p1_start, p2_start):
    p1_score = 0
    p2_score = 0

    DIE = list(range(1, 101))

    current_roll_index = 0
    num_die_rolls = 0
    p1_current_space = p1_start
    p2_current_space = p2_start

    while p1_score < 1000 and p2_score < 1000:
        # Handle p1
        total_roll_amt = 0
        for _ in range(3): # make 3 rolls
            num_die_rolls += 1
            new_roll_val = DIE[current_roll_index]
            total_roll_amt += new_roll_val
            current_roll_index += 1
            if current_roll_index >= len(DIE):
                current_roll_index = 0

        new_big_space = p1_current_space + total_roll_amt
        p1_current_space = int(str(new_big_space)[-1]) # Get the last digit
        if p1_current_space == 0:
            p1_current_space = 10
        p1_score += p1_current_space

        if p1_score >= 1000:
            break

        # Handle p2
        total_roll_amt = 0
        for _ in range(3): # make 3 rolls
            num_die_rolls += 1
            new_roll_val = DIE[current_roll_index]
            total_roll_amt += new_roll_val
            current_roll_index += 1
            if current_roll_index >= len(DIE):
                current_roll_index = 0

        new_big_space = p2_current_space + total_roll_amt
        p2_current_space = int(str(new_big_space)[-1]) # Get the last digit
        if p2_current_space == 0:
            p2_current_space = 10
        p2_score += p2_current_space

    lowest_score = p1_score if p1_score < p2_score else p2_score
    return lowest_score * num_die_rolls

if __name__ == "__main__":
    main()
