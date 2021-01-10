// Import thu vien
import React from 'react';
import ReactDom from 'react-dom';
import DatePicker from "react-datepicker";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
        };

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
            <div>
                <div style={{backgroundColor:'Violet', fontSize:'50px', textAlign:'center'}}>
                    XEM NGŨ HÀNH VÀ HỢP TUỔI.
                </div>

                <div style={{backgroundColor:'Orange', fontSize:'30px', textAlign:'center'}}>
                    Nhập năm sinh âm lịch của bạn Trai và bạn Gái bên dưới.
                </div>

                <label>Năm sinh bạn Nam:</label>
            </div>
        );
    }
}


// render hien thi
ReactDom.render(<App />, document.querySelector('#root'));

