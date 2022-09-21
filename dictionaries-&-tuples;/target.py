jogadores = {} #aqui as keys vão ser o "index" da posição dos jogadores

posicoes = input()
alvo = int(input())

posicoes = posicoes.replace('[', '') #removendo o que não é número
posicoes = posicoes.replace(']', '')
posicoes = [int(numero) for numero in posicoes.split(',')]

for index in range(len(posicoes)): #pego os indexes da lista
    jogadores[index] = int(posicoes[index])  #transformo a key no index e relaciono com o número da lista

for jogador in jogadores.keys():
    for outro_jogador in jogadores.keys():
        if outro_jogador != jogador: #para não ser o mesmo
            if jogadores[jogador] + jogadores[outro_jogador] == alvo: #se a soma deles for o alvo
                if jogadores[jogador] < jogadores[outro_jogador]:
                    jogador_1 = jogador
                    jogador_2 = outro_jogador
                else:
                    jogador_1 = outro_jogador
                    jogador_2 = jogador
                
print([jogador_1, jogador_2])
