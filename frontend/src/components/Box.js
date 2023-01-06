import './Game.css';
import Cell from './Cell.js'
import { useState } from 'react';

function Box(props) {
    let box = props.box;

    const getCellValue = (n, i) => {
        box[i] = n;
        const key = parseInt(props.boxKey);
        props.getter(box, key)
    }

    const displayBox = (box) => {
        const boxKey = props.boxKey;
        return box.map((value, index) => {
            return(
                <Cell
                    key={`${boxKey}-${index}`}
                    cellKey={`${boxKey}-${index}`}
                    value={value}
                    getter={getCellValue}
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