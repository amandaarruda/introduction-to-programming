#Recebendo o nome da quadrilha
nome_da_quadrilha = input()

#Recebendo os passos
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

passos = passo_1 or passo_2 or passo_3 or passo_4 or passo_5

#definindo a pontuação 
pontuacao = 0

#Regras
#1
#Deve ter 5 passos
conjunto_passos = passo_1 + passo_2 + passo_3 + passo_4 + passo_5
#2
#Caso algum passo seja diferente
if (passos) != ("Cumprimento" or "Balancê" or "Passeio" or "Túnel" or "Serrote" or "Casamento" or "Despedida"):
    pontuacao = 0
#3
#Cumprimento no início
if (passo_1 == "Cumprimento"):
    pontuacao_1 = pontuacao + 100
elif (passo_2 or passo_3 or passo_4 or passo_5 == "Cumprimento"):
    pontuacao_1 = pontuacao + 10
#4
if (passos == "Balancê"):
    teste = pontuacao + 50
#5
if (passos == "Passeio"):
    pontuacao_3 = pontuacao + 70
#6
if (passos == "Serrote"):
    pontuacao_4 = pontuacao + 100
#7
if (passo_5 == "Despedida"):
    pontuacao_5 = pontuacao + 35
#8
if (passos == "Túnel"):
    pontuacao_6 = pontuacao * 0.9
#9 
if (passos == "Casamento"):
    pontuacao_7 = pontuacao * 2

#Definindo a pontuação
pontuacao = pontuacao_1 + teste + pontuacao_3 + pontuacao_4 + pontuacao_5 + pontuacao_6 + pontuacao_7

#Resultados
if (pontuacao == 0):
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada')
elif (pontuacao > 0):
    def conjunto_passos():
        return True
    if conjunto_passos():
            print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao}!')
