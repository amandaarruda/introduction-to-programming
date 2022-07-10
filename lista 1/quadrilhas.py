#Passos permitidos
passo_A = "Cumprimento"
passo_B = "Balancé"
passo_C = "Passeio"
passo_D = "Túnel"
passo_E = "Serrote"
passo_F = "Casamento"
passo_G = "Despedida"

#Recebendo o nome da quadrilha
nome_da_quadrilha = input()

#Recebendo os passos
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

#Regras
#1
conjunto_passos = passo_1 + passo_2 + passo_3 + passo_4 + passo_5
#2
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5) != (passo_A or passo_B or passo_C or passo_D or passo_E or passo_F or passo_G):
    pontuacao_previa = float(0)
#3
if (passo_1 == passo_A):
    pontuacao_1 = float(100)
elif (passo_2 or passo_3 or passo_4 or passo_5 == passo_A):
    pontuacao_1 = float(10)
#4
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5 == passo_B):
    pontuacao_2 = float(50)
else:
    pontuacao_2 = float(0)
#5
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5 == passo_C):
    pontuacao_3 = float(70)
else:
    pontuacao_3 = float(0)
#6
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5 == passo_E):
    pontuacao_5 = float(100)
else:
    pontuacao_5 = float(0)
#7
if (passo_5 == passo_G):
    pontuacao_6 = float(35)
else:
    pontuacao_6 = float(0)
#8
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5 == passo_D):
#A pontuação 4 precisa ser uma junção de todas as pontuações
    pontuacao_4 = (pontuacao_1 + pontuacao_2 + pontuacao_3 + pontuacao_5 + pontuacao_6)
    pontuacao_previa = pontuacao_4 - (pontuacao_4 * 0.9)
else:
    pontuacao_4 = (pontuacao_1 + pontuacao_2 + pontuacao_3 + pontuacao_5 + pontuacao_6)
    pontuacao_previa = pontuacao_4
#9 
if (passo_1 or passo_2 or passo_3 or passo_4 or passo_5 == passo_F):
    pontuacao = pontuacao_previa * 2
else:
    pontuacao = pontuacao_previa

#A pontuação prévia serve para ajudar a compor a pontuação de acordo com a regra 9
#Definindo a pontuação prévia
pontuacao_previa = float(pontuacao_1 + pontuacao_2 + pontuacao_3 + pontuacao_4 + pontuacao_5 + pontuacao_6)
#Definindo a pontuacao geral
pontuacao = pontuacao_previa

#Resultados
if (pontuacao == 0):
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada')
elif (pontuacao > 0):
    if conjunto_passos : True
    print(f'Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao}!')
