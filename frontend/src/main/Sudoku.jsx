import React, {Component} from 'react'
import Boxes from '../components/Boxes'
import './Sudoku.css'
import axios from 'axios'
const urlBase = 'http://localhost:3000'
//url base do site


var matriz = []
for (var i=0;i<9;i++){
    matriz[i]=['','','','','','','','','']
}
console.log(matriz)

//o estado armazena os dados do tabuleiro e o novo elemento a ser adicionado
const initialState = {
    newElement: '0',
    board: matriz,
}

export default class Sudoku extends Component{

    state = {...initialState}
    
    //isso nos permite acessar as funções com this
    constructor(props){
        super(props)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.handleClickNext = this.handleClickNext.bind(this)
        this.changeElement = this.changeElement.bind(this)
        this.boardCheck = this.boardCheck.bind(this)
    }

    //quando submetemos os dados, fazemos um post para passar as informações para o backend
    handleSubmit(){
        axios.post(`${urlBase}/submit`,this.state).then(res=>{
            console.log(res.data)
        })
    }

    //essa função analisa se o sudoku foi terminado
    boardCheck(){
        for (var i = 0; i<9; i++){
            if (this.state.board[i].includes('')){
                return false
            }
        }
        return true
    }

    //como o dados retornado pelo backend é organizado como uma matriz linha por coluna
    //devemos converter essas coordenadas na representação do front (box e elementos)
    changeElement(data){

        var board = this.state.board
        const newElement = ''+data.newDigit
        console.log(newElement)

        var box = 0
        var boxElement = 0
        if (data.line < 3){box = 0}
        else if (data.line < 6){box = 3}
        else if (data.line < 9){box = 6}

        if (data.collum < 3){box += 0}
        else if (data.collum < 6){box += 1}
        else if (data.collum < 9){box +=2}

        const collum = data.collum%3
        const line = data.line%3
        boxElement = (line*3) + collum

        board[box][boxElement] = newElement

        this.setState({newElement, board})
    }


    handleClickNext(){
        //botão não realiza nenhuma ação caso o sudoku tenha sido realizado
        //caso contrário, inserimos o elemento retornado pela requisição ao backend e analisamos se o está finalizado
        if (!this.boardCheck()){
            axios.get(`${urlBase}/next`).then(res=>{
                if (res.data != null){
                    console.log(res.data)
                    this.changeElement(res.data)
                }
                else{
                    alert("Não foi possível solucionar")
                }
            })
        }
        else{alert("sudoku finalizado!")}
    }


    render(){
        return (
            <div>
                    <div className = "board">

                    <Boxes id = '0' values = {this.state.board[0]}/>
                    <Boxes id = '1' values = {this.state.board[1]} />
                    <Boxes id = '2' values = {this.state.board[2]} />
                    <Boxes id = '3' values = {this.state.board[3]} />
                    <Boxes id = '4' values = {this.state.board[4]} />
                    <Boxes id = '5' values = {this.state.board[5]} />
                    <Boxes id = '6' values = {this.state.board[6]} />
                    <Boxes id = '7' values = {this.state.board[7]} />
                    <Boxes id = '8' values = {this.state.board[8]} />

                    </div>
                    <div className ="controlButtons">

                        <button className = "button" onClick = {this.handleSubmit}>Submit</button>
                        <button className = "button" onClick = {this.handleClickNext}> Next </button>

                    </div>
            </div>


        )
    }
}