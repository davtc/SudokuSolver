import numpy as np
from sudokuparser import get_sudoku
import copy

# Return a row of the Sudoku at a specified index.
def split_row(sudoku, row):
    return sudoku[row, :]

# Return a column of the Sudoku at a specified index.
def split_col(sudoku, col):
    return sudoku[:, col]

# Return a 9x9 square of the Sudoku at a specified index.
def split_square(sudoku, index):  
    start = index%3*3 
    if index < 3:
        return sudoku[0:3, start:(start+3)]
    elif index < 6:
        return sudoku[3:6, start:(start+3)]
    else:
        return sudoku[6:, start:(start+3)]

# Return the a set of unique digits along a group of row/column/square of cells.
def get_unique(cells):
    unique = set(cells.flatten())
    if 0 in unique:
        unique.remove(0)
    return unique

# Return the number of digits along a group of row/column/square of cells.
def count_numbers(cells):
    number = np.nonzero(cells)[0].flatten()
    return len(number)

# Validate that the input Sudoku does not have repeated numbers in
#  rows/columns/squares.
def validate_sudoku(sudoku):
    for i in range(9):
        if len(get_unique(split_row(sudoku, i))) != count_numbers(split_row(sudoku, i)):
            return False
        if len(get_unique(split_col(sudoku, i))) != count_numbers(split_col(sudoku, i)):
            return False
        if len(get_unique(split_square(sudoku, i))) != count_numbers(split_square(sudoku, i)):
            return False

    return True

# Generate the set of possible values for a cell at a specified row and column.
def get_possible_values(sudoku, row, col):
    unique_row = get_unique(split_row(sudoku, row))
    unique_col = get_unique(split_col(sudoku, col))
    index = (row // 3) * 3 + (col // 3)
    unique_square = get_unique(split_square(sudoku, index))

    return set(range(1, 10)) - unique_row - unique_col - unique_square

# Generate a dictionary containing the set of possible values at all cells 
# sorted so that the lowest set of possible values is the first entry.
def possible_values(sudoku):
    values = {}

    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                values[(i, j)] = get_possible_values(sudoku, i, j)

    return dict(sorted(values.items(), key=lambda x: len(x[1])))

# Remove a certain value from every cell in a specified row/column/square.
def remove_value(values, digit, row, col):
    index = (row // 3) * 3 + (col // 3)

    for i in range(9):
        start_r = index // 3 * 3
        start_c = col // 3 * 3
        if (row, i) in values and digit in values[(row, i)]:
            values[(row, i)].remove(digit)
        if (i, col) in values and digit in values[(i, col)]:
            values[(i, col)].remove(digit)
        if i < 3:
            if (start_r, start_c + i) in values and digit in values[(start_r, start_c + i)]:
                values[(start_r, start_c + i)].remove(digit)
        elif i < 6:
            if (start_r + 1, start_c + i % 3) in values and digit in values[(start_r + 1, start_c + i % 3)]:
                values[(start_r + 1, start_c + i % 3)].remove(digit)
        elif i < 9:
            if (start_r + 2, start_c + i % 3) in values and digit in values[(start_r + 2, start_c + i % 3)]:
                values[(start_r + 2, start_c + i % 3)].remove(digit)
    
    return values

# Find all the cells with only 1 possible value and add it to the Sudoku 
# solution.
def scan(sudoku, values):
    updates = -1

    while updates != 0:
        updates = 0

        for cell, nums in values.copy().items():
            if len(nums) == 1:
                # Add the number to the Sudoku and remove it from the set of 
                # possible values of cells along its row/column/square.
                digit = nums.pop()
                # Add the 
                sudoku[cell] = digit
                values = remove_value(values, digit, cell[0], cell[1])
                values.pop(cell)
                updates += 1
    return sudoku, dict(sorted(values.items(), key=lambda x: len(x[1])))

# Function to solve the sudoku combining backtracking and pruning of the search 
# space.
# Step 1: Generate a dictionary of sets of possible values for each cell sorted
# from least to most possible values.
# Step 2: Start from the cell with the least possible values and iterate through 
# each value while backtracking when there os a contradiction.
def solve_sudoku(sudoku, values):
    if len(values) > 0:
        cell, nums = list(values.items())[0]
        for n in nums:
            # Make deep copies of the Sudoku and possible values so that they 
            # can be modified without affecting the original.
            temp_values = copy.deepcopy(values)
            temp_sudoku = copy.deepcopy(sudoku)
            temp_values.pop(cell)
            temp_sudoku[cell] = n
            temp_values = remove_value(temp_values, n, cell[0], cell[1])
            temp_sudoku, temp_values = scan(temp_sudoku, temp_values)
            # Return if the sudoku has been solved. The Sudoku is solved when
            # there are no more cells missing values.
            if len(temp_values) == 0:
                return temp_sudoku, True
            # Check if a guess is valid. If there are no more values for a cell 
            # but the Sudoku is not solved then there is a contradiction.
            if len(list(temp_values.items())[0][1]) != 0:
                # Recursively call the function if the current guess is valid.
                temp_sudoku, solved = solve_sudoku(temp_sudoku, temp_values)
                if solved:
                    return temp_sudoku, solved
        # Return False if no solution is found when there are still cells with 
        # value 0.
        if sudoku[cell] == 0:
            return sudoku, False
    # Return if the sudoku has been solved.
    else:
        return sudoku, True
    # Return False if no solution is found.
    return sudoku, False

def check_solved(sudoku):
    for i in range(9):
        if np.sum(split_row(sudoku, i)) != 45:
            return False
        if np.sum(split_col(sudoku, i)) != 45:
            return False
        if np.sum(split_square(sudoku, i)) != 45:
            return False

    return True

def main():
    sudoku = get_sudoku()
    """ sudoku = np.array([[0, 1, 0, 0, 0, 9, 0, 3, 0], 
                        [6, 0, 0, 3, 0, 0, 8, 1, 2],
                        [0, 0, 0, 1, 0, 8, 7, 0, 0],
                        [7, 2, 0, 4, 8, 0, 0, 9, 0],
                        [3, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 5, 0, 0, 1, 6, 0, 7, 3],
                        [0, 0, 3, 7, 0, 5, 0, 0, 0],
                        [2, 4, 7, 0, 0, 1, 0, 0, 8],
                        [0, 9, 0, 8, 0, 0, 0, 4, 0]]) """
    """ sudoku = np.array([[6, 5, 0, 0, 7, 9, 3, 0, 0], 
                        [0, 0, 2, 0, 0, 0, 0, 0, 6],
                        [0, 0, 9, 0, 0, 5, 0, 0, 0],
                        [0, 0, 0, 0, 2, 0, 0, 8, 0],
                        [0, 9, 0, 0, 0, 0, 0, 0, 0],
                        [5, 3, 0, 0, 0, 8, 0, 0, 4],
                        [0, 0, 0, 1, 0, 0, 7, 0, 0],
                        [0, 0, 6, 0, 0, 0, 0, 0, 0],
                        [4, 8, 0, 0, 0, 2, 0, 0, 3]]) """
    print(sudoku)
    print(validate_sudoku(sudoku))
    values = possible_values(sudoku) # Generate dictionary of possible values for each cell.
    solution, solved = solve_sudoku(sudoku,values)
    print(solved)
    print(solution)
    print(check_solved(solution))

if __name__ == '__main__':
    main()