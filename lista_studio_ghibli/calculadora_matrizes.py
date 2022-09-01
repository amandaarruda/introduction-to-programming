def multiplicacao_escalar(matriz_1, matriz_2, matriz_resultante, operacoes):
    if operacoes[2] != 'm1' and operacoes[2] != 'm2': #definindo quem é o escalar
        multiplicador = int(operacoes[2])
    elif operacoes[-1] != 'm1' and operacoes[-1] != 'm2':
        multiplicador = int(operacoes[-1])

    if operacoes[2] == 'm1': #definindo quem é a matriz a ser multiplicada
        m = matriz_1
    elif operacoes[2] == 'm2':
        m = matriz_2
    elif operacoes[-1] == 'm1':
        m = matriz_1 
    else:
        m = matriz_2 

    for linha in m: #multiplicando
        l = []
        for elemento in linha:
            valor = (elemento*multiplicador)
            l.append(valor)
        matriz_resultante.append(l)        

def multiplicacao_matrizes(matriz_1, matriz_2, matriz_resultante, operacoes):
    if operacoes[2] != operacoes[-1]:   
        if (operacoes[2] == 'm1'): #definindo quem é o primeiro elemento da multiplicação
            resultado = [[sum(a*b for a,b in zip(m1_row,m2_col)) for m2_col in zip(*matriz_2)] for m1_row in matriz_1]
        else:
            resultado = [[sum(a*b for a,b in zip(m2_row,m1_col)) for m1_col in zip(*matriz_1)] for m2_row in matriz_2]
    else: #caso seja a mesma matriz
        if operacoes[2] == 'm1':
            m = matriz_1
        else:
            m = matriz_2
        resultado = [[sum(a*b for a,b in zip(m_row,m_col)) for m_col in zip(*m)] for m_row in m]

    for r in resultado:
        matriz_resultante.append(r)

def soma_matrizes(matriz_1, matriz_2, matriz_resultante):
    if operacoes[2] != operacoes[-1]: #caso seja uma soma entre duas matrizes diferentes
        resultado = [[matriz_1[i][j] + matriz_2[i][j] for j in range(len(matriz_1[0]))] for i in range(len(matriz_1))]
    else: #caso sejam iguais
        if operacoes[2] == 'm1':
            m = matriz_1
        else:
            m = matriz_2
        resultado = [[m[i][j] + m[i][j] for j in range(len(m[0]))] for i in range(len(m))]

    for r in resultado:
        matriz_resultante.append(r)

def subtracao_matrizes(matriz_1, matriz_2, matriz_resultante):
    if operacoes[2] != operacoes[-1]: #caso seja uma subtração entre duas matrizes diferentes
        if operacoes[2] == 'm1':
            resultado = [[matriz_1[i][j] - matriz_2[i][j] for j in range(len(matriz_1[0]))] for i in range(len(matriz_1))]
        else:
            resultado = [[matriz_2[i][j] - matriz_1[i][j] for j in range(len(matriz_2[0]))] for i in range(len(matriz_2))]
    else: #caso sejam iguais
        if operacoes[2] == 'm1':
            m = matriz_1
        else:
            m = matriz_2
        resultado = [[m[i][j] - m[i][j] for j in range(len(m[0]))] for i in range(len(m))]

    for r in resultado:
        matriz_resultante.append(r)

matriz_1 = []
matriz_2 = []
todas_operacoes = [] #armazenando as operações que serão feitas
tamanho = int(input()) #tamanho da matriz quadrada
for matriz in range(2):
    linhas = []
    for N in range(tamanho): #N representa o NxN
        linha = input().split(' ')
        l = []
        for elemento in linha: #transformando a matriz de str pra int
            numero = int(elemento)
            l.append(numero)
        linhas.append(l)
    if (matriz_1 == []):
        for l in linhas:
            matriz_1.append(l)
    else:
        for l in linhas:
            matriz_2.append(l)
            
qt_operacoes = int(input())
for quantidade in range(qt_operacoes):
    operacao = input().split()
    todas_operacoes.append(operacao)

for operacoes in todas_operacoes:
    matriz_resultante = []
    if (operacoes[3] == '*'):
        multiplicacao_escalar(matriz_1, matriz_2, matriz_resultante, operacoes)
    elif (operacoes[3] == '.'):
        multiplicacao_matrizes(matriz_1, matriz_2, matriz_resultante, operacoes)
    elif (operacoes[3] == '+'):
        soma_matrizes(matriz_1, matriz_2, matriz_resultante)
    else:
        subtracao_matrizes(matriz_1, matriz_2, matriz_resultante)

    if (operacoes[0] == 'm1'):
        matriz_1 = matriz_resultante
    else:
        matriz_2 = matriz_resultante

for linhas in matriz_resultante: #imprimindo o resultado
    print(*linhas)
