jogadores = {} #aqui as keys vão ser o "index" da posição dos jogadores

posicoes = list(input())
alvo = int(input())

for elemento in posicoes: #limpando a lista
    if elemento == '[' or elemento == ']' or elemento == ',':
        posicoes.remove(elemento)

for index in range(len(posicoes)): #pego os indexes da lista
    jogadores[index] = int(posicoes[index])  #transformo a key no index e relaciono com o número da lista

for index in range(len(posicoes)):
    if jogadores.get(index) + int(posicoes[index]) == alvo:
        if jogadores.get(index) < int(posicoes[index]):
            jogador_1 = jogadores.get(index)
            jogador_2 = index
        else:
            jogador_2 = jogadores.get(index)
            jogador_1 = index
        resposta = [jogador_1, jogador_2]

print(resposta)
