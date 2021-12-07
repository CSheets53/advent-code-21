import copy

def main():
    f = open("../inputs/d6.txt")
    lines = [line for line in f]
    f.close()

    population = lines[0].split(',')
    population = [int(p) for p in population]

    print(f"Part 1: {part1(population)}")
    print(f"Part 2: {part2(population)}")

def part1(pop):
    """Simulate the number of lanternfish there would be after 80 days"""
    REPRODUCTION_TIME = 7
    NUM_DAYS = 80

    current_pop = copy.copy(pop)
    # Need to use a copy for adding new lanternfish to not mess up for loop
    new_pop = copy.copy(current_pop)

    for _ in range(NUM_DAYS):
        for i in range(len(current_pop)):
            if current_pop[i] == 0:
                current_pop[i] = REPRODUCTION_TIME - 1
                new_pop[i] = REPRODUCTION_TIME - 1
                new_pop.append(REPRODUCTION_TIME + 1)
            else:
                current_pop[i] -= 1
                new_pop[i] -= 1

        current_pop = copy.copy(new_pop)

    return len(current_pop)

def part2(pop):
    """Simulate the number of lanternfish there would be after 256 days"""
    REPRODUCTION_TIME = 7
    NUM_DAYS = 256

    # Make a dict where each key is 0-8 and keep a count of how many fish are in each key
    # Each day, shift the values up one key until 0, where they add onto 7 and also onto 8

    pop_counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in pop:
        pop_counter[fish] += 1

    for d in range(NUM_DAYS):
        new_counter = {}
        for i in range(8):
            new_counter[i] = pop_counter.get(i + 1)

        new_counter[6] += pop_counter.get(0)
        new_counter[8] = pop_counter.get(0)
        pop_counter = new_counter

    return sum(pop_counter.values())

if __name__ == "__main__":
    main()
