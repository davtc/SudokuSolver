import './Tab.css'
import URLTab from './URLTab'
import ImageTab from './ImageTab'
import { useState } from 'react';

function Tab(props) {
    const [active, setActive] = useState('urlTab');
    const [previewLoad, setPreviewLoad] = useState(false);

    const switchTab = () => {
        if (active == 'urlTab') {
            setActive('imageTab');
        } else {
            setActive('urlTab');
        }
    }

    return (
        <div>
            <div className='tab-nav'>
                <h3 className={`left tab + ${active == 'urlTab' ? 'active' : ""}`} onClick={switchTab}>URL</h3>
                <h3 className={`right tab + ${active == 'imageTab' ? 'active' : ""}`} onClick={switchTab}>Image</h3>
            </div>
            <div className='tab-content'>
                <img className='preview' title="Preview"></img>
                {previewLoad && <button>Load</button>}
                {active == 'urlTab' ? <URLTab /> : <ImageTab />}
            </div>
        </div>
    );
} export default Tab;