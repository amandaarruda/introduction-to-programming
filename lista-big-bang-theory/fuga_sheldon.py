#planetas a serem comparados
quantidade_planetas = int(input())

while quantidade_planetas < 2:   
    print('Número inválido, tente novamente')
    quantidade_planetas = int(input())

#Variáveis para ajudar na comparação
indice_passado = float('inf')
nome_passado = ''
melhor_planeta = ''
melhor_indice = 0

for i in range(quantidade_planetas):
    nome = input()
    raio = float(input())
    massa = float(input())
    temperatura = int(input())

    indice = ((raio + massa + (temperatura/288))/3)

    if (abs(1-indice) < abs(1-indice_passado)):
        melhor_planeta = nome
        melhor_indice = indice
    else:
        melhor_planeta = nome_passado
        melhor_indice = indice_passado

    #Salvando para a próxima comparação
    indice_passado = melhor_indice
    nome_passado = melhor_planeta

#Resultados
if (melhor_indice == 1):
    print(f'{melhor_planeta} é perfeito!')
elif (melhor_indice < 1):
    print(f'{melhor_planeta} vai dar pro gasto')
elif (melhor_indice > 1):
    print(f'{melhor_planeta} vai ter que servir')
