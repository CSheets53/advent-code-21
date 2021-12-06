from copy import deepcopy

class BoardCell:
    def __init__(self, val):
        self.val = val
        self.marked = False

    def __repr__(self):
        return str(self.val)

def main():
    f = open("../inputs/d4.txt")
    lines = [line for line in f]
    f.close()

    order = lines[0].split(',')
    order = [int(n) for n in order]
    
    all_boards = []
    for i in range(2, len(lines[2:]), 6):
        new_board_raw = [line.rstrip('\n') for line in lines[i:i+5]]

        new_board = []
        for line in new_board_raw:
            new_row = [BoardCell(int(x)) for x in line.split()]
            new_board.append(new_row)

        all_boards.append(new_board)

    # print(f"Part 1: {part1(order, all_boards)}")
    print(f"Part 2: {part2(order, all_boards)}")

def is_board_solved(board):
    # Check rows
    for row in board:
        row_solved = True
        for cell in row:
            if not cell.marked:
                row_solved = False

        if row_solved:
            return True

    # Check cols
    for col_i in range(len(board)):
        col_solved = True
        for row_i in range(len(board)):
            if not board[row_i][col_i].marked:
                col_solved = False

        if col_solved:
            return True

    return False

def mark_boards(draw, boards):
    for board in boards:
        for row in board:
            for cell in row:
                if draw == cell.val and not cell.marked:
                    cell.marked = True

        if is_board_solved(board):
            return board

    return None

def calc_score(board, last_draw):
    # Find sum of all unmarked numbers
    sum_unmarked = 0
    for row in board:
        for cell in row:
            if not cell.marked:
                sum_unmarked += cell.val

    return sum_unmarked * last_draw

def part1(order, boards):
    """Find the board that'll win first, and calculate the final score of that board"""
    for drawn in order:
        solution_board = mark_boards(drawn, boards)

        if solution_board:
            return calc_score(solution_board, drawn)

def part2(order, boards):
    """Find the board that'll win last and its final score"""
    removed_board_indices = []

    for drawn in order:
        for i, board in enumerate(boards):
            for row in board:
                for cell in row:
                    if drawn == cell.val and not cell.marked:
                        cell.marked = True

            if i not in removed_board_indices and is_board_solved(board):
                removed_board_indices.append(i)

                if len(removed_board_indices) == len(boards):
                    return calc_score(board, drawn)

if __name__ == "__main__":
    main()
