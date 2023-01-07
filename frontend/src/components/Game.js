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
    const [gridHistory, setGridHistory] = useState(new Array())

    const getGridValues = (newBox, boxKey) => {
        setGrid(grid => {
            return grid.map((prevBox, index) => {
                if (index == boxKey) {
                    return newBox;
                } else {
                    return prevBox;
                }
            });
        });
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
                />
            );
    })};

    const handleBlank = () => {
        setGrid(blank);
        setSudoku(blankSudoku);
        setNewGame(newGame => !newGame);
    }
    
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
            console.log(resetSudoku)
        }
    };

    const handleReset = () => {
        setGrid(() => {
            return resetSudoku.map(box => {
                return box.map(cell => {
                    return cell
                })
            })
        });
    }

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
            />
        </div>
    );
} export default Game;