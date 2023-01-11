import './Tab.css'
import ButtonControl from './ButtonControl';
import { useState } from 'react';

function ImageTab() {
    const [file, setFile] = useState(null);

    const handleFileChange = e => {
        setFile(e.target.files[0]);
    };

    const onFileSubmit = e => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('imageFile', file)

    }

    return(
        <div>
            <form onSubmit={onFileSubmit}>
                <p>Upload an image of a Sudoku puzzle:</p>
                <input type='file' onChange={handleFileChange}/>
                <Button type='submit'>Submit</Button>
            </form>
        </div>
    );
} export default ImageTab