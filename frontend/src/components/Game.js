import './Game.css'
import Box from './Box.js'
import Controls from './Controls'
import { useState } from 'react';

function Game(props) {
    const blank = new Array(9).fill().map(() => {return new Array(9).fill(0)});
    const [grid, setGrid] = useState(blank);
    const blankSudoku = new Array(9).fill().map(() => {return new Array(9).fill(false)});
    const [sudoku, setSudoku] = useState(blankSudoku);
    const [resetSudoku, setResetSudoku] = useState(blank);
    const [newGame, setNewGame] = useState(true);
    const [gridHistory, setGridHistory] = useState([]);
    let min = -1;
    const [offsetMin, setOffsetMin] = useState(min);
    const [offset, setOffset] = useState(min)

    const createCopy = (array, dimension) => {
        return array.map(row => {
            if (dimension == 1) {
                return row
            }
            if (dimension == 2) {
                return row.map(col => {
                    return col;
                })
            }
        });
    };

    const updateArray = (array, row, col, value, dimension) => {
        let copy = createCopy(array, dimension);
        copy[row][col] = value;
        return copy;
    };

    const sliceArray = (array, start, end, dimension) => {
        const copy = createCopy(array, dimension);
        return copy.slice(start, end);
    };

    const getGridValues = (boxIndex, cellIndex, oldValue, newValue) => {
        setGrid(grid => updateArray(grid, boxIndex, cellIndex, newValue, 2));
        if (offset < gridHistory.length - 1) {
            setGridHistory(gridHistory => sliceArray(gridHistory, 0, offset + 1, 1))
        }
        addGridHistory(boxIndex, cellIndex, oldValue, newValue);
    };



    const addGridHistory = (boxIndex, cellIndex, oldValue, newValue) => {
        setGridHistory(gridHistory => {
            let copy = createCopy(gridHistory, 1);
            copy.push({ 
                boxIndex: boxIndex,
                cellIndex: cellIndex,
                oldValue: oldValue,
                newValue: newValue
            });
            return copy;
        });
        setOffset(offset => offset + 1)
    };

    const setStartingSudoku = () => {
        setSudoku(() => {
            return grid.map((box) => {
                return box.map((cell) => {
                    if (cell == 0) {
                        return false;
                    } else {
                        return true;
                    }
                })
            });
        });
    };

    const displayGrid = (grid) => {
        return grid.map((box, boxIndex) => {
            return(
                <Box
                    key={`${boxIndex}`}
                    boxIndex={`${boxIndex}`}
                    box={box}
                    sudokuBox={sudoku[boxIndex]}
                    getter={getGridValues}
                    history={addGridHistory}
                />
            );
    })};

    const handleBlank = () => {
        setGrid(blank);
        setSudoku(blankSudoku);
        setResetSudoku(blank);
        setNewGame(newGame => !newGame);
        setGridHistory([]);
        setOffsetMin(-1);
        setOffset(-1);
    };
    
    const handleStart = () => {
        if (!grid.every(box => box.every(cell => cell === 0))) {
            setStartingSudoku();
            setNewGame(newGame => !newGame);
            setResetSudoku(createCopy(grid, 2));
            min = grid.reduce((totalCount, box) => {
                return totalCount += box.reduce((count, value) => {
                    if (value > 0) {
                        return count += 1;
                    } else {
                        return count;
                    }
                }, 0);
            }, 0) - 1;
            setOffsetMin(min);
            setOffset(min);
        }
    };

    const handleReset = () => {
        setGrid(createCopy(resetSudoku, 2));
        setGridHistory(gridHistory => sliceArray(gridHistory, 0, offsetMin, 1));
        setOffset(min);
    };

    const handleUndo = () => {
        if (offset > offsetMin) {
            setOffset(offset => offset - 1);
            const { boxIndex, cellIndex, oldValue } = gridHistory[offset];
            setGrid(grid => updateArray(grid, boxIndex, cellIndex, oldValue, 2));
        }
    };
    
    return(
        <div className='game-container'>
            <div className='game'>
                {displayGrid(grid)}
            </div>
            <Controls
                new={newGame}
                handleBlank={handleBlank}
                handleStart={handleStart}
                handleReset={handleReset}
                handleUndo = {handleUndo}
            />
        </div>
    );
} export default Game;