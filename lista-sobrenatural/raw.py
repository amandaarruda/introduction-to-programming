matriz = []

somas_linhas = []
somas_colunas = []
somas_diagonal_principal = []
maiores_somas = []
diagonal_principal = []
maior_soma_l = 0
maior_soma_c = 0
maior_soma_d = 0

tamanho = int(input()) #recebe o tamanho da matriz quadrada

for N in range(tamanho): #N é o N que representa NxN da matriz
    linhas = input().split(' ')
    matriz.append(linhas)

for i in range(tamanho): #sendo i um elemento da linha
    for j in range(tamanho): #e j um elemento da coluna
        if(i == j):
            diagonal_principal.append(matriz[i][j])

for l in range(tamanho - 1):
    for c in range(tamanho - 1):
        soma = matriz[l][c] + matriz[l][c+1] #fazendo a soma horizontal
        somas_linhas.append(soma)
        soma = matriz[c][l] + matriz[c+1][l] #fazendo a soma vertical
        somas_colunas.append(soma)

for somas in somas_linhas: #definindo a maior soma das linhas
    if (somas > maior_soma_l):
        maior_soma_l = soma
maiores_somas.append(maior_soma_l)

for somas in somas_colunas: #definindo a maior soma das colunas
    if (somas > maior_soma_c):
        maior_soma_c = soma
maiores_somas.append(maior_soma_c)

for somas in somas_diagonal_principal: #definindo a maior soma da diagonal
    if (somas > maior_soma_d):
        maior_soma_d = soma
maiores_somas.append(maior_soma_d)

password = maiores_somas.join()
