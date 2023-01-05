import './App.css';
import Game from './components/Game.js'
import Controls from './components/Controls.js'
import Tab from './components/Tab'

function App() {
  return (
    <div className="App">
      <header className='heading'>
        <h1 className='title'>Load and Solve Sudoku</h1>
      </header>
      <div className='content-container'>
        <div>
          <Game />
        </div>
        <div className='tab-container'>
          <Tab />
        </div>
      </div>
    </div>
  );
}

export default App;
