import './Game.css';
import { useState } from 'react';

function Cell(props) {
    const [num, setNum] = useState(props.value);
    let className = 'cell';

    if (props.isStart) {
        className += ' starting';
    }
    
    const onChange = (e) => {
        let value = e.target.value
        // Default value is 0.
        if (value.length == 0) {
            value = 0
        }
        // If more than one didit is entered, take the last digit entered.
        else if (value.length > 1) {
            value = value.slice(-1);
        }
        setNum(value);
    }

    return (
        <input className='cell'
            key={props.cellKey}
            type='number'
            min='1'
            max='9'
            maxLength='1'
            onChange={onChange}
            value={num == 0 ? '' : num}
        >
        </input>
    );
} export default Cell;