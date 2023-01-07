import './Controls.css';
import { useState, useEffect } from 'react';
import ButtonControl from './ButtonControl';

function Controls(props) {
    return(
        <div className='control-panel'>
            <div>
                {!props.new && <ButtonControl name='Blank' handler={props.handleBlank}/>}
                {props.new && <ButtonControl name='Start' handler={props.handleStart} />}
                <ButtonControl name='Save' handler={props.handleBlank}/>
                <ButtonControl name='Load' handler={props.handleBlank}/>
            </div>
            <div>
                <ButtonControl name='Undo' handler={props.handleUndo}/>
                <ButtonControl name='Redo' handler={props.handleBlank}/>
                <ButtonControl name='Pencil' handler={props.handleBlank}/>
                <ButtonControl name='Reset Puzzle' handler={props.handleReset} />
                <ButtonControl name='Check' handler={props.handleBlank}/>
                <ButtonControl name='Solve' handler={props.handleBlank}/>
            </div>
        </div>
    );
} export default Controls