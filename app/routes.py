from app import app
from flask import request, jsonify

from sudokusolver import validate_sudoku, init_possible_values, solve_sudoku, check_solved

@app.route('/validate', methods = ['POST'])
def validate():
    data = request.json()
    sudoku = data.get('sudoku')
    print(sudoku)
    response = jsonify({
        'validate': validate_sudoku(sudoku)
    })
    return response

@app.route('/solve', methods = ['POST'])
def solve():
    data = request.json()
    sudoku = data.get('sudoku')
    if validate_sudoku(sudoku):
        values = init_possible_values(sudoku)
        solution, solved = solve_sudoku(sudoku, values)
        if solved and check_solved(sudoku):
            response = jsonify({
                'message': 'SUCCESS',
                'solved': solved,
                'solution': solution
            })
        else:             
            response = jsonify({
                'message': 'UNSUCCESSFUL',
                'solved': solved,
                'solution': sudoku
            })
    else:
        response = jsonify({
                'message': 'INVALID'
            })

    return response