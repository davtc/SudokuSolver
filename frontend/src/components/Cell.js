import './Game.css';
import { useState, useEffect } from 'react';

function Cell(props) {
    const [startNum, setStartNum] = useState(props.value);
    const [num, setNum] = useState(props.value);
    const [isDisabled, setIsDisabled] = useState(false);

    const [className, setClassName] = useState(() => {
        if (startNum != 0) {
            setIsDisabled(true);
            return 'cell starting';
        }
        else {
            return 'cell';
        }
    });

    useEffect(() => {
        if (num != props.value) {
            setNum(props.value);
            setStartNum(props.value);
            setIsDisabled(false);
            setClassName('cell');
        }
    })

    const onChange = (e) => {
        let value = e.target.value
        // If more than one didit is entered, take the last digit entered.
        if (value >= 1) {
            value = value.slice(-1);
            setNum(value);
            const index = parseInt(props.cellKey.split('-')[1]);
            props.getter(parseInt(value), index);
        }
    }

    const onFocus = () => {
        setClassName('cell focused');
    }

    const onBlur = () => {
        setClassName('cell');
    }

    return (
        <div>
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
        </div>
    );
} export default Cell;