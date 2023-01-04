import './Tab.css'
import URLTab from './URLTab'
import ImageTab from './ImageTab'

function Tab(props) {
    return (
        <div>
            <div className='tab-nav'>
                <h4 className='left tab active'>URL</h4>
                <h4 className='right tab'>Image</h4>
            </div>
            <div className='tab-content'>
                <img className='preview' title="Preview"></img>
                <button>Load</button>
                <URLTab></URLTab>
                <ImageTab></ImageTab>
            </div>
        </div>
    );
} export default Tab;