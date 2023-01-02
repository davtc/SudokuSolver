import './App.css';
import Game from './components/Game.js'

function App() {
  const sudoku = new Array(9).fill(new Array(9).fill(0));
  return (
    <div className="App">
      <header>
        <h1>Load and Solve Sudoku</h1>
      </header>
      <Game sudoku={sudoku}></Game>
    </div>
  );
}

export default App;
