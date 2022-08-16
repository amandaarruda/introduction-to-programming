conjunto_palavras = []
repetem = []
nao_repetem = []
tamanho = 0

for quantidade in range(10):
    entrada = input()
    conjunto_palavras.append(entrada)

for palavra in conjunto_palavras:
    if palavra not in nao_repetem and palavra not in repetem:
        nao_repetem.append(palavra)
    else:
        repetem.append(palavra)
        if (palavra in nao_repetem):
            nao_repetem.remove(palavra)


print('As palavras sao:')
for exclusivas in nao_repetem:
    print(exclusivas)
    for letras in exclusivas:
        tamanho += 1
print(f'A soma do tamanho das palavras é: {tamanho}')
print(f'Estou impressionado, você me venceu, pode ir embora...')
