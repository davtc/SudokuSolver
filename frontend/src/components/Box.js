import './Game.css';
import Cell from './Cell.js'
import { useState } from 'react';

function Box(props) {
    let box = props.box;
    const updateCellValue = (n, i) => {
        box[i] = n;
        const key = parseInt(props.boxKey);
        props.update(box, key)
    }

    const setBox = (box) => {
        const boxKey = props.boxKey;
        return box.map((value, index) => {
            return(
                <Cell
                    key={`${boxKey}-${index}`}
                    cellKey={`${boxKey}-${index}`}
                    value={value}
                    update={updateCellValue}
                >
                </Cell>
            );
        })}
    
    return(
        <div className='box'>
            {setBox(props.box)}
        </div>
    );
} export default Box;