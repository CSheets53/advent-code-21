BRACKETS = {'(': ')', '[': ']', '{': '}', '<': '>'}
CORRUPTED_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}

incomplete_lines = []

def main():
    f = open("../inputs/d10.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2()}")

def calc_corrupted_score(line):
    stack = []

    for c in line:
        if c in BRACKETS.keys():
            stack.append(c)
        else:
            left_bracket = stack.pop()
            if c != BRACKETS.get(left_bracket):
                return CORRUPTED_SCORES.get(c)

    return 0

def part1(lines):
    """Find corrupted lines and total up scores for illegal closing brackets"""
    score = 0

    for line in lines:
        corrupted_score = calc_corrupted_score(line)
        score += corrupted_score

        if corrupted_score == 0:
            incomplete_lines.append(line)

    return score

def calc_incomplete_score(line):
    score = 0
    stack = []

    for c in line:
        if c in BRACKETS.keys():
            stack.append(c)
        else:
            left_bracket = stack[-1]
            if c == BRACKETS.get(left_bracket):
                stack.pop()

    # Now we have a stack of unclosed brackets
    while stack:
        left_bracket = stack.pop()
        needed = BRACKETS.get(left_bracket)
        score *= 5
        score += INCOMPLETE_SCORES.get(needed)

    return score

def part2():
    """Find the middle score for incomplete lines"""
    all_scores = []
    for line in incomplete_lines:
        all_scores.append(calc_incomplete_score(line))

    all_scores = sorted(all_scores)
    return all_scores[len(all_scores) // 2]

if __name__ == "__main__":
    main()
