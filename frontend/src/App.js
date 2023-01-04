import './App.css';
import Game from './components/Game.js'
import Controls from './components/Controls.js'
import Tab from './components/Tab'

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
      <div className='content-container'>
        <div className='game-container'>
          <Game sudoku={sudoku} />
          <Controls />
        </div>
        <div className='tab-container'>
          <Tab />
        </div>
      </div>
    </div>
  );
}

export default App;
