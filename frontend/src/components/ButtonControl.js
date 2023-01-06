import './Controls.css'
import { useState } from 'react';

function ButtonControl(props) {
    const [className, setClassName] = useState('');

    const highlightBtn = async () => {
        setClassName('highlight');
        await new Promise(resolve => setTimeout(resolve, 200));
        setClassName('');
    };
    const handler = () => {
        props.handler();
        highlightBtn()
    }
    return (
        <button className={className} onClick={handler}>{props.name}</button>
    );
} export default ButtonControl;