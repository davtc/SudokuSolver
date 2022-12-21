import numpy as np
from sudokuparser import get_sudoku

def split_row(sudoku, index):
    return sudoku[index, :]

def split_col(sudoku, index):
    return sudoku[:, index]

def split_square(sudoku, index):  
    c = index%3*3 
    if index < 3:
        return sudoku[0:3, c:(c+3)]
    elif index < 6:
        return sudoku[3:6, c:(c+3)]
    else:
        return sudoku[6:, c:(c+3)]

def count_unique(cells):
    return np.size((np.nonzero(cells)), 1)

def validate_sudoku(sudoku):
    for i in range(len(sudoku)):
        if count_unique(split_row(sudoku, i)) != np.size((np.nonzero(split_row(sudoku, i))), 1):
            return False
        if count_unique(split_col(sudoku, i)) != np.size((np.nonzero(split_col(sudoku, i))), 1):
            return False
        if count_unique(split_square(sudoku, i)) != len(np.nonzero(split_square(sudoku, i))):
            print(i)
            print(count_unique(split_square(sudoku, i)))
            return False

    return True

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
    print(validate_sudoku(sudoku))

if __name__ == '__main__':
    main()