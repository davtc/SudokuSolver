import './Tab.css'

function URLTab() {
    return (
        <div>
            <p>Enter URL with a Sudoku puzzle:</p>
            <input type='url' 
                placeholder='https://sudoku.com' 
                pattern="https://.*" size="30"
                required />
            <button>Submit</button>
        </div>
    );
} export default URLTab