frascos = int(input())
entradas = int(input())

elementos = [] #todos os elementos
quantidades = [] #quantidades dos elementos
necessario = [] #elementos necessarios
contador = 0
index = -1

for disponiveis in range(entradas):
    informacoes = input().split(' ') #recebe as entradas separadamente e categoriza
    (elemento, quantidade) = informacoes
    elementos.append(elemento)
    quantidades.append(int(quantidade))

for rodada in range(len(quantidades)): #analisa se a soma é compatível na ordem em que vem
    contador += quantidades[rodada]
    necessario.append(elementos[0])
    elementos.pop(0)
    if (contador == frascos):
        break

while contador != frascos and quantidades != []: #analisa nas outras sublistas
    contador = 0
    quantidades.pop(0)
    necessario.pop(0)
    for rodada in range(len(quantidades)): #corrigir dps a excecao
        contador += quantidades[rodada]
        if quantidades[rodada] == frascos: #caso um elemento só tenha a quantidade
            necessario = [necessario[0]]
            contador = quantidades[0]
            break

if (contador == frascos):
    elementos_necessarios  = (' ').join(necessario)
    print(f'Vencemos a batalha e a humanidade foi restaurada! {elementos_necessarios} foram usados para deszumbificar')
else:
    print('Estou sentido algo estranho... será que também vou virar zumbi?')
