#dono da lista
nome = input()

#quantidade de filmes
quantidade = int(input())

ranking = []

contador = 0

#recebendo os filmes e as notas
while (contador != quantidade):
    sugestao = input().split(' - ') 
    ranking.append(sugestao)

    for ordem in range(len(ranking)-1, 0, -1):
        for nota in range(ordem):
            if (float(ranking[nota][1]) < float(ranking[nota+1][1])):
                ranking[nota], ranking[nota+1] = ranking[nota+1], ranking[nota]

    contador += 1
