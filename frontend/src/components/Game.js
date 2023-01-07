import './Game.css'
import Box from './Box.js'
import Controls from './Controls'
import { useState } from 'react';

function Game(props) {
    const blank = new Array(9).fill().map(() => {return new Array(9).fill(0)});
    const [sudoku, setSudoku] = useState(blank);
    const blankPuzzle = new Array(9).fill().map(() => {return new Array(9).fill(false)});
    const [puzzle, setPuzzle] = useState(blankPuzzle);
    const [resetPuzzle, setResetPuzzle] = useState(sudoku);
    const [newGame, setNewGame] = useState(true);

    const getGridValues = (newBox, boxKey) => {
        setSudoku(sudoku => {
            return sudoku.map((prevBox, index) => {
                if (index == boxKey) {
                    return newBox;
                } else {
                    return prevBox;
                }
            });
        });
    };

    const setPuzzleStart = () => {
        setPuzzle(() => {
            return sudoku.map((box) => {
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
                    puzzleBox={puzzle[boxIndex]}
                    getter={getGridValues}
                />
            );
    })};

    const handleBlank = () => {
        setSudoku(blank);
        setPuzzle(blankPuzzle);
        setNewGame(newGame => !newGame);
    }
    
    const handleStart = () => {
        if (!sudoku.every(box => box.every(cell => cell === 0))) {
            setPuzzleStart();
            setNewGame(newGame => !newGame);
            setResetPuzzle(() => {
                let reset = JSON.stringify(sudoku);
                return JSON.parse(reset);
            });
        }
    };

    const handleReset = () => {
        console.log(resetPuzzle)
        setSudoku(resetPuzzle);
    }

    return(
        <div className='game-container'>
            <div className='game'>
                {displayGrid(sudoku)}
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