import './Tab.css'
import ButtonControl from './ButtonControl';

function URLTab() {
    return (
        <div>
            <p>Enter URL with a Sudoku puzzle:</p>
            <input type='url' 
                placeholder='https://sudoku.com' 
                pattern="https://.*" size="30"
                required />
            < ButtonControl name='Submit' />
        </div>
    );
} export default URLTab