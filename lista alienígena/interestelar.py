def letra_numero(letra):
    global posicao
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    posicao = letras.index(letra) #a posição é igual ao index da lista de letras acima
    return posicao

def numero_letra(valor):
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letras[valor] # o valor é o index

def mod_letra(posicao): #o mod da letra é o resto da sua posição por 11
    global mod
    mod = posicao % 11
    return mod

def fatorial(mod): #a posição fatorial é a posição obtida pela letra - 1
    if (mod > 1):
        return (mod) * fatorial(mod - 1)
    elif (mod >= 0):
        return 1

def fibonacci(mod):
    if mod <= 1:
        return mod
    else:
        return fibonacci(mod - 1) + fibonacci(mod - 2)

posicao = 0
lista_fibonacci = []
lista_fatorial = []
senha_final = []
senhas_finais = []
numeros_sem_conversao = []
pedaco_convertido = []
existe_senha = False

senha = input()
quantidade = int(input())
for palavras in range(quantidade):
    palavra = input()
    for letra in palavra:
        letra_numero(letra) #transformo a letra em numero
        mod_letra(posicao) #tiro o mod da posição da letra

        for i in range(mod): #crio a lista de fibonacci e a de fatorial de acordo com o mod
            lista_fibonacci.append(fibonacci(i))
            lista_fatorial.append(fatorial(i))

        if mod == 0:
            senha_final.append('1')
        elif mod % 2 != 0:
            for x in range(len(lista_fibonacci)):
                numeros_sem_conversao.append(lista_fibonacci[x] * lista_fatorial[x]) #multiplicando os valores das listas
        else:
            for x in range(len(lista_fibonacci)):
                numeros_sem_conversao.append(lista_fibonacci[x] + lista_fatorial[x]) #somando os valores das listas

        for valor in numeros_sem_conversao:
            pedaco_convertido.append(numero_letra(valor % 26)) #criando um pedaço pra cada letra
        senha_final.append(('').join(pedaco_convertido)) #junto o resultado de uma letra para criar uma n-upla com o resultado de todas

        lista_fatorial = [] #limpo as listas para uma nova iteração
        lista_fibonacci = []
        pedaco_convertido = []
        numeros_sem_conversao = []
    senhas_finais.append(('').join(senha_final)) #junto o resultado da palavra
    if senhas_finais[0] == senha:
        existe_senha = True
    senha_final = [] #limpo as senhas
    senhas_finais = []

if existe_senha:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais.')
