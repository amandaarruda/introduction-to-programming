#número do local do mapa
X = int(input())

#progresso
P = int(input())

pontuacao = 0 

#Calculando a pontuacao
while (P >= 0):
    P = pontuacao+(P*((1+P)/2))
    pontuacao = P
    P = int(input())
else:
    if (pontuacao < X):
        print('Ainda falta um pouco...')
    elif (pontuacao == X):
        print('Parabéns!!! Você é o mais inteligente')
    elif (pontuacao > X):
        if (pontuacao < (X*20)):
            print('Parece que o gêniozinho passou um pouco do local...')
        elif ((X*20) <= pontuacao <= (X*100)):
            print('Acho que sua grande inteligência fez você se perder um pouco no caminho, onde estamos?')
        elif (pontuacao > (X*100)):
            print('Hum... acho que o gêniozinho não tem mesmo doutorado ein...')
