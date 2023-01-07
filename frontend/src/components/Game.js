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

    const getGridValues = (newBox, boxKey) => {
        setGrid(grid => {
            return grid.map((prevBox, boxIndex) => {
                if (boxIndex == boxKey) {
                    return newBox;
                } else {
                    return prevBox;
                }
            });
        });
    };

    const addGridHistory = (cellIndex, boxIndex, oldValue, newValue) => {
        setGridHistory([...gridHistory, { 
            cellIndex: cellIndex,
            boxIndex: boxIndex,
            oldValue: oldValue,
            newValue: newValue
        }]);
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
                    boxKey={`${boxIndex}`}
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
        setOffsetMin(0);
        setOffset(0);
    };
    
    const handleStart = () => {
        if (!grid.every(box => box.every(cell => cell === 0))) {
            setStartingSudoku();
            setNewGame(newGame => !newGame);
            setResetSudoku(() => {
                return grid.map(box => {
                    return box.map(cell => {
                        return cell
                    })
                })
            });
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
        setGrid(() => {
            return resetSudoku.map(box => {
                return box.map(cell => {
                    return cell;
                })
            })
        });
        setGridHistory(gridHistory => gridHistory.slice(0, offsetMin))
        setOffset(min);
    };
    
    const updateGrid = (cellIndex, boxIndex, value) => {
        setGrid(grid => {
            return grid.map((box, b) => {
                if (b == boxIndex) {
                    return box.map((cell, c) => {
                        if (c == cellIndex) {
                            return value;
                        } else {
                            return cell;
                        }
                    });
                } else {
                    return box;
                }
            })
        })
    }

    const handleUndo = () => {
        if (offset > offsetMin) {
            setOffset(offset => offset - 1);
            const { cellIndex, boxIndex, oldValue, newValue } = gridHistory[offset];
            console.log(gridHistory[offset])
            updateGrid(cellIndex, boxIndex, oldValue);
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