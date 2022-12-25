import numpy as np
from sudokuparser import get_sudoku

def split_row(sudoku, row):
    return sudoku[row, :]

def split_col(sudoku, col):
    return sudoku[:, col]

def split_square(sudoku, index):  
    start = index%3*3 
    if index < 3:
        return sudoku[0:3, start:(start+3)]
    elif index < 6:
        return sudoku[3:6, start:(start+3)]
    else:
        return sudoku[6:, start:(start+3)]

def get_unique(cells):
    unique = set(cells.flatten())
    if 0 in unique:
        unique.remove(0)
    return unique

def count_numbers(cells):
    number = np.nonzero(cells)[0].flatten()
    return len(number)

# Validate that the input Sudoku does not have repeated numbers in rows/columns/squares.
def validate_sudoku(sudoku):
    for i in range(9):
        if len(get_unique(split_row(sudoku, i))) != count_numbers(split_row(sudoku, i)):
            return False
        if len(get_unique(split_col(sudoku, i))) != count_numbers(split_col(sudoku, i)):
            return False
        if len(get_unique(split_square(sudoku, i))) != count_numbers(split_square(sudoku, i)):
            return False

    return True

def get_possible_values(sudoku, row, col):
    unique_row = get_unique(split_row(sudoku, row))
    unique_col = get_unique(split_col(sudoku, col))
    index = (row // 3) * 3 + (col // 3)
    unique_square = get_unique(split_square(sudoku, index))

    return set(range(1, 10)) - unique_row - unique_col - unique_square
    
def initialise_possible_values(sudoku):
    values = {}

    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                values[(i, j)] = get_possible_values(sudoku, i, j)

    return values

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

def scan(sudoku, values):
    updates = -1

    while updates != 0:
        updates = 0

        for cell, nums in values.copy().items():
            if len(nums) == 1:
                digit = nums.pop()
                sudoku[cell] = digit
                values = remove_value(values, digit, cell[0], cell[1])
                values.pop(cell)
                updates += 1

    return sudoku, values

def solve_sudoku(sudoku):
    values = initialise_possible_values(sudoku)
    solution, values = scan(sudoku, values)
    
    return solution

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
    print(sudoku)
    print(validate_sudoku(sudoku))
    print(solve_sudoku(sudoku))

if __name__ == '__main__':
    main()