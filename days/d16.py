def main():
    f = open("../inputs/test.txt")
    input_hex = [line.rstrip('\n') for line in f][0]
    packet = bin(int(input_hex, 16))[2:]
    
    print(f"Part 1: {part1(packet)}")
    print(f"Part 2: {part2()}")

def part1(main_packet: str):
    """Parse the main packet and add up the version numbers of all packets"""
    version_numbers = []

    return sum(version_numbers)

def part2():
    pass

if __name__ == "__main__":
    main()
