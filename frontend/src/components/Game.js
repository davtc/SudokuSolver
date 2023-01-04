import './Game.css'
import Box from './Box.js'

function Game(props) {
    const setGrid = (grid) => {
        return grid.map((box, index) => {
            return(
                <Box
                    key={`${index}`}
                    boxKey={`${index}`}
                    box={box}
                />
            );
        })}
    return(
        <div className='game'>
            {setGrid(props.sudoku)}
        </div>
    );
} export default Game;