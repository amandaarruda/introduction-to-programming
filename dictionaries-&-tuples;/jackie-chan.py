tabela_talismas = {'Carneiro' : {'habilidade': 'adormecer', 'requisito': 'imortalidade'},
    'Cao': {'habilidade': 'imortalidade', 'requisito': 'forca descomunal'},
    'Cobra': {'habilidade': 'invisibilidade', 'requisito': 'equilibrio espiritual'},
    'Coelho': {'habilidade': 'alta velocidade', 'requisito': 'metamorfose animal'},
    'Tigre': {'habilidade': 'equilibrio espiritual', 'requisito': 'adormecer'}, 
    'Dragao': {'habilidade': 'fogo', 'requisito': 'cura'},
    'Cavalo': {'habilidade': 'cura', 'requisito': 'levitacao'}, 
    'Macaco': {'habilidade': 'metamorfose animal', 'requisito': 'raio laser'},
    'Galo': {'habilidade': 'levitacao', 'requisito': 'animar objetos'}, 
    'Porco': {'habilidade': 'raio laser', 'requisito': 'fogo'},
    'Rato': {'habilidade': 'animar objetos', 'requisito': 'alta velocidade'}, 
    'Touro': {'habilidade': 'forca descomunal', 'requisito': 'invisibilidade'}}

qt_talismas = int(input()) 
habilidades_jackie = [] #esta lista contém todas as habilidades dos amuletos que Jackie tem

for quantidade in range(qt_talismas): #descubro e adiiciono as habilidades de jackie na lista
    talisma = input()
    habilidades_jackie.append(tabela_talismas[talisma]['habilidade'])

qt_viloes = int(input())

for quantidade in range(qt_viloes): #para cada talismã do vilão
    talisma_adversario = input()
    requisito = tabela_talismas[talisma_adversario]['requisito'] #descubro qual o requisito dele
    habilidade_equivalente = tabela_talismas[talisma_adversario]['habilidade'] #descubro qual a habiliade dele
    if requisito in habilidades_jackie: #se o requisito for uma das habilidades de jackie
        qt_viloes -= 1 #derroto ele
        habilidades_jackie.append(habilidade_equivalente) #acrescento a habilidade equivalente às minhas
        print(f'Boa! O talisma do {talisma_adversario} vai ser nosso!')
    else:
        for key, values in tabela_talismas.items():
            if requisito == values['habilidade']: #descubro qual talisma tem a habilidade do meu requisito
                print(f'Nao vai dar, melhor ir atras do talisma do {key} antes.')

if qt_viloes <= 0:
    print('Esse plano funciona, vamos agora!')
else:
    print(f'Que mau dia!! Melhor pensarmos num plano de fuga.')
