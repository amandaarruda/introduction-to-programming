def fatorial(valor):
    if valor > 1:
        return valor * fatorial(valor - 1)
    else:
        return 1

def combinacao_simples(maior): #faz a combinacao simples à medida que transforma os parâmetros para o fatorial
    valor = maior
    global k_fatorial
    k_fatorial = fatorial(valor)

    valor = n
    global n_fatorial
    n_fatorial  = fatorial(valor)

    valor = n-maior
    global n_menos_k_fatorial
    n_menos_k_fatorial = fatorial(valor)

    global num
    num = int(n_fatorial/(k_fatorial*n_menos_k_fatorial))

    return num

letras = input()

maiusculas = []
minusculas = []

for letra in letras: #cria duas listas, uma de maiúsculas e outra de muinúsculas, a fim de contá-las
    if letra.isupper():
        maiusculas.append(letra)
    else:
        minusculas.append(letra)

if len(maiusculas) >= len(minusculas): #verifica qual vai ser o tipo de letra dominante e a quantidade dela na palavra
    maior = len(maiusculas)
    lista_maior = maiusculas #vai ser usado pra descobrir o caractere do planeta
else:
    maior = len(minusculas)
    lista_maior = minusculas 

k_fatorial = 0
n_fatorial = 0
n_menos_k_fatorial = 0

n = len(letras)
num = 0

combinacao_simples(maior)

r = num % maior
caractere = lista_maior[r]

nome = f'{caractere}-{num}'

if caractere.isupper():
    print(f'Morty!!! Morty!!! Vamos para a dimensão {nome}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {nome} para sempre, Morty!!! Wubba lubba dub dub!!!')
else:
    print(f'Oh geez, Rick!!! Eu não sei se ir pra dimensão {nome} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!')
