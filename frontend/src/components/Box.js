import './Game.css';
import Cell from './Cell.js'
import { useState } from 'react';

function Box(props) {
    let box = props.box;

    const getBoxValues = (cellIndex, newValue) => {
        const boxIndex = parseInt(props.boxIndex);
        props.getter(boxIndex, cellIndex, box[cellIndex], newValue)
        box[cellIndex] = newValue;
    }

    const displayBox = (box) => {
        const boxKey = props.boxKey;
        return box.map((value, cellIndex) => {
            return(
                <Cell
                    key={`${boxKey}-${cellIndex}`}
                    cellKey={`${boxKey}-${cellIndex}`}
                    value={value}
                    sudoku={props.sudokuBox[cellIndex]}
                    getter={getBoxValues}
                >
                </Cell>
            );
        })}
    
    return(
        <div className='box'>
            {displayBox(props.box)}
        </div>
    );
} export default Box;