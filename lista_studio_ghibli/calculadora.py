def calculadora(operacao, quantidade_numeros):

    novo_valor_soma = 0
    novo_valor_mult = 1

    for quantidade in range(quantidade_numeros):
        valor = int(input())

        if (operacao == 'S'):
            novo_valor_soma = novo_valor_soma + valor
        elif (operacao == 'sub'):
            if (quantidade == 0):
                proximo_valor = int(input())
                novo_valor_soma = valor - proximo_valor
            else:
                novo_valor_soma = novo_valor_soma - valor
        elif (operacao == 'M'):
            novo_valor_mult = novo_valor_mult * valor
        else:
            if (quantidade == 0):
                proximo_valor = float(input())
                novo_valor_mult = float(valor) / proximo_valor
            else:
                novo_valor_mult = novo_valor_mult / float(valor)

    if (operacao == 'S' or operacao == 'sub'):
        print(f'{novo_valor_soma}')
    else:
        print(f'{novo_valor_mult}')                  

nova_operacao = '1'

while (nova_operacao == '1'):
    operacao = input()
    quantidade_numeros = int(input())
    calculadora(operacao, quantidade_numeros)

    nova_operacao = input()
