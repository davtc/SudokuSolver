import './Game.css';
import Cell from './Cell.js'
import { useState } from 'react';

function Box(props) {
    let box = props.box;

    const getBoxValues = (n, i) => {
        box[i] = n;
        const boxKey = parseInt(props.boxKey);
        props.getter(box, boxKey)
    }

    const displayBox = (box) => {
        const boxKey = props.boxKey;
        return box.map((value, cellIndex) => {
            return(
                <Cell
                    key={`${boxKey}-${cellIndex}`}
                    cellKey={`${boxKey}-${cellIndex}`}
                    value={value}
                    puzzle={props.puzzleBox[cellIndex]}
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