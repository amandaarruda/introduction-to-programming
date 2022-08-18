mochilas = []
tamanhos = [] #quantidades de elementos que as mochilas aguentam
vagas = [] #espaços disponíveis nas mochilas
nome_index = -1
acao = ''

quantidade_mochilas = int(input())
nomes = input().split(' ')

for quantidade in range(quantidade_mochilas):
    tamanho = int(input()) #espaço da mochila
    tamanhos.append(tamanho) #lista com todos os espaços
    mochilas.append(['Lanterna', 'Omega 3 da top therm']) #lista das mochilas
    vagas.append(tamanho - 2) #preenche as duas vagas da lanterna e do ômega 3

itens_adicionados = int(input()) #quantidade de itens a serem adicionados

for item in range(itens_adicionados):
    nome = input() #nome do item
    mochila = int(input()) #especifica a mochila
    if (vagas[mochila] > 0): #se a mochila tiver vaga
        mochilas[mochila].append(nome) #adiciona o item na mochila
        vagas[mochila] = vagas[mochila] - 1 #atualiza a qt. de vagas disponíveis
    else:
        print('Mochila cheia. Não vai dar para levar.')

while (acao != 'CHEGAMOS NO CIN!'): #determinando as ações
    acao = input()
    if (acao == 'Tirar da mochila'):
        elemento = input()
        mochila = int(input())
        if (elemento in mochilas[mochila]):
            mochilas[mochila].remove(elemento)
            vagas[mochila] += 1
            print(f'{elemento} usado com sucesso da mochila {mochila}.')
        else:
            print(f'Você não tem {elemento} na mochila {mochila}.')
    elif (acao == 'Guardar na mochila'):
        elemento = input()
        mochila = int(input())
        if (vagas[mochila] > 0):
            mochilas[mochila].append(elemento)
            vagas[mochila] -= 1
            print(f'{elemento} adicionado na mochila {mochila}.')
        else:
            print(f'Mochila {mochila} cheia!')
    elif (acao != 'CHEGAMOS NO CIN!'):
        print('Ação inválida.')
else:
    for mochila in range(len(mochilas)): #imprimindo os itens das mochilas
        print(f'Mochila de {nomes[mochila]} chegou assim:')
        for item_final in range(len(mochilas[mochila])):
            print(mochilas[mochila][item_final])
