#Definir o dia
X = int(input())

#Resultados dos valores
if (X % 2 == 0 and 17 < X <= 26 and X != 20):
    print('Um de seus cantores favoritos cantará nesse dia, portanto gaste até, no máximo, 400 reais!')
elif (X % 2 != 0 and 17 <= X < 26):
    print('Nenhum cantor favorito seu cantará nesse dia, portanto gaste até, no máximo, 200 reais!')
else:
    print('Você escolheu um dia que não irá acontecer nenhum show, tente novamente!')