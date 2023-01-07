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
        setNewGame(newGame => !newGame);
        setGridHistory([]);
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
    };
    
    const handleUndo = () => {
        console.log(gridHistory);
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