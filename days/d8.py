# Stores frequency sums for each digit -- the sums of the frequencies of letters that appear in each digit's segments
# Keys: sums, values: digit
DIGIT_SUMS = {42: 0, 17: 1, 34: 2, 39: 3, 30: 4, 37: 5, 41: 6, 25: 7, 49: 8, 45: 9}

def main():
    f = open("../inputs/d8.txt")
    lines = [line.rstrip('\n') for line in f]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def part1(lines):
    """Count the number of times digits 1, 4, 7, or 8 appear in the output values"""
    valid_segment_lengths = {2, 3, 4, 7}
    count = 0
    for line in lines:
        output = line.split('|')[1]
        for segments in output.split():
            if len(segments) in valid_segment_lengths:
                count += 1

    return count

def calc_output(line):
    spl = line.split('|')
    input_patterns = spl[0].split()
    output_patterns = spl[1].split()

    # Determine letter frequencies to use for segments
    letter_frequencies = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for seq in input_patterns:
        for c in seq:
            letter_frequencies[c] += 1

    digits = ''
    for seq in output_patterns:
        seq_sum = 0
        for c in seq:
            seq_sum += letter_frequencies.get(c)

        digits += str(DIGIT_SUMS.get(seq_sum))

    return int(digits)

def part2(lines):
    """Determine the wiring configurations, use them to decode the output values, and sum them all"""
    count = 0
    for line in lines:
        count += calc_output(line)

    return count

if __name__ == "__main__":
    main()
