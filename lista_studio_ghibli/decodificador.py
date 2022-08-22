elementos_ascii = []
mensagem_decodificada = []
indecodificavel = False
mensagem_codificada = input().split(' ')

def decodificador(mensagem):
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
        indecodificavel = True
    if not indecodificavel:
        elementos_ascii.append(valor_ascii)

for mensagem in mensagem_codificada:
    decodificador(mensagem)

for elemento in elementos_ascii:
    caractere = chr(elemento)
    mensagem_decodificada.append(caractere)

if (not indecodificavel):
    mensagem_final = ('').join(mensagem_decodificada)
    print(mensagem_final)
else:
    print('Infelizmente os números nao dizem nada')
