import './Game.css'
import Box from './Box.js'
import Controls from './Controls'
import { useState } from 'react';

function Game(props) {
    const startingSudoku = new Array(9).fill().map(() => {return new Array(9).fill(0)})
    const [puzzle, setPuzzle] = useState(startingSudoku);
    let sudoku = startingSudoku;

    const updateSudokuValues = (box, key) => {
        sudoku[key] = box;
        console.log(sudoku)
    }

    const setGrid = (grid) => {
        return grid.map((box, index) => {
            return(
                <Box
                    key={`${index}`}
                    boxKey={`${index}`}
                    box={box}
                    update={updateSudokuValues}
                />
            );
    })};
    
    const getBoxValues = () => {

    }
    const handleStart = () => {
        setPuzzle(sudoku);
        console.log(puzzle)
    };

    return(
        <div className='game-container'>
            <div className='game'>
                {setGrid(puzzle)}
            </div>
            <Controls
            handleStart={handleStart}
            />
        </div>
    );
} export default Game;