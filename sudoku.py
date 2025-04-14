import copy

def solve_sudoku(grid):
    # validate input
    if len(grid) != 9:
        raise ValueError("Invalid grid: must have 9 rows")
    for row in grid:
        if len(row) != 9:
            raise ValueError("Invalid grid: each row must have 9 elements")
        for num in row:
            if not isinstance(num, int) or num < 0 or num > 9:
                raise ValueError("Invalid grid: numbers must be integers between 0 and 9")
    
    grid_copy = copy.deepcopy(grid)
    if solve_helper(grid_copy):
        return grid_copy
    else:
        return None

def solve_helper(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_helper(grid):
                return True
            grid[row][col] = 0
    return False

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # check row
    if num in grid[row]:
        return False
    # check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True