resultados = input().split(' ')
alteracoes = input().split(' ')

iteracao = -1 #para facilitar o index
rodada = -1 #para calcular qual a ordem do terço
pontuacao = 0 #para calcular a pontuação do terço verdadeira
pontuacao_falsa = 0 #para calcular a pontuacao total do sapo
pontuacoes = [] #para calcular a pontuação total do sapo

vitorias = 0
empates = 0

for resultado in resultados: #calcula quanto seria a pontuacao se o resultado do sapo fosse o correto
    iteracao += 1
    if (resultados[iteracao] == 'V'):
        pontuacao_falsa += 3
    elif (resultados[iteracao] == 'E'):
        pontuacao_falsa += 1

iteracao = -1 #"zerando" a iteração

for alteracao in alteracoes: #para corrigir os resultados
    iteracao += 1
    if (alteracao == '1'):
        if (resultados[iteracao] == 'V'):
            resultados[iteracao] = 'E'
            print('O maldito sapo interferiu no resultado! O que parecia uma vitória garantida terminou em um empate.')
        elif (resultados[iteracao] == 'E'):
            resultados[iteracao] = 'D'
            print('O anfíbio da maldição interferiu no resultado! Um empate tranquilo virou uma frustrante derrota.')
        else:
            print('O que já era ruim, se tornou uma humilhante derrota. Desgraçado desse sapo!')

tercos = [[resultados[0:4]], [resultados[4:8]], [resultados[8:]], '0'] #definindo os terços

for terco in tercos: 
    pontuacoes.append(pontuacao) #definindo uma lista para somar as pontuações dos tercos
    pontuacao = 0
    for resultados in terco:
        rodada += 1
        if (rodada > 0): #dando o resultado do terço
            if (pontuacoes[rodada] > 7):
                print(f'A pontuação na {rodada}ª fatia de 4 jogos está com uma gordurinha de {pontuacoes[rodada] - 7} pontos.')
            elif (pontuacoes[rodada] < 7):
                print(f'A pontuação na {rodada}ª fatia de 4 jogos está abaixo da planejada em {7 - pontuacoes[rodada]} pontos.')
            else:
                print(f'A pontuação na {rodada}ª fatia de 4 jogos está dentro do planejado.')
        for resultado in resultados: #somando as pontuações nos terços
            if (resultado == 'V'):
                vitorias += 1
                pontuacao += 3
            elif (resultado == 'E'):
                pontuacao += 1
                empates += 1

pontuacao_total = sum(pontuacoes)
pontos_perdidos = abs(pontuacao_total - pontuacao_falsa)

if (pontos_perdidos > 0):
    print(f'A maldição do sapo fez o Vascão perder {pontos_perdidos} pontos. Um número preocupante, que pode fazer diferença.')
else:
    print('A maldição parece que não teve impacto relevante! Não houve nenhuma perda de pontos.')

if (pontuacao_total >= 21):
    print(f'Na reta final do campeonato, o Vasco garantiu um total de {pontuacao_total} pontos, com {vitorias} vitórias, {empates} empates e {12-  (vitorias + empates)} derrotas, e alcançou o tão esperado acesso. O Clube do Fomento Corporal vibra num SJ lotado!')
else:
    print(f'Na reta final do campeonato, o Vasco fez somente {pontuacao_total} pontos, com {vitorias} vitórias, {empates} empates e {12-  (vitorias + empates)} derrotas, e não conseguiu o acesso. Mais um ano de série B e sofrimento. Mob, o clube e a torcida estão completamente desolados.')
