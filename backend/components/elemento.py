class Elemento:
    def __init__(self,num,linha,coluna):
        self.num=num
        self.linha=linha
        self.coluna=coluna
        self.vetor_possibilidades=[]
        self.alterado = False
        #vetor contém as possibilidade de preenchimento daquele espaço
        #alterado atua para gerar uma coloração diferente para o elemento alterado na jogada

    #função que retorna um vetor com os elementos da linha
    def elementos_linha(self,matriz):
        valores_linha=[]
        for i in range(0,9):
            valores_linha.append(matriz[self.linha][i])#os numeros da linha contém ele mesmo
        return valores_linha

    #função que retorna um vetor com os elementos da coluna
    def elementos_coluna(self,matriz):
        valores_coluna=[]
        for i in range(0,9):
            valores_coluna.append(matriz[i][self.coluna])#os numeros da coluna contém ele mesmo
        return valores_coluna

    #função que retorna um vetor com os elementos da caixa
    def elementos_caixa(self,matriz):
        valores_caixa=[]
        if (self.linha<3):
            if (self.coluna<3):
                for linha1 in range(0,3):
                    for coluna1 in range(0,3):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<6):
                for linha1 in range(0,3):
                    for coluna1 in range(3,6):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<9):
                for linha1 in range(0,3):
                    for coluna1 in range(6,9):
                        valores_caixa.append(matriz[linha1][coluna1])
        elif(self.linha<6):
            if(self.coluna<3):
                for linha1 in range(3,6):
                    for coluna1 in range(0,3):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<6):
                for linha1 in range(3,6):
                    for coluna1 in range(3,6):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<9):
                for linha1 in range(3,6):
                    for coluna1 in range(6,9):
                        valores_caixa.append(matriz[linha1][coluna1])
        elif(self.linha<9):
            if(self.coluna<3):
                for linha1 in range(6,9):
                    for coluna1 in range(0,3):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<6):
                for linha1 in range(6,9):
                    for coluna1 in range(3,6):
                        valores_caixa.append(matriz[linha1][coluna1])
            elif(self.coluna<9):
                for linha1 in range(6,9):
                    for coluna1 in range(6,9):
                        valores_caixa.append(matriz[linha1][coluna1])

        return valores_caixa

    #retorna um vetor de possibilidades diretas da posição
    def possibilidades(self,matriz):
        maybe=[1,2,3,4,5,6,7,8,9]

        #retiramos os elementos da linha do vetor de possibilidades
        vetor=self.elementos_linha(matriz)
        for linhas in range(0,9):
            if (vetor[linhas].num in maybe):
                maybe.remove(vetor[linhas].num)

        #retiramos os elementos da coluna do vetor de possibilidades
        vetor=self.elementos_coluna(matriz)
        for colunas in range(0,9):
            if (vetor[colunas].num in maybe):
                maybe.remove(vetor[colunas].num)

        #retiramos os elementos da caixa do vetor de possibilidades
        vetor=self.elementos_caixa(matriz)
        for elementos in range(0,9):
            if (vetor[elementos].num in maybe):
                maybe.remove(vetor[elementos].num)

        #deixamos o vetor ordenado e o adicionamos ao vetor de possibilidades do elemento
        maybe.sort()
        self.vetor_possibilidades=maybe
        return maybe

    def analisar_linha(self,matriz):
        matriz_possibilidades=[]
        maybe1=self.possibilidades(matriz)
        maybe=[]
        for i in maybe1:
            maybe.append(i)
        #analisamos os elementos da linha
        for i in range(0,9):
            if (matriz[self.linha][i].num==0 and i!=self.coluna):
                possibilidades=matriz[self.linha][i].possibilidades(matriz)
                matriz_possibilidades.append(possibilidades)
                #com isso, matriz_possibilidades passa a ser uma matriz com vetores de possibilidades dos elementos da linha

        #Portanto, se houver a mesma possibilidade em algum elemento da linha, ela não deve ser considerada
        for elemento_analisado in maybe1:
            for possibilidade_da_linha in matriz_possibilidades:
                if (elemento_analisado in possibilidade_da_linha):
                    maybe.remove(elemento_analisado)
                    break
        #caso haja apenas uma possibilidade, retornamos o valor
        #caso contrário, retornamos None
        if (len(maybe)==1):
            return maybe[0]
        return None

    # Mesmo raciocínio das linhas
    def analisar_coluna(self,matriz):
        elementos=self.elementos_coluna(matriz)
        vetor=[]
        maybe1=self.possibilidades(matriz)
        maybe=[]
        for i in maybe1:
            maybe.append(i)
        for elemento in elementos:
            if(elemento.num==0 and elemento.linha!=self.linha):
                vetor.append(elemento.possibilidades(matriz))
        for elemento_analisado in maybe1:
            for elemento_da_coluna in vetor:
                if(elemento_analisado in elemento_da_coluna):
                    maybe.remove(elemento_analisado)
                    break
        if (len(maybe)==1):
            return maybe[0]
        return None

    # Mesmo raciocínio das linhas
    def analisar_caixa(self,matriz):
        elementos=self.elementos_caixa(matriz)
        vetor=[]
        maybe1=self.possibilidades(matriz)
        maybe=[]
        for i in maybe1:
            maybe.append(i)
        for elemento in elementos:
            if (elemento.num==0 and (elemento.coluna!=self.coluna or elemento.linha!=self.linha)):
                vetor.append(elemento.possibilidades(matriz))
        for elemento_analisado in maybe1:
            for elemento_da_caixa in vetor:
                if(elemento_analisado in elemento_da_caixa):
                    maybe.remove(elemento_analisado)
                    break
        if (len(maybe)==1):
            return maybe[0]
        return None

    #retorna um vetor com os elementos dos vetores iguais
    def verification(self,vetor_comparacao):
        vetor=[]

        for i in range(0,len(vetor_comparacao)):
            count=0

            if(len(vetor_comparacao[i])==3): # verificamos quando há vetores repetidos com 3 elementos
                for a in range(0,len(vetor_comparacao)):
                    if(vetor_comparacao[i]==vetor_comparacao[a]):
                        count+=1

                #devemos ter 3 vetores com 3 elementos repetidos, pois assim restringimos esses elementos à apenas essas posições
                if (count==3):
                    if (vetor_comparacao[i] not in vetor):
                        vetor.append(vetor_comparacao[i])
                        #adicionamos o vetor repetido

            if(len(vetor_comparacao[i])==2): # verificamos quando há vetores repetidos com 2 elementos
                for a in range(0,len(vetor_comparacao)):
                    if(vetor_comparacao[i]==vetor_comparacao[a]):
                        count+=1

                #devemos ter 2 vetores com 2 elementos repetidos, pois assim restringimos esses elementos à apenas essas posições
                if(count==2):
                    if(vetor_comparacao[i] not in vetor):
                        vetor.append(vetor_comparacao[i])
                        #adicionamos o vetor repetido
        return vetor

    def analisar_coluna_especial(self,matriz):

        vetor=[]
        vetor_de_posicoes=[]
        vetor_comparacao=[]

        for i in range(0,9):
            if(matriz[i][self.coluna].num==0):
                vetor.append(matriz[i][self.coluna])

        var=False
        for i in range(0,len(vetor)):
            for a in range(i+1,len(vetor)):
                if(vetor[i].vetor_possibilidades==vetor[a].vetor_possibilidades):
                    #guardamos as posições e conteúdo dos vetores iguais
                    vetor_de_posicoes.append(i)
                    vetor_de_posicoes.append(a)
                    vetor_comparacao.append(vetor[i].vetor_possibilidades)
                    vetor_comparacao.append(vetor[a].vetor_possibilidades)
                    var=True

        #verificamos essa igualdade (se será possível restringir as possibilidades)
        var1=matriz[0][0].verification(vetor_comparacao)

        if (var==True and len(var1)!=0):# se houver vetores iguais e passíveis de restrição
            for i in range(0,len(vetor)):
                if(i not in vetor_de_posicoes):
                    for a in vetor[i].vetor_possibilidades:
                        for b in var1:
                            if(a in b):
                                #removemos as possibilidades que também estão nos vetores repetidos (restritos à essas posições)
                                vetor[i].vetor_possibilidades.remove(a)

            #se após isso, houver apenas uma possibilidade em algum elemento, retornamos true e alteramos o valor do elemento
            for i in vetor:
                if(len(i.vetor_possibilidades)==1):
                    i.num=i.vetor_possibilidades[0]
                    i.alterado = True
                    print("linha: ",i.linha+1)
                    print("coluna: ", i.coluna+1)
                    print("número: ", i.num)
                    return True, i.num, i.linha, i.coluna
        return False, 0, 0, 0

    #mesmo raciocínio da coluna especial
    def analisar_linha_especial(self,matriz):

        vetor=[]
        vetor_de_posicoes=[]
        vetor_comparacao=[]

        for i in range(0,9):
            if(matriz[self.linha][i].num==0):
                vetor.append(matriz[self.linha][i])

        var=False
        for i in range(0,len(vetor)):
            for a in range(i+1,len(vetor)):
                if(vetor[i].vetor_possibilidades==vetor[a].vetor_possibilidades):
                    vetor_de_posicoes.append(i)#guardamos as posições dos iguai
                    vetor_de_posicoes.append(a)
                    vetor_comparacao.append(vetor[i].vetor_possibilidades)
                    vetor_comparacao.append(vetor[a].vetor_possibilidades)
                    var=True

        var1=matriz[0][0].verification(vetor_comparacao)
        if (var==True and len(var1)!=0):#se houver vetores iguais
            for i in range(0,len(vetor)):
                if(i not in vetor_de_posicoes):
                    for a in vetor[i].vetor_possibilidades:
                        if(a in vetor_comparacao):
                            vetor[i].vetor_possibilidades.remove(a)
            for i in vetor:
                if(len(i.vetor_possibilidades)==1):
                    i.num=i.vetor_possibilidades[0]
                    i.alterado = True
                    print("linha: ",i.linha+1)
                    print("coluna: ", i.coluna+1)
                    print("número: ", i.num)
                    return True, i.num, i.linha, i.coluna
        return False, 0, 0, 0

    #mesmo raciocínio da coluna especial
    def analisar_caixa_especial(self,matriz):

        vetor=[]
        vetor_de_posicoes=[]
        vetor_comparacao=[]

        for linha in range(self.linha,self.linha+3):
            for coluna in range(self.coluna,self.coluna+3):
                if(matriz[linha][coluna].num==0):
                    vetor.append(matriz[linha][coluna])

        var=False
        for i in range(0,len(vetor)):
            for a in range(i+1,len(vetor)):
                if(vetor[i].vetor_possibilidades==vetor[a].vetor_possibilidades):
                    vetor_de_posicoes.append(i)#guardamos as posições dos iguai
                    vetor_de_posicoes.append(a)
                    vetor_comparacao.append(vetor[i].vetor_possibilidades)
                    vetor_comparacao.append(vetor[a].vetor_possibilidades)
                    var=True

        var1=matriz[0][0].verification(vetor_comparacao)
        if (var==True and len(var1)!=0):#se houver vetores iguais
            for i in range(0,len(vetor)):
                if(i not in vetor_de_posicoes):
                    for a in vetor[i].vetor_possibilidades:
                        if(a in vetor_comparacao):
                            vetor[i].vetor_possibilidades.remove(a)
            for i in vetor:
                if(len(i.vetor_possibilidades)==1):
                    i.num=i.vetor_possibilidades[0]
                    i.alterado = True
                    print("linha: ",i.linha+1)
                    print("coluna: ", i.coluna+1)
                    print("número: ", i.num)
                    return True, i.num, i.linha, i.coluna
        return False, 0, 0, 0
