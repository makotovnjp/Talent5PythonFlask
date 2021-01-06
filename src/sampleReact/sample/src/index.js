// Import thu vien
import React from 'react';
import ReactDom from 'react-dom';

// Create App component
// ES5 (trước 2015
// const App = funtion() {
//
// }
const App = () => {
    // return JSX (na na html)
    return(
        <div>
         hello
        </div>
    );
};

// render hien thi
ReactDom.render(<App />, document.querySelector('#root'));

