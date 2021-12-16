def main():
    # Get input
    f = open("../inputs/d13.txt")
    coordinates = []
    fold_instructions = []
    for line in f:
        l = line.rstrip('\n')
        if not l:
            continue

        if "fold" not in l:
            new_x, new_y = l.split(',')
            new_x, new_y = int(new_x), int(new_y)
            coordinates.append((new_x, new_y))
        else:
            fold_instructions.append(l)
    f.close()

    # Generate grid
    # Hard code size by using first x fold and first y fold -> value * 2 + 1
    NUM_ROWS = 895
    NUM_COLS = 1311
    original_paper = [['.' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    for coord in coordinates:
        original_paper[coord[1]][coord[0]] = '#'

    print(f"Part 1: {part1(original_paper, fold_instructions[0])}")
    print(f"Part 2:")
    part2(original_paper, fold_instructions)

def count_dots(paper):
    count = 0
    for row in paper:
        for element in row:
            if element == '#':
                count += 1

    return count

def generate_new_paper(paper, num_rows, num_cols):
    new_paper = []
    for i in range(num_rows):
        new_row = []
        for j in range(num_cols):
            new_row.append(paper[i][j])

        new_paper.append(new_row)

    return new_paper

def part1(paper, first_fold):
    """Fold the paper once and count the number of dots"""
    x_fold = True if 'x' in first_fold else False
    value = int(first_fold.split('=')[1])
    new_paper = None

    if x_fold:
        new_paper = generate_new_paper(paper, len(paper), value)

        # populate new paper with left-fold values
        for i in range(len(paper)):
            for j in range(value + 1, len(paper[0])):
                if paper[i][j] == '#':
                    new_paper[i][len(paper[0]) - j - 1] = '#'
    else:
        # y fold
        new_paper = generate_new_paper(paper, value, len(paper[0]))

        # populate new paper with up-fold values
        for i in range(value + 1, len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j] == '#':
                    new_paper[len(paper) - i - 1][j] = '#'

    return count_dots(new_paper)

def part2(paper, instructions):
    """Fold the paper and read the final result in the console"""
    current_paper = paper
    for fold in instructions:
        x_fold = True if 'x' in fold else False
        value = int(fold.split('=')[1])
        new_paper = None

        if x_fold:
            new_paper = generate_new_paper(current_paper, len(current_paper), value)

            # populate new paper with left-fold values
            for i in range(len(current_paper)):
                for j in range(value + 1, len(current_paper[0])):
                    if current_paper[i][j] == '#':
                        new_paper[i][len(current_paper[0]) - 1 - j] = '#'
        else:
            # y fold
            new_paper = generate_new_paper(current_paper, value, len(current_paper[0]))

            # populate new paper with up-fold values
            for i in range(value + 1, len(current_paper)):
                for j in range(len(current_paper[0])):
                    if current_paper[i][j] == '#':
                        new_paper[len(current_paper) - 1 - i][j] = '#'

        current_paper = new_paper

    for row in current_paper:
        print(''.join(row))

if __name__ == "__main__":
    main()
