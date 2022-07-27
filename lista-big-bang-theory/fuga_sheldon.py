#planetas a serem comparados
quantidade_planetas = int(input())

for i in range(quantidade_planetas):
    
    if (quantidade_planetas < 2):
        print('Número inválido, tente novamente')
        quantidade_planetas = int(input())
    else:
        nome = input()
        raio = float(input())
        massa = float(input())
        temperatura = int(input())

        indice = ((raio + massa + (temperatura/288))/3)
    indice 
