nome = input() #dono da lista

quantidade = int(input()) #quantidade de filmes
ranking = []
contador = 0

#recebendo os filmes e as notas
while (contador != quantidade):
    sugestao = input().split(' - ') #recebendo já separado pra analisar só as notas
    ranking.append(sugestao)

    for ordem in range(len(ranking)-1, 0, -1): #criando manualmente o bubble sort
        for nota in range(ordem):
            if (float(ranking[nota][1]) < float(ranking[nota+1][1])):
                ranking[nota], ranking[nota+1] = ranking[nota+1], ranking[nota]

    contador += 1
else:
    print(f'Os filmes sugeridos por {nome} são:')

    unpacked_ranking = [item for filme in ranking for item in filme] #transformando a lista de listas em uma lista só

    while (contador != 0):
        print(f'{unpacked_ranking[0]} - {unpacked_ranking[1]}')
        unpacked_ranking.pop(0)
        unpacked_ranking.pop(0)
        contador -=1
