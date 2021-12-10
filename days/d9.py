def main():
    f = open("../inputs/d9.txt")
    grid = [list(line.rstrip('\n')) for line in f]
    f.close()

    print(f"Part 1: {part1(grid)}")
    print(f"Part 2: {part2(grid)}")

def part1(grid):
    """Return the sum of the risk levels of the lowest points in the height map"""
    risk_level_low_points = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]

            lower_than_all = True
            if i > 0 and current >= grid[i - 1][j]:
                lower_than_all = False
            if i < len(grid) - 1 and current >= grid[i + 1][j]:
                lower_than_all = False
            if j > 0 and current >= grid[i][j - 1]:
                lower_than_all = False
            if j < len(grid[i]) - 1 and current >= grid[i][j + 1]:
                lower_than_all = False

            if lower_than_all:
                risk_level_low_points.append(int(current) + 1)

    return sum(risk_level_low_points)

# Direction vectors for bfs
dir_row = [-1, 0, 1, 0]
dir_col = [0, 1, 0, -1]

def is_valid(visited, i, j, grid):
    if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[i]) - 1:
        return False

    if visited[i][j] or grid[i][j] == '9':
        return False

    return True

def calculate_basin_size(i, j, grid):
    # Use bfs to explore and count the size of each path until 9 is hit
    # Source: https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/
    visited = [[False for _ in range(len(grid[i]))] for i in range(len(grid))]
    
    queue = [(i, j)]
    visited[i][j] = True
    size = 0

    while len(queue):
        current_i, current_j = queue.pop(0)
        size += 1

        # Check 4 adjacent cells
        for a in range(4):
            adj_i = current_i + dir_row[a]
            adj_j = current_j + dir_col[a]

            if (is_valid(visited, adj_i, adj_j, grid)):
                queue.append((adj_i, adj_j))
                visited[adj_i][adj_j] = True
    
    return size

def part2(grid):
    """Find the three largest basins and multiply their sizes together"""
    basin_sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]

            lower_than_all = True
            if i > 0 and current >= grid[i - 1][j]:
                lower_than_all = False
            if i < len(grid) - 1 and current >= grid[i + 1][j]:
                lower_than_all = False
            if j > 0 and current >= grid[i][j - 1]:
                lower_than_all = False
            if j < len(grid[i]) - 1 and current >= grid[i][j + 1]:
                lower_than_all = False

            if lower_than_all:
                basin_sizes.append(calculate_basin_size(i, j, grid))

    three_largest = sorted(basin_sizes, reverse=True)[:3]

    return three_largest[0] * three_largest[1] * three_largest[2]

if __name__ == "__main__":
    main()
