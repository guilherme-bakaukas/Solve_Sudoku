import './Boxes.css'
import React, {Component} from 'react'

const possibleDigits = ['1','2','3','4','5','6','7','8','9']

export default class Boxes extends Component{

    constructor(props) {
        super(props);
        this.state = {
          values: props.values,
        };
        this.handleChange = this.handleChange.bind(this);
    }

    //essa função gera a mudança automática do texto  
    handleChange(event){
        
        //checamos que o valor inserido é válido

        if (!possibleDigits.includes(event.target.value) && event.target.value !== ''){
            alert("Digite valores de 1 a 9!")
            return
        }

        var values = this.state.values
        values[event.target.id] = event.target.value
        this.setState({values})
        console.log(this.state.values)
    }


    render(){
        return(
            <div className = "boxes">
                <textarea className = 'digitArea' id="0" value={this.state.values[0]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="1" value={this.state.values[1]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="2" value={this.state.values[2]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="3" value={this.state.values[3]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="4" value={this.state.values[4]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="5" value={this.state.values[5]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="6" value={this.state.values[6]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="7" value={this.state.values[7]} onChange={this.handleChange} />
                <textarea className = 'digitArea' id="8" value={this.state.values[8]} onChange={this.handleChange} />
            </div>
        )
    }
}