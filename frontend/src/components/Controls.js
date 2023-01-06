import './Controls.css';
import { useState } from 'react';
import ButtonControl from './ButtonControl';

function Controls(props) {
    return(
        <div className='control-panel'>
            <div>
                <ButtonControl name='Blank' handler={props.handleBlank}/>
                <ButtonControl name='Start' handler={props.handleStart} />
                <ButtonControl name='Save' />
                <ButtonControl name='Load' />
            </div>
            <div>
                <ButtonControl name='Undo' />
                <ButtonControl name='Redo' />
                <ButtonControl name='Pencil' />
                <ButtonControl name='Reset Puzzle' />
                <ButtonControl name='Check' />
                <ButtonControl name='Solve' />
            </div>
        </div>
    );
} export default Controls