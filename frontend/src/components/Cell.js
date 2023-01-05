import './Game.css';
import { useState } from 'react';

function Cell(props) {
    const [num, setNum] = useState(props.value);
    const [isDisabled, setIsDisabled] = useState(false);
    const checkStart = (value) => {
        if (value != 0) {
            setIsDisabled(true);
            return 'cell starting';
        }
        else {
            return 'cell';
        }
    };
    const [className, setClassName] = useState(() => {return checkStart(num)});
    
    const onChange = (e) => {
        let value = e.target.value
        // Default value is 0.
        if (value.length == 0) {
            value = 0;
        }
        // If more than one didit is entered, take the last digit entered.
        else if (value.length > 1) {
            value = value.slice(-1);
        }
        setNum(value);
        const index = parseInt(props.cellKey.split('-')[1]);
        props.update(parseInt(value), index);
    }

    const onFocus = () => {
        setClassName(className => className + ' focused');
    }

    const onBlur = () => {
        setClassName(className => className.split(' focused')[0]);
    }

    return (
        <input className={className}
            key={props.cellKey}
            type='number'
            min='1'
            max='9'
            maxLength='1'
            onChange={onChange}
            onFocus={onFocus}
            onBlur={onBlur}
            value={num == 0 ? '' : num}
            disabled={isDisabled}
        />

    );
} export default Cell;