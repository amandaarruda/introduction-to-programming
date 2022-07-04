#Objetivo: ler 2 valores inteiros e compará-los, imprimindo em ordem crescente
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

if valor1 <= valor2:
    print(valor1, valor2)
else:
    print(valor2, valor1)