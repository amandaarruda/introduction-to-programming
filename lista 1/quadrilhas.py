#Recebendo o nome da quadrilha
nome_da_quadrilha = input()

#Passos permitidos
passo_A = "Cumprimento"
passo_B = "Balancê"
passo_C = "Passeio"
passo_D = "Túnel"
passo_E = "Serrote"
passo_F = "Casamento"
passo_G = "Despedida"

#Recebendo os passos
passo_1 = input()
passo_2 = input()
passo_3 = input()
passo_4 = input()
passo_5 = input()

#Definindo a pontuação 
pontuacao = float(0)

#Declarando o casamento e os passos diferentes
casamento = False
diferente = False

#Regras
#1
#Deve ter 5 passos
conjunto_passos = passo_1 + passo_2 + passo_3 + passo_4 + passo_5
#Regras que dependem de cada passo:
#Passo 1
#Regra do Cumprimento
if (passo_1 == passo_A):
    pontuacao = 100
#Regra do Balancê
elif (passo_1 == passo_B):
    pontuacao = 50
#Regra do Passeio
elif (passo_1 == passo_C):
    pontuacao = 70
#Regra do Serrote
elif (passo_1 == passo_E):
    pontuacao = 100
#Regra da Despedida
elif (passo_1 == passo_G):
    pontuacao = 0
#Regra do Túnel
elif (passo_1 == passo_D):
    pontuacao = pontuacao * 0.9
#Regra do Casamento
elif (passo_1 == passo_F):
    casamento = True
#Passo diferente
elif (passo_1 != passo_A, passo_B, passo_C, passo_D, passo_E, passo_F, passo_G):
    diferente = True
else:
    pontuacao = 0

#Passo 2
#Regra do Cumprimento
if (passo_2 == passo_A):
    pontuacao += 10
#Regra do Balancê
elif (passo_2 == passo_B):
    pontuacao += 50
#Regra do Passeio
elif (passo_2 == passo_C):
    pontuacao += 70
#Regra do Serrote
elif (passo_2 == passo_E):
    pontuacao += 100
#Regra da Despedida
elif (passo_2 == passo_G):
    pontuacao = pontuacao
#Regra do Túnel
elif (passo_2 == passo_D):
    pontuacao *= 0.9
#Regra do Casamento
elif (passo_2 == passo_F):
    casamento = True
#Passo diferente
elif (passo_2 != passo_A, passo_B, passo_C, passo_D, passo_E, passo_F, passo_G):
    diferente = True
else:
    pontuacao = 0

#Passo 3
#Regra do Cumprimento
if (passo_3 == passo_A):
    pontuacao += 10
#Regra do Balancê
elif (passo_3 == passo_B):
    pontuacao += 50
#Regra do Passeio
elif (passo_3 == passo_C):
    pontuacao += 70
#Regra do Serrote
elif (passo_3 == passo_E):
    pontuacao += 100
#Regra da Despedida
elif (passo_3 == passo_G):
    pontuacao = pontuacao
#Regra do Túnel
elif (passo_3 == passo_D):
    pontuacao *= 0.9
#Regra do Casamento
elif (passo_3 == passo_F):
    casamento = True
#Passo diferente
elif (passo_3 != passo_A, passo_B, passo_C, passo_D, passo_E, passo_F, passo_G):
    diferente = True
else:
    pontuacao = 0

#Passo 4
#Regra do Cumprimento
if (passo_4 == passo_A):
    pontuacao += 10
#Regra do Balancê
elif (passo_4 == passo_B):
    pontuacao += 50
#Regra do Passeio
elif (passo_4 == passo_C):
    pontuacao += 70
#Regra do Serrote
elif (passo_4 == passo_E):
    pontuacao += 100
#Regra da Despedida
elif (passo_4 == passo_G):
    pontuacao = pontuacao
#Regra do Túnel
elif (passo_4 == passo_D):
    pontuacao *= 0.9
#Regra do Casamento
elif (passo_4 == passo_F):
    casamento = True
#Passo diferente
elif (passo_4 != passo_A, passo_B, passo_C, passo_D, passo_E, passo_F, passo_G):
    diferente = True
else:
    pontuacao = 0

#Passo 5
#Regra do Cumprimento
if (passo_5 == passo_A):
    pontuacao += 10
#Regra do Balancê
elif (passo_5 == passo_B):
    pontuacao += 50
#Regra do Passeio
elif (passo_5 == passo_C):
    pontuacao += 70
#Regra do Serrote
elif (passo_5 == passo_E):
    pontuacao += 100
#Regra da Despedida
elif (passo_5 == passo_G):
    pontuacao += 35
#Regra do Túnel
elif (passo_5 == passo_D):
    pontuacao *= 0.9
#Regra do Casamento
elif (passo_5 == passo_F):
    casamento = True
#Passo diferente
elif (passo_5 != passo_A, passo_B, passo_C, passo_D, passo_E, passo_F, passo_G):
    diferente = True
else:
    pontuacao = 0


#Continuando a regra do Casamento
if (casamento == True):
    pontuacao = pontuacao * 2


#Resultados
if (diferente == True):
    print(f'Poxa, {nome_da_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
elif (pontuacao > 0):
    def conjunto_passos():
        return True
    if conjunto_passos():
            print(f"Parabéns, {nome_da_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao:.1f}!")
