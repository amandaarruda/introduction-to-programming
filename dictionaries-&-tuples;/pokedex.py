pokedex = {} #a pokedex é o dicionário

end = False
while not end:
    try:
        comando = input().split(' ') #cria uma lista a cada comando  

        if comando[0] == 'ADD':
            if comando[1] in pokedex.keys(): #keys são os nomes, "verbetes" do dicionário
                print('Pokémon já adicionado na Pokédex')
            else:
                descricao = input()
                pokedex[comando[1]] = descricao
                print('Pokémon adicionado com sucesso')
        else:
            if comando[1] in pokedex.keys():
                print(pokedex[comando[1]])
            else:
                print('Ainda não há registro desse Pokémon')

    except EOFError:
        end = True #fazendo assim pra não usar break 
