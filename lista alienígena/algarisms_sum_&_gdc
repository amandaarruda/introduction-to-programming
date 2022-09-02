def soma_digitos(n):
    if (n == 0):
        return 0 #quando chega a 0, não há
    else:
        return (n % 10) + soma_digitos(n // 10) #o resto do número é o dígito mais a direita e a divisão inteira do número são os números restantes a serem somados

def mdc(a, b):
    if (b == 0):
        return a #sendo b 0, o MDC é o próprio a
    else:
        return mdc(b, a%b) #usando o algoritmo de euclides   
    
for rodada in range(3):
    n = int(input())
    soma_digitos(n)
    if (rodada == 0):
        a = soma_digitos(n)
    elif (rodada == 1):
        b = soma_digitos(n)
    else:
        c = soma_digitos(n)

a = mdc(a, b)
b = c #atualizando as variáveis para fazer com o próximo número, já que a função faz de 2 em 2
resultado = mdc(a, b)

print(f'O MDC obtido é: {resultado}')
