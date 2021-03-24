from flask import Flask
from flask import request, jsonify, make_response
from components.sudoku import Board

app = Flask(__name__)


#aqui alteramos a url do servidor
app.config['SERVER_NAME'] = 'localhost:3000'

#REQUISIÇÃO POST
#request.get_json serve para pegar dados em json
#transforma json em dicionario de python

#instanciamos um objeto da classe Board
boardElement = Board()

#aqui iremos receber o tabuleiro inicial do sudoku
#portanto, vinculamos esse dado ao tabuleiro da classe Board
@app.route("/submit", methods=["POST"])
def submit():

    req = request.get_json()
    board = req.get("board")
    boardElement.vinculateBoard(board)
        
    return "submit recieved"

#essa requisição é feita pelo frontend a fim de coletar informações sobre o elemento a ser adicionado ao sudoku
@app.route("/next", methods=["GET"])
def next():

    #chamamos a função que retorna um dicionário contendo as informações do elemento as ser adicionado
    response = boardElement.getElement()

    res = make_response(jsonify(response),200)
    #jsonify converte em json

    return res

if __name__ == "__main__":
    app.run()