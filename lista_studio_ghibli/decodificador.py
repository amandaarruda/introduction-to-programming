def decodificador(mensagem): # a função transforma o número pro correspondente ascii
    if (0 <= int(mensagem) < 26):
        valor_ascii = int(mensagem) + 97
    elif (26 <= int(mensagem) < 50):
        valor_ascii = int(mensagem) + 71
    elif (50 <= int(mensagem) < 76):
        valor_ascii = int(mensagem) + 15
    elif (76 <= int(mensagem) < 100):
        valor_ascii = int(mensagem) - 11
    elif (int(mensagem) == 100):
        valor_ascii = 32
    else:
        valor_ascii = 33 #O valor 33 serve apenas para sinalizar que o código não diz nada, já que não deveria ser considerado
    elementos_ascii.append(valor_ascii)

elementos_ascii = [] #armazena os valores convertidos
mensagem_decodificada = [] #armazena os caracteres convertidos
mensagem_codificada = input().split(' ') #recebe os números originais

for mensagem in mensagem_codificada:
    decodificador(mensagem)

for elemento in elementos_ascii:
    caractere = chr(elemento) #converte
    mensagem_decodificada.append(caractere)

if (33 not in elementos_ascii):
    mensagem_final = ('').join(mensagem_decodificada)
    print(mensagem_final)
else:
    print('Infelizmente os números nao dizem nada')
