qt_entradas = int(input())

cartas_ataque = {} #crio dois dicionários para atribuir os valores de ataque e defesa
cartas_defesa = {}

for n in range(qt_entradas):
    carta = input().split(' ') #recebo tudo já separado

    ataque = int(carta[-2]) #defino quem é o ataque e a defesa, já que são os dois últimos
    defesa = int(carta[-1])
    nome = (' ').join(carta[:-2]) #junto tudo que sobrou pra formar o nome

    cartas_ataque[nome] = ataque #acrescento-os nos dicionários com o nome como key
    cartas_defesa[nome] = defesa

nome_maior_ataque = max(cartas_ataque, key = cartas_ataque.get) #utilizo a função max para achar a key do maior valor
maior_ataque = max(cartas_ataque.values()) #e para achar o maior valor

nome_maior_defesa = max(cartas_defesa, key = cartas_defesa.get)
maior_defesa = max(cartas_defesa.values())

tupla_ataque = (nome_maior_ataque, maior_ataque)
tupla_defesa = (nome_maior_defesa, maior_defesa)

print(f'Carta com maior poder de ataque: {tupla_ataque[0]}\nAtaque: {tupla_ataque[1]}\n\nCarta com maior poder de defesa: {tupla_defesa[0]}\nDefesa: {tupla_defesa[1]}')
