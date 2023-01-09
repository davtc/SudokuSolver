import './Game.css'
import Box from './Box.js'
import Controls from './Controls'
import { useEffect, useState } from 'react';

function Game(props) {
    const [grid, setGrid] = useState(new Array(9).fill().map(() => {return new Array(9).fill(0)}));
    const blankSudoku = new Array(9).fill().map(() => {return new Array(9).fill(false)});
    const [sudoku, setSudoku] = useState(blankSudoku);
    const [resetSudoku, setResetSudoku] = useState(new Array(9).fill().map(() => {return new Array(9).fill(0)}));
    const [newGame, setNewGame] = useState(true);
    const [gridHistory, setGridHistory] = useState([]);
    const [offsetMin, setOffsetMin] = useState(-1);
    const [offset, setOffset] = useState(-1);

    const copyValue = (value) => {
        return value;
    }

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
        return copy.slice(start, end)
    };

    const getGridValues = (boxIndex, cellIndex, oldValue, newValue) => {
        setGrid(updateArray(grid, boxIndex, cellIndex, newValue, 2));
        if (offset < gridHistory.length - 1) {
            setGridHistory([...sliceArray(gridHistory, 0, offset + 1, 1), {
                boxIndex: boxIndex,
                cellIndex: cellIndex,
                oldValue: oldValue,
                newValue: newValue
            }
            ])
            setOffset(offset + 1);
        } else {
            addGridHistory(boxIndex, cellIndex, oldValue, newValue);
        }
    };



    const addGridHistory = (boxIndex, cellIndex, oldValue, newValue) => {
        setGridHistory([...gridHistory, { 
                boxIndex: boxIndex,
                cellIndex: cellIndex,
                oldValue: oldValue,
                newValue: newValue
            }]
        );
        setOffset(copyValue(offset) + 1)
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
        setGrid(new Array(9).fill().map(() => {return new Array(9).fill(0)}));
        setSudoku(blankSudoku);
        setResetSudoku(new Array(9).fill().map(() => {return new Array(9).fill(0)}));
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
            const min = gridHistory.length - 1
            setOffsetMin(copyValue(min));
            setOffset(copyValue(min));
        }
    };

    const handleReset = () => {
        setGrid(createCopy(resetSudoku, 2));
        setGridHistory(sliceArray(gridHistory, 0, offsetMin + 1, 1));
        setOffsetMin(copyValue(offsetMin));
        setOffset(copyValue(offsetMin));
    };

    const handleUndo = () => {
        if (offset > offsetMin) {
            setOffset(Math.max(offset - 1, offsetMin + 1));
            const { boxIndex, cellIndex, oldValue } = gridHistory[offset];
            setGrid(updateArray(grid, boxIndex, cellIndex, oldValue, 2));
        }
    };

    const handleRedo = () => {
        setOffset(Math.min(offset + 1, gridHistory.length - 1));
        const { boxIndex, cellIndex, newValue } = gridHistory[offset];
        setGrid(updateArray(grid, boxIndex, cellIndex, newValue, 2));
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
                handleRedo = {handleRedo}
            />
        </div>
    );
} export default Game;