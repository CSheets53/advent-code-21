from queue import PriorityQueue

def main():
    f = open("../inputs/d15.txt")
    grid = []
    for line in f:
        l = line.rstrip('\n')
        row = []
        for c in l:
            row.append(int(c))
        
        grid.append(row)
    f.close()

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

def part1(grid):
    """Find the lowest-cost path from the top left to the bottom right of the grid"""
    # A* ftw!
    frontier = PriorityQueue()
    start = (0, 0) # row, col
    end = (len(grid) - 1, len(grid[0]) - 1)
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    def _get_neighbors(pos):
        neighbors = []
        row, col = pos[0], pos[1]

        if row > 0:
            neighbors.append((row - 1, col))
        
        if row < len(grid) - 1:
            neighbors.append((row + 1, col))

        if col > 0:
            neighbors.append((row, col - 1))

        if col < len(grid[0]) - 1:
            neighbors.append((row, col + 1))

        return neighbors

    while not frontier.empty():
        current = frontier.get()[1]

        if current == end:
            break

        for next in _get_neighbors(current):
            new_cost = cost_so_far[current] + grid[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current

    return cost_so_far[end]

def part2(original_grid: list[list]):
    """Find the lowest-cost path from the top left to the bottom right of the grid, when expanded 5x5"""
    # Expand the grid
    num_rows_og = len(original_grid)
    num_cols_og = len(original_grid[0])
    
    # Copy over the original grid, and give it a big size
    grid = [[-1 for _ in range(num_cols_og * 5)] for _ in range(num_rows_og * 5)]
    for i in range(num_rows_og):
        for j in range(num_cols_og):
            grid[i][j] = original_grid[i][j]

    # Duplicate to the right
    for i in range(num_rows_og):
        new_row = original_grid[i].copy()
        for count in range(1, 5):
            for j in range(num_cols_og):
                new_num = new_row[j + (num_cols_og * (count - 1))] + 1
                new_row.append(new_num if new_num <= 9 else 1)

        grid[i] = new_row

    # Duplicate down
    for count in range(1, 5):
        for i in range(num_rows_og):
            row_to_check = grid[i + (num_rows_og * (count - 1))].copy()
            new_row = []
            for val in row_to_check:
                new_num = val + 1
                new_row.append(new_num if new_num <= 9 else 1)

            grid[i + (num_rows_og * count)] = new_row
    
    # A* code
    frontier = PriorityQueue()
    start = (0, 0) # row, col
    end = (len(grid) - 1, len(grid[0]) - 1)
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    def _get_neighbors(pos):
        neighbors = []
        row, col = pos[0], pos[1]

        if row > 0:
            neighbors.append((row - 1, col))
        
        if row < len(grid) - 1:
            neighbors.append((row + 1, col))

        if col > 0:
            neighbors.append((row, col - 1))

        if col < len(grid[0]) - 1:
            neighbors.append((row, col + 1))

        return neighbors

    while not frontier.empty():
        current = frontier.get()[1]

        if current == end:
            break

        for next in _get_neighbors(current):
            new_cost = cost_so_far[current] + grid[next[0]][next[1]]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put((new_cost, next))
                came_from[next] = current

    return cost_so_far[end]

if __name__ == "__main__":
    main()
