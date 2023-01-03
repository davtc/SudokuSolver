import './App.css';
import Game from './components/Game.js'
import Controls from './components/Controls.js'
import Loader from './components/Loader.js'

function App() {
  const sudoku = new Array(9).fill().map(() => {return new Array(9).fill(0)});
  sudoku[5][1] = 2;
  sudoku[3][3] = 5;
  console.log(sudoku)
  return (
    <div className="App">
      <header className='heading'>
        <h1 className='title'>Load and Solve Sudoku</h1>
      </header>
      <div className='app-container'>
        <div className='game-container'>
          <Game sudoku={sudoku}></Game>
          <Controls></Controls>
        </div>
        <div>
          <Loader></Loader>
        </div>
      </div>
    </div>
  );
}

export default App;
