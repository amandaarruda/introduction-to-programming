nome_adversario = input() #determinando o vilão

adversarios = {'Vingador': 30, 'Tiamat': 20, 'Vingador das Sombras': 14} #pontos de vida

armas = {'Bobby': 'grande espada', 'Diana': 'dardo', 'Eric': 'grande espada', 'Hank': 'espada', 'Presto': 'cajado', 'Sheila': 'espada', 'Uni': 'chifre'}
armaduras = {'Bobby': 'media', 'Diana': 'leve', 'Eric': 'pesada', 'Hank': 'media', 'Presto': 'leve', 'Sheila': 'leve', 'Uni': 'leve'}

danos_armas = {'chifre': 2, 'cajado': 4, 'espada': 6, 'grande espada': 8, 'dardo': 12}
progresso_armaduras = {'pesada': 0, 'media': 1, 'leve': 3} #classifico o progresso em níveis numéricos

if nome_adversario not in adversarios: #determinando os pontos de vida do vilão
    pontos_de_vida = 9
else:
    pontos_de_vida = adversarios[nome_adversario]

turnos = int(input())

luta = True
while luta:
    combatente = input() #quem vai atacar
    turnos -= 1

    #determinando as operacoes
    if combatente != 'Mestre dos Magos': #dano na vida do vilão
        arma_do_combatente = armas[combatente]
        dano_da_arma = danos_armas[arma_do_combatente]
        pontos_de_vida -= dano_da_arma

        armadura_do_combatente = armaduras[combatente] #dano no turno atual
        progresso_da_armadura = progresso_armaduras[armadura_do_combatente]
        turnos -= progresso_da_armadura

    #possibilidades de acabar o jogo:
    if combatente == 'Mestre dos Magos': #se entrar o mestre dos magos na história
        print('Muito obrigado amigo, que nos vejamos novamente um dia')
        luta = False
    elif pontos_de_vida <= 0: #se o vilão perder a vida
        print(f'{combatente} executou o ultimo golpe em {nome_adversario}, estamos livres!')
        luta = False
    elif turnos <= 0: #se os turnos acabarem
        if pontos_de_vida > 0:
            print(f"Oh nao, {nome_adversario} e muito forte, este e o fim!")
        luta = False
