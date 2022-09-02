def contador_parenteses_abertos(expressao, aberto):
    if aberto in expressao:
        expressao.remove(aberto) #se ) estivar na expressão, removo ele da lista
        return contador_parenteses_abertos(expressao, aberto) + 1 #acrescenta 1 no contador e reinicia a contagem
    else: 
        return 0 #caso base

def contador_parenteses_fechados(expressao, fechado):
    if fechado in expressao:
        expressao.remove(fechado)
        return contador_parenteses_fechados(expressao, fechado) + 1
    else: 
        return 0

aberto = '('
fechado = ')'

rodadas = int(input())
for rodada in range(rodadas):

    expressao = list(input()) #transformo a string em uma lista

    parenteses_abertos = contador_parenteses_abertos(expressao, aberto)
    parenteses_fechados = contador_parenteses_fechados(expressao, fechado)

    if (parenteses_abertos == parenteses_fechados):
        print('Essa sentença está com os parênteses balanceados, HOORAY!')
    elif (parenteses_abertos > parenteses_fechados):
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    elif (parenteses_fechados > parenteses_abertos):
        print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
