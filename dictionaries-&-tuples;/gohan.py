qt_pedras = int(input())
pedras_gohan = input().split(' ')
pedras_piccolo = input().split(' ')

ordenada_gohan = sorted(pedras_gohan)
ordenada_piccolo = sorted(pedras_piccolo)

distancia_gohan = {}
distancia_piccolo = {}

for quantidade in range(qt_pedras): #crio os dicionários
    distancia_gohan[quantidade] = ordenada_gohan[quantidade]
    distancia_piccolo[quantidade] = ordenada_piccolo[quantidade]

if distancia_piccolo == distancia_gohan:
    print('Dale Gohan!')
else:
    print('Ih, nao foi agora, Gohan! Vamos tentar de novo semana que vem.')
