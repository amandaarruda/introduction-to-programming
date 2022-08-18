matriz = []

maiores_concatenacoes = ['0', '1', '2']
diagonal_principal = []
maior_soma_l = -1
maior_soma_c = -1
maior_soma_d = -1

tamanho = int(input()) #recebe o tamanho da matriz quadrada

for N in range(tamanho): #N é o N que representa NxN da matriz
    linhas = input().split(' ')
    matriz.append(linhas)

for i in range(tamanho): #sendo i um elemento da linha
    for j in range(tamanho): #e j um elemento da coluna
        if(i == j):
            diagonal_principal.append(matriz[i][j]) #determina a diagonal principal

for l in range(tamanho):
    for c in range(tamanho):
        if (c < (tamanho - 1)):
            concatenacao = matriz[l][c] + matriz[l][c+1] #fazendo a concatenação horizontal
            soma = int(matriz[l][c]) + int(matriz[l][c+1]) #fazendo a soma da concatenação
            if (soma > maior_soma_l):
                maior_soma_l = soma
                maiores_concatenacoes[0] = concatenacao

            concatenacao = matriz[c][l] + matriz[c+1][l] #fazendo a concatenação vertical
            soma = int(matriz[c][l]) + int(matriz[c+1][l])
            if (soma > maior_soma_c):
                maior_soma_c = soma
                maiores_concatenacoes[1] = concatenacao

for n in range(len(diagonal_principal)-1): #fazendo a concatenação diagonal
    concatenacao = diagonal_principal[n] + diagonal_principal[n+1]
    soma = int(diagonal_principal[n]) + int(diagonal_principal[n+1])
    if (soma > maior_soma_d):
        maior_soma_d = soma
        maiores_concatenacoes[2] = concatenacao

password = maiores_concatenacoes[0]+maiores_concatenacoes[1]+maiores_concatenacoes[2]
print(f'Falei que era fácil Dustinzinho...\nPegando todas os números que formam as combinações dos pares de cada sentido temos...\nPassword: {password}')
