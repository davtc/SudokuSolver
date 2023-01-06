import './Game.css'
import Box from './Box.js'
import Controls from './Controls'
import { useState } from 'react';

function Game(props) {
    const startingSudoku = new Array(9).fill().map(() => {return new Array(9).fill(0)})
    startingSudoku[5][3] = 3
    const [puzzle, setPuzzle] = useState(startingSudoku);

    const getSudokuValues = (box, key) => {
        setPuzzle(puzzle => {
            const newPuzzle = puzzle.map((old, index) => {
                if (index == key) {
                    return box
                } else {
                    return old
                }
            })
            return newPuzzle
        })
    }

    const displayGrid = (grid) => {
        return grid.map((box, index) => {
            return(
                <Box
                    key={`${index}`}
                    boxKey={`${index}`}
                    box={box}
                    getter={getSudokuValues}
                />
            );
    })};

    const handleBlank = () => {
        const blank = new Array(9).fill().map(() => {return new Array(9).fill(0)});
        setPuzzle(blank)
    }
    
    const handleStart = () => {
        
    };

    return(
        <div className='game-container'>
            <div className='game'>
                {displayGrid(puzzle)}
            </div>
            <Controls
            handleBlank={handleBlank}
            handleStart={handleStart}
            />
        </div>
    );
} export default Game;