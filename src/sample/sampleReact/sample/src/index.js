// Import thu vien
import React from 'react';
import ReactDom from 'react-dom';

// Create App component
// ES5 (trước 2015
// const App = funtion() {
//
// }
// const App = () => {
//     // return JSX (na na html)
//     return(
//         <div>
//          hello
//         </div>
//     );
// };
// Next Step
// 1. gửi dữ liệu về flask server: import Axios from 'axios';
// 2. nhận được dữ liệu thì hiển thị như thế nào: tạo component để hiển thị kết quả
// 3. chia client, folder server ->
// app = Flask(__name__,
//             instance_relative_config=True,
//             static_folder="../../client/static",
//             template_folder="../../client/template")


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: ''};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
            <label>
            Name:
    <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
            </form>
    );
    }
}


// render hien thi
ReactDom.render(<App />, document.querySelector('#root'));

