import './Controls.css';
import { useState } from 'react';

function Controls(props) {

    return(
        <div className='control-panel'>
            <div>
                <button>Undo</button>
                <button>Redo</button>
                <button>Pencil Marks</button>
                <button>Reset</button>
                <button>Solve</button>
            </div>
            <div>
                <button>Save</button>
                <button>Load</button>
            </div>
        </div>
    );
} export default Controls