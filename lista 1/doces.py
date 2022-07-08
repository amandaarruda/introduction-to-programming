#preços
pe_de_moleque = 2
cocada = 5
maca_do_amor = 3

#dados
doce1 = input()
quantidade1 = int(input())
doce2 = input()
quantidade2 = int(input())
doce3 = input()
quantidade3 = int(input())

#faturamentos
faturamento1 = quantidade1 * pe_de_moleque
faturamento2 = quantidade2 * cocada
faturamento3 = quantidade3 * maca_do_amor

#apuração
if (faturamento1 > faturamento2 and faturamento1 > faturamento3):
    maior_faturamento = faturamento1
    melhor_doce = doce1
elif (faturamento2 > faturamento3):
    maior_faturamento = faturamento2
    melhor_doce = doce2
elif (faturamento1 == faturamento2 or faturamento1 == faturamento3 or faturamento3 == faturamento2): #para caso haja valores iguais
    if (quantidade1 > quantidade2 and quantidade1 > quantidade3):
        maior_faturamento = faturamento1
        melhor_doce = doce1
    elif (quantidade2 > quantidade3):
        maior_faturamento = faturamento2
        melhor_doce = doce2
    else:
        maior_faturamento = faturamento3
        melhor_doce = doce3
else:
    maior_faturamento = faturamento3
    melhor_doce = doce3

#resultados
if (maior_faturamento == 0):
    print('A ideia foi peba! Acho melhor encontrar um novo jeito de ganhar dinheiro...')
else:
    print(f'Oxe! Você ganhou {maior_faturamento} reais vendendo {melhor_doce}. O povo gostou, visse?!')
