participanteBR = input('Digite nome do brasileiro: ')
participanteEN = input("Digite o nome do americano: ")

valorBR = float(input(f"Digite os db de {participanteBR}: "))
print(f'A reação à piada de {participanteBR} foi de {valorBR:.2f} dB')
valorEN = float(input(f"Digite os db de {participanteEN}: "))
print(f'A reação à piada de {participanteEN} foi de {valorEN:.2f} dB')

if (valorBR > valorEN):
    print(f'O GRANDE VENCEDOR É\n{participanteBR}\n{valorBR:.2f} dB')
    taxa = float(input('Digite a taxa do dólar: '))
    print('R$', 10*taxa)
elif (valorBR == valorEN):
    print(f'{participanteBR} e {participanteEN} empataram!')
else:
    print(f'O GRANDE VENCEDOR É\n{participanteEN}\n{valorEN:.2f} dB')
    print('U$', valorEN)
