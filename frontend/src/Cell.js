import './Cell.css';
import { useState, useEffect } from 'react';

function Cell(props) {
    const { num, setNum } = useState(0)
    let className = 'cell'

    if (props.isStart) {
        className += ' start'
    }
    
    const onChange = (e) => {
        let value = e.target.value
        if (value.length == 0) {
            setNum(0)
        }
        if (value.length > 1) {
            value = value.slice(0, 1)
        }
        setNum(value)
    }

    return (
        <input className='cell'
            key={props.key}
            type='number'
            min='1'
            max='9'
            onChange={onChange}
            value={num == 0 ? '' : num}
        >
        </input>
    )
} export default Cell