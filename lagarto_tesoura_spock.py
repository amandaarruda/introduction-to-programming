#Entrada
N = int(input()) #número de rodadas

#inicializando variáveis
vitorias_sheldon = 0
vitorias_raj = 0
empates = 0

while (N > 0):
        escolha_sheldon = input()
        escolha_raj = input()

        #analisando possibilidades
        sheldon_ganha = False
        raj_ganha = False
        empate = False

        if (escolha_sheldon == 'lagarto' and escolha_raj == 'spock') or (escolha_sheldon == 'spock' and escolha_raj == 'tesoura') or (escolha_sheldon == 'tesoura' and escolha_raj == 'lagarto'):
            sheldon_ganha = True
        elif (escolha_raj == 'lagarto' and escolha_sheldon == 'spock') or (escolha_raj == 'spock' and escolha_sheldon == 'tesoura') or (escolha_raj == 'tesoura' and escolha_sheldon == 'lagarto'):
            raj_ganha = True
        elif (escolha_raj == escolha_sheldon):
            empate = True

        #calculando resultados
        if (not sheldon_ganha):
            vitorias_sheldon += 1
        elif (not raj_ganha):
            vitorias_raj += 1
        elif (not empate):
            empates += 1

        N -= 1

if (vitorias_sheldon > vitorias_raj):
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif (vitorias_raj > vitorias_sheldon):
    print("ENGOLE ESSA, SHELDON!")
else:
    print("Oh não, precisamos de outra rodada.")
