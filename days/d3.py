from copy import deepcopy
import numpy as np
from numpy.core.numeric import ones

def main():
    f = open("../inputs/d3.txt")
    lines = [list(line.rstrip('\n')) for line in f]
    f.close()

    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")

def part1(lines):
    """Calculate the power consumption of the sub by multiplying the gamma and epsilon rates"""
    transp = np.transpose(deepcopy(lines))
    gamma_rate_bin = ''

    for line in transp:
        ones_count = 0
        zeroes_count = 0

        for bit in line:
            if bit == '1':
                ones_count += 1
            else:
                zeroes_count += 1

        gamma_rate_bin += '1' if ones_count > zeroes_count else '0'

    epsilon_rate_bin = ''
    for bit in gamma_rate_bin:
        epsilon_rate_bin += '1' if bit == '0' else '0'

    return (int(gamma_rate_bin, 2) * int(epsilon_rate_bin, 2))

def part2(lines):
    """Calculate the oxygen generator and CO2 scrubber ratings, then multiply them together"""
    # Warning: nasty code ahead 🤮
    current_lines = deepcopy(lines)
    bit_i = 0
    while len(current_lines) > 1:
        transp = np.transpose(deepcopy(current_lines))
        ones_count = 0
        zeroes_count = 0
        for bit in transp[bit_i]:
            if bit == '1':
                ones_count += 1
            else:
                zeroes_count += 1

        comp_bit = '1' if ones_count >= zeroes_count else '0'

        new_lines = []
        for line in current_lines:
            if line[bit_i] == comp_bit:
                new_lines.append(line)

        if len(new_lines) < 1:
            break

        current_lines = new_lines
        bit_i += 1

    o2_rating = ''
    for bit in current_lines[0]:
        o2_rating += bit

    current_lines = deepcopy(lines)
    bit_i = 0
    while len(current_lines) > 1:
        transp = np.transpose(deepcopy(current_lines))
        ones_count = 0
        zeroes_count = 0
        for bit in transp[bit_i]:
            if bit == '1':
                ones_count += 1
            else:
                zeroes_count += 1

        comp_bit = '0' if ones_count >= zeroes_count else '1'

        new_lines = []
        for line in current_lines:
            if line[bit_i] == comp_bit:
                new_lines.append(line)

        if len(new_lines) < 1:
            break

        current_lines = new_lines
        bit_i += 1

    co2_rating = ''
    for bit in current_lines[0]:
        co2_rating += bit

    return int(o2_rating, 2) * int(co2_rating, 2)

if __name__ == "__main__":
    main()
