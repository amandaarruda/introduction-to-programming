#Entradas
nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())

#Colocações
#Primeiro lugar
if (pontuacao_1 < pontuacao_2 and pontuacao_1 < pontuacao_3):
    nome_primeiro = nome_1
    pontuacao_primeiro = pontuacao_1
elif (pontuacao_2 < pontuacao_3 and pontuacao_2 < pontuacao_1):
    nome_primeiro = nome_2
    pontuacao_primeiro = pontuacao_2
elif (pontuacao_1 == pontuacao_2 and pontuacao_1 == pontuacao_3):
    if (nome_1 < nome_2 and nome_1 < nome_3):
        nome_primeiro = nome_1
        pontuacao_primeiro = pontuacao_1
    elif (nome_2 < nome_3 and nome_1 < nome_3):
        nome_primeiro = nome_2
        pontuacao_primeiro = pontuacao_2
    else:
        nome_primeiro = nome_3
        pontuacao_primeiro = pontuacao_3
elif (pontuacao_1 == pontuacao_2 and pontuacao_1 < pontuacao_3):
    if (nome_1 < nome_2):
        nome_primeiro = nome_1
        pontuacao_primeiro = pontuacao_1
    else:
        nome_primeiro = nome_2
        pontuacao_primeiro = pontuacao_2
elif (pontuacao_2 == pontuacao_3 and pontuacao_2 < pontuacao_1):
    if (nome_2 < nome_3):
        nome_primeiro = nome_2
        pontuacao_primeiro = pontuacao_2
    else:
        nome_primeiro = nome_3
        pontuacao_primeiro = pontuacao_3
elif (pontuacao_1 == pontuacao_3 and pontuacao_1 < pontuacao_2):
    if (nome_1 < nome_3):
        nome_primeiro = nome_1
        pontuacao_primeiro = pontuacao_1
    else:
        nome_primeiro = nome_3
        pontuacao_primeiro = pontuacao_3
else:
  nome_primeiro = nome_3
  pontuacao_primeiro = pontuacao_3

#Terceiro lugar
if (pontuacao_1 > pontuacao_2 and pontuacao_1 > pontuacao_3):
    nome_terceiro = nome_1
    pontuacao_terceiro = pontuacao_1
elif (pontuacao_2 > pontuacao_3 and pontuacao_2 > pontuacao_1):
    nome_terceiro = nome_2
    pontuacao_terceiro = pontuacao_2
elif (pontuacao_1 == pontuacao_2 and pontuacao_1 == pontuacao_3):
    if (nome_1 > nome_2 and nome_1 > nome_3):
        nome_terceiro = nome_1
        pontuacao_terceiro = pontuacao_1
    elif (nome_2 > nome_3 and nome_2 > nome_1):
        nome_terceiro = nome_2
        pontuacao_terceiro = pontuacao_2
    else:
        nome_terceiro = nome_3
        pontuacao_terceiro = pontuacao_3
elif (pontuacao_1 == pontuacao_2 and pontuacao_1 > pontuacao_3):
    if (nome_1 > nome_2):
        nome_terceiro = nome_1
        pontuacao_terceiro = pontuacao_1
    else:
        nome_terceiro = nome_2
        pontuacao_terceiro = pontuacao_2
elif (pontuacao_2 == pontuacao_3 and pontuacao_2 > pontuacao_1):
    if (nome_2 > nome_3):
        nome_terceiro = nome_2
        pontuacao_terceiro = pontuacao_2
    else:
        nome_terceiro = nome_3
        pontuacao_terceiro = pontuacao_3
elif (pontuacao_1 == pontuacao_3 and pontuacao_1 > pontuacao_2):
    if (nome_1 > nome_3):
        nome_terceiro = nome_1
        pontuacao_terceiro = pontuacao_1
    else:
        nome_terceiro = nome_3
        pontuacao_terceiro = pontuacao_3
else:
    nome_terceiro = nome_3
    pontuacao_terceiro = pontuacao_3

#Segundo lugar
if (nome_1 != nome_primeiro and nome_1 != nome_terceiro):
    pontuacao_segundo = pontuacao_1
    nome_segundo = nome_1
elif (nome_2 != nome_primeiro and nome_2 != nome_terceiro):
    pontuacao_segundo = pontuacao_2
    nome_segundo = nome_2
elif (nome_3 != nome_primeiro and nome_3 != nome_terceiro):
    pontuacao_segundo = pontuacao_3
    nome_segundo = nome_3
else:
    if (nome_1 == nome_2 and nome_1 == nome_3):
        if (pontuacao_1 != pontuacao_primeiro and pontuacao_1 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_1
            nome_segundo = nome_1
        elif (pontuacao_2 != pontuacao_primeiro and pontuacao_2 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_2
            nome_segundo = nome_2
        elif (pontuacao_3 != pontuacao_primeiro and pontuacao_3 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_3
            nome_segundo = nome_3
    elif (nome_1 == nome_2 and nome_1 != nome_3):
        if (pontuacao_1 != pontuacao_primeiro and pontuacao_1 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_1
            nome_segundo = nome_1
        elif (pontuacao_2 != pontuacao_primeiro and pontuacao_2 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_2
            nome_segundo = nome_2
        elif (pontuacao_3 != pontuacao_primeiro and pontuacao_3 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_3
            nome_segundo = nome_3
    elif (nome_2 == nome_3 and nome_2 != nome_1):
        if (pontuacao_1 != pontuacao_primeiro and pontuacao_1 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_1
            nome_segundo = nome_1
        elif (pontuacao_2 != pontuacao_primeiro and pontuacao_2 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_2
            nome_segundo = nome_2
        elif (pontuacao_3 != pontuacao_primeiro and pontuacao_3 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_3
            nome_segundo = nome_3
    elif (nome_1 == nome_3 and nome_3 != nome_2):
        if (pontuacao_1 != pontuacao_primeiro and pontuacao_1 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_1
            nome_segundo = nome_1
        elif (pontuacao_2 != pontuacao_primeiro and pontuacao_2 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_2
            nome_segundo = nome_2
        elif (pontuacao_3 != pontuacao_primeiro and pontuacao_3 != pontuacao_terceiro):
            pontuacao_segundo = pontuacao_3
            nome_segundo = nome_3

#Resultados
print(f'{nome_primeiro} {pontuacao_primeiro}\n{nome_segundo} {pontuacao_segundo}\n{nome_terceiro} {pontuacao_terceiro}')
