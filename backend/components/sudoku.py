from .elemento import Elemento

class Board:

    def __init__(self):
#esses valores indicam a posição e valor do número a ser adicionado, inicialmente setados dessa maneira

        self.infoElement = {"newDigit": 0, "line": 0, "column": 0}

        self.matriz = []

#criamos uma matriz interna de tamanho 9 por 9 preenchida de valores nulos, posteriormente ela será preenchida pela matriz
#a partir do sumbmit
        for i in range (0,9):
            line = []
            for a in range(0,9):
                line.append(0)
            self.matriz.append(line)

#função que vincula o tabuleiro do frontend e converte a representação da matriz(box por elementos) para linha por coluna
    def vinculateBoard(self, matriz):

        for board in range(0,9):
            
            board_columm = (board%3)*3
            
            if (board < 3):
                board_line = 0
            elif (board < 6):
                board_line = 3
            elif (board < 9):
                board_line = 6

            for element in range(0,9):
                coluna = (element%3)

                if (element < 3):
                    linha = 0
                elif (element < 6):
                    linha = 1
                elif (element < 9):
                    linha = 2
                
                linha += board_line
                coluna += board_columm
                if (matriz[board][element]!=''):
                    self.matriz[linha][coluna] = Elemento(int(matriz[board][element]), linha, coluna)
                else:
                    self.matriz[linha][coluna] = Elemento(0,linha,coluna)

    
#implementar função getElement que retorna um objeto(dict) a ser retornado para o frontend

#função que imprime o tabuleiro completo
    def print_tabuleiro(self):
        print()
        for linha in range(0,9):
            print()
            for coluna in range(0,9):
                print ( self.matriz[linha][coluna].num," ",end="")
        print()
        print("---------------------------------------------------------------------")

#atualizamos as possibilidades de cada elemento
    def atualizar(self):
        for linha in range(0,9):
            for coluna in range(0,9):
                vetor=self.matriz[linha][coluna].possibilidades(self.matriz)
                self.matriz[linha][coluna].alterado = False

#analisamos e determinamos a jogada, retorna a self.matriz caso tenha encontrado uma jogada
#caso contrário retorna None
    def verificar_tabuleiro(self):
        changed = False
        elemento_vazio = False
        for linha in range(0,9):
            for coluna in range(0,9):
                if (self.matriz[linha][coluna].num==0):
                    elemento_vazio = True
                    #primeiramente analisamos as possibilidades diretas, se houver apenas 1, já adicionamos na self.matriz
                    maybe=self.matriz[linha][coluna].possibilidades(self.matriz)
                    if (len(maybe)==1):
                        self.matriz[linha][coluna].num=maybe[0]
                        self.matriz[linha][coluna].alterado = True
                        self.infoElement["newDigit"] = maybe[0]
                        self.infoElement["line"] = linha
                        self.infoElement["column"] = coluna
                        print("linha: ", linha+1)
                        print("coluna: ",coluna+1)
                        print("número: ",maybe[0])
                        changed = True
                        return changed
                    else:
                        #analisamos a caixa do elemento
                        elemento=self.matriz[linha][coluna].analisar_caixa(self.matriz)
                        if (elemento!=None):
                            self.matriz[linha][coluna].num = elemento
                            self.matriz[linha][coluna].alterado = True
                            self.infoElement["newDigit"] = elemento
                            self.infoElement["line"] = linha
                            self.infoElement["column"] = coluna
                            print("linha: ",linha+1)
                            print("coluna: ", coluna+1)
                            print("número: ",elemento)
                            changed = True
                            return changed
                        else:
                            #analisamos a linha do elemento
                            elemento=self.matriz[linha][coluna].analisar_linha(self.matriz)
                            if (elemento!=None):
                                self.matriz[linha][coluna].num=elemento
                                self.matriz[linha][coluna].alterado = True
                                self.infoElement["newDigit"] = elemento
                                self.infoElement["line"] = linha
                                self.infoElement["column"] = coluna        
                                print("linha: ",linha+1)
                                print("coluna: ", coluna+1)
                                print("número: ", elemento)
                                changed = True
                                return changed
                            else:
                                #analisamos a coluna do elemento
                                elemento=self.matriz[linha][coluna].analisar_coluna(self.matriz)
                                if (elemento!=None):
                                    self.matriz[linha][coluna].num=elemento
                                    self.matriz[linha][coluna].alterado = True
                                    self.infoElement["newDigit"] = elemento
                                    self.infoElement["line"] = linha
                                    self.infoElement["column"] = coluna
                                    print("linha: ",linha+1)
                                    print("coluna: ", coluna+1)
                                    print("número: ", elemento)
                                    changed = True
                                    return changed

        # verificamos a condição especial em linha, caixa e coluna
        # essa condição verifica casos como:
        # dois elementos da mesma linha,caixa ou coluna contém as possibilidades [1,2] enquanto um outro elemento desse contexto contém [1,2,3]
        # É evidente que o terceiro elemento só poderia conter o algarismo 3, pois se não, os demais estariam comprometidos
        # Assim, a análise especial busca verificar esse tipo de caso

        for i in range(0,9):
            var, digit, elementLinha, elementColuna = self.matriz[i][0].analisar_linha_especial(self.matriz)
            if (var==True):
                self.infoElement["newDigit"] = digit
                self.infoElement["line"] = elementLinha
                self.infoElement["column"] = elementColuna
                changed = True
                return changed

        for linha in range(0,9,3):
            for coluna in range(0,9,3):
                var, digit, elementLinha, elementColuna = self.matriz[linha][coluna].analisar_caixa_especial(self.matriz)
                if (var==True):
                    
                    self.infoElement["newDigit"] = digit
                    self.infoElement["line"] = elementLinha
                    self.infoElement["column"] = elementColuna
                    changed = True
                    return changed
        
        for i in range(0,9):
            var, digit, elementLinha, elementColuna = self.matriz[0][i].analisar_coluna_especial(self.matriz)
            if (var==True):
                self.infoElement["newDigit"] = digit
                self.infoElement["line"] = elementLinha
                self.infoElement["column"] = elementColuna
                changed = True
                return changed
        
        if (elemento_vazio==False):
            #caso não tenha mais elemento vazio, devemos setar a matriz como None
            self.matriz = None
            return True
        #retornamos e changed = False pois não houve mudança no tabuleiro
        else:
            return changed

    def getElement(self):

        if(self.matriz!=None):
            #ainda não houve mudança, logo changed = false
            changed = False
            print("JOGADA ")
            aux = 0
            #while garante que iremos verificar a self.matriz até alterá-la (limite de 10 iterações)
            while(changed==False and aux<10):
                changed = self.verificar_tabuleiro()
                aux+=1

            #caso tenha realizado 10 iterações, retornamos um objeto nulo, indicando que não foi possível encontrar uma jogada
            if(aux==10):
                print("Não foi possível solucioná-lo")
                return None

            #atualizamos a matriz (possibilidades reanalisadas) e retornamos as informações do elemento a ser inserido
            if (self.matriz!=None):
                self.print_tabuleiro()
                self.atualizar()
                print("Elemento retornado: ", self.infoElement)
                return self.infoElement
        return None

#Para resolver problemas de um nível mais elevado devemos evoluir as possibilidades de analise
