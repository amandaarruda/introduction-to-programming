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

#maior faturamento 
if faturamento1 > faturamento2 and faturamento1 > faturamento3:
    maior_faturamento = faturamento1

#resultados
