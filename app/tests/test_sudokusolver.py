import pytest
import numpy as np

import sys

sys.path.append('../sudokusolver/app')

import sudokusolver as ss

# Input Sudokus obtained from https://sudoku.com/.
@pytest.fixture
def input_sudoku():
    sudoku = [
        # Simple Sudoku
        np.array([[0, 2, 6, 0, 0, 0, 3, 7, 8], 
                  [0, 5, 8, 6, 3, 7, 4, 0, 0],
                  [0, 4, 7, 0, 0, 0, 5, 6, 1],
                  [0, 0, 0, 7, 2, 0, 9, 0, 0],
                  [0, 0, 0, 3, 0, 8, 2, 5, 0],
                  [8, 0, 2, 0, 0, 0, 0, 1, 0],
                  [4, 6, 9, 5, 0, 1, 0, 0, 0],
                  [0, 0, 1, 9, 0, 0, 7, 4, 0],
                  [0, 3, 0, 0, 4, 0, 0, 9, 0]]),
        # Medium Sudoku
        np.array([[0, 1, 0, 0, 0, 9, 0, 3, 0], 
                  [6, 0, 0, 3, 0, 0, 8, 1, 2],
                  [0, 0, 0, 1, 0, 8, 7, 0, 0],
                  [7, 2, 0, 4, 8, 0, 0, 9, 0],
                  [3, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 5, 0, 0, 1, 6, 0, 7, 3],
                  [0, 0, 3, 7, 0, 5, 0, 0, 0],
                  [2, 4, 7, 0, 0, 1, 0, 0, 8],
                  [0, 9, 0, 8, 0, 0, 0, 4, 0]]),
        # Difficult Sudoku
        np.array([[6, 5, 0, 0, 7, 9, 3, 0, 0], 
                  [0, 0, 2, 0, 0, 0, 0, 0, 6],
                  [0, 0, 9, 0, 0, 5, 0, 0, 0],
                  [0, 0, 0, 0, 2, 0, 0, 8, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 0],
                  [5, 3, 0, 0, 0, 8, 0, 0, 4],
                  [0, 0, 0, 1, 0, 0, 7, 0, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0, 0],
                  [4, 8, 0, 0, 0, 2, 0, 0, 3]]),
        # Invalid Sudoku
        np.array([[6, 0, 0, 0, 0, 0, 6, 0, 0], 
                  [0, 0, 1, 0, 0, 0, 0, 0, 6],
                  [0, 0, 0, 0, 0, 3, 0, 0, 0],
                  [0, 0, 0, 0, 5, 0, 0, 8, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 0],
                  [5, 0, 0, 0, 0, 8, 0, 0, 4],
                  [0, 0, 0, 1, 0, 0, 7, 0, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0, 0],
                  [4, 8, 0, 0, 0, 2, 0, 0, 3]])
    ]
    return sudoku

@pytest.fixture
def solved_sudoku():
    solution = [np.array([[8, 1, 2, 6, 7, 9, 5, 3, 4],
                          [6, 7, 9, 3, 5, 4, 8, 1, 2],
                          [4, 3, 5, 1, 2, 8, 7, 6, 9],
                          [7, 2, 1, 4, 8, 3, 6, 9, 5],
                          [3, 6, 4, 5, 9, 7, 2, 8, 1],
                          [9, 5, 8, 2, 1, 6, 4, 7, 3],
                          [1, 8, 3, 7, 4, 5, 9, 2, 6],
                          [2, 4, 7, 9, 6, 1, 3, 5, 8],
                          [5, 9, 6, 8, 3, 2, 1, 4, 7]
    ])]
    return  solution

def test_get_unique(input_sudoku):
    row = ss.split_row(input_sudoku[1], 3)
    col = ss.split_col(input_sudoku[2], 5)
    square = ss.split_square(input_sudoku[1], 0)
    assert ss.get_unique(row) == {2, 4, 7, 8, 9}
    assert ss.get_unique(col) == {2, 5, 8, 9}
    assert ss.get_unique(square) == {1, 6}

def test_validate_sudoku(input_sudoku):
    assert ss.validate_sudoku(input_sudoku[0]) == True
    assert ss.validate_sudoku(input_sudoku[1]) == True
    assert ss.validate_sudoku(input_sudoku[2]) == True
    assert ss.validate_sudoku(input_sudoku[3]) == False

def test_get_possible_valies(input_sudoku):
    assert ss.get_possible_values(input_sudoku[1], 8, 8) == {5, 6, 7}

def test_scan_sudoku(input_sudoku):
    values = ss.init_possible_values(input_sudoku[1])
    assert values == {(1, 1): {7}, (2, 1): {3}, (3, 5): {3}, (1, 5): {4, 7}, (2, 7): {5, 6}, (3, 2): {1, 6}, (3, 6): {5, 6}, (3, 8): {5, 6}, (4, 1): {8, 6}, (4, 5): {2, 7}, (5, 3): {9, 2}, (5, 6): {2, 4}, (6, 0): {8, 1}, (6, 1): 
                     {8, 6}, (6, 7): {2, 6}, (6, 8): {9, 6}, (7, 3): {9, 6}, (7, 7): {5, 6}, (8, 0): {1, 5}, (8, 5): {2, 3}, (0, 0): {8, 4, 5}, (0, 3): {2, 5, 6}, (0, 6): {4, 5, 6}, (0, 8): {4, 5, 6}, (1, 2): {9, 4, 5}, (1, 4): {4, 5, 7}, (2, 0): {9, 4, 5}, (4, 3): {9, 2, 5}, (5, 0): {8, 9, 4}, (5, 2): {8, 9, 4}, (7, 4): {9, 3, 6}, (8, 2): {1, 5, 6}, (8, 4): {2, 3, 6}, (8, 8): {5, 6, 7}, (0, 2): {8, 2, 4, 5}, (2, 2): {9, 2, 4, 5}, (2, 4): {2, 4, 5, 6}, (2, 8): {9, 4, 5, 6}, (4, 2): {8, 9, 4, 6}, (4, 4): {9, 2, 5, 7}, (4, 6): {2, 4, 5, 6}, (4, 7): {8, 2, 5, 6}, (6, 4): {9, 2, 4, 6}, (6, 6): {1, 2, 6, 9}, (7, 6): {9, 3, 5, 6}, (0, 4): {2, 
                     4, 5, 6, 7}, (8, 6): {1, 2, 3, 5, 6}}
    sudoku, values = ss.scan_sudoku(input_sudoku[1], values)
    scan = np.array([[0, 1, 0, 0, 0, 9, 0, 3, 0],
                     [6, 7, 9, 3, 5, 4, 8, 1, 2],
                     [0, 3, 0, 1, 0, 8, 7, 0, 0],
                     [7, 2, 0, 4, 8, 3, 0, 9, 0],
                     [3, 0, 0, 0, 0, 7, 0, 0, 1],
                     [0, 5, 0, 0, 1, 6, 0, 7, 3],
                     [0, 0, 3, 7, 0, 5, 0, 0, 0],
                     [2, 4, 7, 0, 0, 1, 0, 0, 8],
                     [0, 9, 0, 8, 0, 2, 0, 4, 0]])
    assert (sudoku == scan).all()

def test_solve_sudoku(input_sudoku, solved_sudoku):
    values = ss.init_possible_values(input_sudoku[1])
    solution, values = ss.solve_sudoku(input_sudoku[1], values)
    assert (solution == solved_sudoku[0]).all()

def test_check_solved(solved_sudoku):
    assert ss.check_solved(solved_sudoku[0]) == True