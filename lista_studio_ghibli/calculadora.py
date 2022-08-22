end = False
valores = [] #armazena os valores a serem trabalhados

def calculadora(operacao):
    for quantidade in range(quantidade_numeros - 1): #-1 pra iteração bater certinho
        if (operacao == 'S'):
            resultado = valores[0] + valores[1]
        elif (operacao == 'sub'):
            resultado = valores[0] - valores[1]
        elif (operacao == 'M'):
            resultado = valores [0] * valores[1]
        else:
            resultado = float(valores[0]) / valores[1]
        valores.pop(0) #atualiza o valor
        valores[0] = resultado
    

while (not end):
    operacao = input()
    quantidade_numeros = int(input())
    for quantidade in range(quantidade_numeros):
        valor = int(input())
        valores.append(valor)
    calculadora(operacao)
    print(*valores)
    valores.pop(0) #limpa a lista
    nova_operacao = int(input())
    if (nova_operacao != 1):
        end = True
