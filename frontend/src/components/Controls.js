import './Controls.css';
import { useState, useEffect } from 'react';
import ButtonControl from './ButtonControl';

function Controls(props) {
    return(
        <div className='control-panel'>
            <div>
                {!props.new && <ButtonControl name='Blank' handler={props.handleBlank}/>}
                {props.new && <ButtonControl name='Start' handler={props.handleStart} />}
                <ButtonControl name='Save' />
                <ButtonControl name='Load' />
            </div>
            <div>
                <ButtonControl name='Undo' handler={props.handleUndo}/>
                <ButtonControl name='Redo' />
                <ButtonControl name='Pencil' />
                <ButtonControl name='Reset Puzzle' handler={props.handleReset} />
                <ButtonControl name='Check' />
                <ButtonControl name='Solve' />
            </div>
        </div>
    );
} export default Controls