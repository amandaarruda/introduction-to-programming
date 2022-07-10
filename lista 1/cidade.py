#Informações
cidade1 = input()
nota1 = float(input())
distancia1 = float(input())

cidade2 = input()
nota2 = float(input())
distancia2 = float(input())

cidade3 = input()
nota3 = float(input())
distancia3 = float(input())

#Definindo a nota mais alta
if (nota1 > nota2 and nota1 > nota3):
    melhor_cidade = cidade1
    melhor_nota = nota1
elif (nota2 > nota3):
    melhor_cidade = cidade2
    melhor_nota = nota2
elif (nota1 == nota2 or nota1 == nota3 or nota3 == nota2):
    if (distancia1 < distancia2 and distancia1 < distancia3):
        melhor_cidade = cidade1
        melhor_nota = nota1
    elif (distancia2 < distancia3):
        melhor_cidade = cidade2
        melhor_nota = nota2
    else:
        melhor_cidade = cidade3
else:
    melhor_cidade = cidade3
    melhor_nota = nota3

#Resultados
if (4 <= melhor_nota <= 5):
    print('melhor_cidade')
else:
    print('Nota mínima não atingida')
