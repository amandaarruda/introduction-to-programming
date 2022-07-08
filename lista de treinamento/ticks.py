#Quantidade de dias da vida real e de casas na vila
D = int(input())
C = int(input())

#ticks a cada 1 min no jogo
ticks_min = 1200

#o tempo de jogo por dia é de 180 min, mas ele só constroi durante 90 min
#tempo total de jogo
tempo_total = 90 * D

#minutos gastos em cada casa
tempo_casa = tempo_total / C

#Quantidade de ticks gasta em cada casa
total_ticks = tempo_casa * ticks_min
print(int(total_ticks))
