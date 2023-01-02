import './Game.css';
import Cell from './Cell.js'

function Box(props) {
    const setBox = (box) => {
        const boxKey = props.boxKey;
        return box.map((value, index) => {
            return(
                <Cell
                    key={`${boxKey}-${index}`}
                    value={value}
                    isStart={props.isStart}
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