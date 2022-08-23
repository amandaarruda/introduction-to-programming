def interceptador(mensagem):
    if ('crcrcrcrcr' in mensagem or 'uuuuuuuoooooo' in mensagem or 'ooooooeeeeeeee' in mensagem):
        verificador[0] = 1
    
    if ('ppprrrrrooon' in mensagem or 'tutututututututu' in mensagem or 'eeeeeeeeoooooo' in mensagem):
        verificador[1] = 1

    if (verificador[0] == 0 and verificador[1] == 0):
        verificador[2] = 1

verificador = [0, 0, 0] #funciona como uma lista de booleanas. A primeira posição checa insetos, a segunda, aviões e a terceira checa se nenhum dos dois foi identificado

while (verificador[2] == 0): #enquanto ainda há mensagens de insetos ou aviões
    mensagem = input().split(' ')
    interceptador(mensagem)

    if (verificador[0] == 1 and verificador[1] == 0): #se for inseto
        print('É apenas o Mar Podre se comunicando, podemos ficar tranquilos, por enquanto…')
    elif (verificador[0] == 0 and verificador[1] == 1): #se for avião
        print('São sinais de aeronaves estrangeiras! Devemos preparar nossas defesas??')
    elif (verificador[0] == 1 and verificador[1] == 1): #se for os dois
        print('A transmissão sugere que tropas estrangeiras e as criaturas do Mar Podre irão se confrontar! Precisamos impedi-los antes que mais mortes desnecessárias ocorram!')
    
    if (verificador[2] == 0):
        verificador = [0, 0, 0] #se ainda não tiver acabado, reseta para uma próxima rodada
else:
    print('Não é possível determinar a origem da transmissão… Isso deverá levar mais algum tempo.')
