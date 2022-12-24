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
    for i in range(len(sudoku)):
        if len(get_unique(split_row(sudoku, i))) != count_numbers(split_row(sudoku, i)):
            return False
        if len(get_unique(split_col(sudoku, i))) != count_numbers(split_col(sudoku, i)):
            return False
        if len(get_unique(split_square(sudoku, i))) != count_numbers(split_square(sudoku, i)):
            return False

    return True

def get_possible_values(sudoku, row, col):
    unique_row = get_unique(split_row(sudoku, row))
    print(unique_row)
    unique_col = get_unique(split_col(sudoku, col))
    print(unique_col)
    index = (row // 3) * 3 + (col // 3)
    unique_square = get_unique(split_square(sudoku, index))
    print(unique_square)

    return set(range(1, 10)) - unique_row - unique_col - unique_square
    
def initialise_possible_values(sudoku):
    value = {}

    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                value[(i, j)] = get_possible_values(sudoku, i, j)
            else:
                value[(i, j)] = sudoku[i, j]

    return value

def main():
    #sudoku = get_sudoku()
    sudoku = np.array([[0, 1, 0, 0, 0, 9, 0, 3, 0], 
                        [6, 0, 0, 3, 0, 0, 8, 1, 2],
                        [0, 0, 0, 1, 0, 8, 7, 0, 0],
                        [7, 2, 0, 4, 8, 0, 0, 9, 0],
                        [3, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 5, 0, 0, 1, 6, 0, 7, 3],
                        [0, 0, 3, 7, 0, 5, 0, 0, 0],
                        [2, 4, 7, 0, 0, 1, 0, 0, 8],
                        [0, 9, 0, 8, 0, 0, 0, 4, 0]])
    print(sudoku)
    print(initialise_possible_values(sudoku))

if __name__ == '__main__':
    main()