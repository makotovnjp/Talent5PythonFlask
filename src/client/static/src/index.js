// Import thu vien
import React, { useState} from "react";
import ReactDom from 'react-dom';
import InputNumber from 'react-input-number';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '',
            manYear: 2000,
            womanYear: 2000,
            result: 'test'
        };

        this.manYearChangeHandler = this.manYearChangeHandler.bind(this);
        this.womanYearChangeHandler = this.womanYearChangeHandler.bind(this);
    }

    manYearChangeHandler = (Year) => {
        this.setState({manYear: Year});
    }

    womanYearChangeHandler = (Year) => {
        this.setState({womanYear: Year});
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

                <div>
                    <label>Năm sinh bạn Nam:</label>
                    <InputNumber min={1950} max={2021} step={1} value={this.state.manYear} onChange={this.manYearChangeHandler}/>
                </div>
                <div>
                    <label>Năm sinh bạn Nữ:</label>
                    <InputNumber min={1950} max={2021} step={1} value={this.state.womanYear} onChange={this.womanYearChangeHandler}/>
                </div>
                <div>
                    {this.state.manYear}
                    {this.state.womanYear}
                    {this.state.result}
                </div>


            </div>
        );
    }
}


// render hien thi
ReactDom.render(<App />, document.querySelector('#root'));

