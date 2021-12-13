class Octopus:
    def __init__(self, row, col, initial_val):
        self.row = row
        self.col = col
        self.initial_val = initial_val

        self.val = self.initial_val
        self.visited = False
        self.adjacency_matrix = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1), (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

def main():
    f = open("../inputs/d11.txt")
    grid = [list(line.rstrip('\n')) for line in f]
    f.close()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = Octopus(i, j, int(grid[i][j]))

    # print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

def finish_octopi(grid):
    """Reset visited status and reset the energy if needed"""
    flash_count = 0

    for row in grid:
        for octopus in row:
            octopus.visited = False

            if octopus.val > 9:
                octopus.val = 0
                flash_count += 1

    return flash_count

def part1(grid):
    """Calculate the number of total flashes after 100 steps"""
    flash_count = 0

    for _ in range(100):
        flashed_octopi = []

        # Increase energy level of all octopi by 1
        for row in grid:
            for octopus in row:
                octopus.val += 1

                if octopus.val > 9:
                    flashed_octopi.append(octopus)

        # Use bfs for every flashed octopus to increase adjacent octopi energies
        while flashed_octopi:
            current_flashed_octopus = flashed_octopi.pop()
            
            # Skip already visited octopi
            if not current_flashed_octopus.visited:
                current_flashed_octopus.visited = True

                for i, j in current_flashed_octopus.adjacency_matrix:
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                        neighbor_octopus = grid[i][j]
                        neighbor_octopus.val += 1

                        if neighbor_octopus.val > 9:
                            flashed_octopi.append(neighbor_octopus)

        # Reset octopi and count flashes
        flash_count += finish_octopi(grid)

    return flash_count

def part2(grid):
    """Find the first step where all octopi flash"""
    all_flashed = False
    step = 0

    while not all_flashed:
        flashed_octopi = []

        # Increase energy level of all octopi by 1
        for row in grid:
            for octopus in row:
                octopus.val += 1

                if octopus.val > 9:
                    flashed_octopi.append(octopus)

        # Use bfs for every flashed octopus to increase adjacent octopi energies
        while flashed_octopi:
            current_flashed_octopus = flashed_octopi.pop()
            
            # Skip already visited octopi
            if not current_flashed_octopus.visited:
                current_flashed_octopus.visited = True

                for i, j in current_flashed_octopus.adjacency_matrix:
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]):
                        neighbor_octopus = grid[i][j]
                        neighbor_octopus.val += 1

                        if neighbor_octopus.val > 9:
                            flashed_octopi.append(neighbor_octopus)

        # Reset octopi and count flashes
        flash_count = finish_octopi(grid)
        step += 1
        
        if flash_count == 100:
            return step

    return step

if __name__ ==  "__main__":
    main()
