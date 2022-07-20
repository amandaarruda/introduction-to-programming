#Atributos do atacante
seus_pontos_vida = int(input())
seu_ataque = int(input())
sua_defesa = int(input())
sua_fraqueza = input()
sua_resistencia = input()

#Atributos do adversário
nome_entidade = input()
pontos_vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = input()
resistencia_entidade = input()

###

#Determinando as condições
if (sua_fraqueza != 'fogo' and sua_fraqueza != 'gelo' and sua_fraqueza != 'eletricidade'):
    sua_fraqueza = 'nao tem'

if (sua_resistencia != 'fogo' and sua_resistencia != 'gelo' and sua_resistencia != 'eletricidade'):
    sua_resistencia = 'nao tem'

if (resistencia_entidade != 'fogo'and resistencia_entidade != 'gelo'and resistencia_entidade != 'eletricidade'):
    resistencia_entidade = 'nao tem'

if (fraqueza_entidade != 'fogo' and fraqueza_entidade != 'gelo' and fraqueza_entidade != 'eletricidade'):
    fraqueza_entidade = 'nao tem'

###

#Turno 1
turno_1 = input()

#Definindo o elemento da rodada
elemento_magico = False
if (turno_1 == 'Agi'):
    elemento_magico = True
elif (turno_1 == 'Bufu'):
    elemento_magico = True 
elif (turno_1 == 'Zio'):
    elemento_magico = True

#Caso atinja uma resistência
atingiu_resistencia = False
atingiu_fraqueza = False
game_over = False
if (elemento_magico == True):
    if (turno_1 == 'Agi' and resistencia_entidade == 'fogo') or (turno_1 == 'Bufu' and resistencia_entidade == 'gelo') or (turno_1 == 'Zio' and resistencia_entidade == 'eletricidade'):
        atingiu_resistencia = True
        dano_resistencia_entidade = int((seu_ataque - defesa_entidade) * 0.5)
    #Caso atinja uma fraqueza
    elif (turno_1 == 'Agi' and fraqueza_entidade == 'fogo') or (turno_1 == 'Bufu' and fraqueza_entidade == 'gelo') or (turno_1 == 'Zio' and fraqueza_entidade == 'eletricidade'):
        atingiu_fraqueza = True
        dano_fraqueza_entidade = int((seu_ataque - defesa_entidade) * 1.7)

#Para ataque físico e magias que não atingem nada
atingiu_normal = False
if((atingiu_fraqueza == False and atingiu_resistencia == False) or elemento_magico == False):
    dano_entidade = int(seu_ataque - defesa_entidade)
    atingiu_normal = True

#Mensagens
numero_turno = 1
print(f'Turno: {numero_turno}')

#Variáveis das mensagens
seu_nome = 'São João'
magia = turno_1
adversario = nome_entidade
atacante = seu_nome
ataque = turno_1
atacado = nome_entidade

#Mensagem da fraqueza
if (atingiu_fraqueza == True):
    dano_ataque = dano_fraqueza_entidade
    vida_restante = pontos_vida_entidade - dano_ataque
    if (vida_restante <= 0):
        vida_restante = 0
        game_over = True                
    print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
    pontos_vida_entidade = vida_restante
#Mensagem da resistência
elif (atingiu_resistencia == True):
    dano_ataque = dano_resistencia_entidade
    vida_restante = pontos_vida_entidade - dano_ataque
    if (vida_restante <= 0):
        vida_restante = 0
        game_over = True                
    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
    pontos_vida_entidade = vida_restante
#Outra mensagem
elif (atingiu_normal == True):
    dano_ataque = dano_entidade
    vida_restante = pontos_vida_entidade - dano_ataque
    if (vida_restante <= 0):
        vida_restante = 0
        game_over = True            
    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
    pontos_vida_entidade = vida_restante
###

#Turno 2
if (game_over == True):
    print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
    game_over = False
else:
    if (atingiu_fraqueza == True):
        elemento_magia = fraqueza_entidade
        atacante = nome_entidade
        numero_turno = 2
        print(f'Turno: {numero_turno}')
        print(f'{atacante} teve sua fraqueza em {elemento_magia} acertada, portanto não poderá agir.')
        atingiu_fraqueza = False
    else:
        turno_2 = input()

        #Definindo o elemento da rodada
        elemento_magico_2 = False
        if (turno_2 == 'Agi'):
            elemento_magico_2 = True
        elif (turno_2 == 'Bufu'):
            elemento_magico_2 = True 
        elif (turno_2 == 'Zio'):
            elemento_magico_2 = True

        atingiu_resistencia_2 = False
        atingiu_normal_2 = False

        #Caso atinja uma resistência
        if (elemento_magico_2 == True):
            if (turno_2 == 'Agi' and sua_resistencia == 'fogo') or (turno_2 == 'Bufu' and sua_resistencia == 'gelo') or (turno_2 == 'Zio' and sua_resistencia == 'eletricidade'):
                atingiu_resistencia_2 = True
                dano_resistencia_sua = int((ataque_entidade - sua_defesa) * 0.5)
            #Caso atinja uma fraqueza
            elif (turno_2 == 'Agi' and sua_fraqueza == 'fogo') or (turno_2 == 'Bufu' and sua_fraqueza == 'gelo') or (turno_2 == 'Zio' and sua_fraqueza == 'eletricidade'):
                atingiu_fraqueza = True
                dano_fraqueza_sua = int((ataque_entidade - sua_defesa) * 1.7)
        #Para ataque físico e magias que não atingem nada
        elif ((atingiu_fraqueza == False and atingiu_resistencia_2 == False) or elemento_magico_2 == False):
            dano_seu = int(ataque_entidade - sua_defesa)
            atingiu_normal_2 = True

        #Mensagens
        numero_turno = 2
        print(f'Turno: {numero_turno}')

        magia = turno_2
        atacante = nome_entidade
        ataque = turno_2
        atacado = seu_nome

        #Mensagem da fraqueza
        if (atingiu_fraqueza == True):
            dano_ataque = dano_fraqueza_sua
            vida_restante = seus_pontos_vida - dano_ataque
            if (vida_restante <= 0):
                vida_restante = 0
                game_over = True 
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            #Mensagem da resistência
        elif (atingiu_resistencia_2 == True):
            dano_ataque = dano_resistencia_sua
            vida_restante = seus_pontos_vida - dano_ataque
            if (vida_restante <= 0):
                vida_restante = 0
                game_over = True                     
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        #Outra mensagem
        elif (atingiu_normal_2 == True):
            dano_ataque = dano_seu
            vida_restante = seus_pontos_vida - dano_ataque
            if (vida_restante <= 0):
                vida_restante = 0
                game_over = True                 
            print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')

    #Turno 3
    if (game_over == True):
        print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
        game_over = False
    else:
        if (atingiu_fraqueza == True):
            elemento_magia = sua_fraqueza
            atacante = seu_nome
            numero_turno = 3
            print(f'Turno: {numero_turno}')
            print(f'{atacante} teve sua fraqueza em {elemento_magia} acertada, portanto não poderá agir.')
            print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
        else:
            turno_3 = input()

            #Definindo o elemento da rodada
            elemento_magico_3 = False
            if (turno_3 == 'Agi'):
                elemento_magico_3 = True
            elif (turno_3 == 'Bufu'):
                elemento_magico_3 = True 
            elif (turno_3 == 'Zio'):
                elemento_magico_3 = True

            #Definindo booleanas
            atingiu_resistencia_3 = False
            atingiu_fraqueza = False
            atingiu_normal_3 = False

            #Caso atinja uma resistência
            if (elemento_magico_3 == True): 
                if (turno_3 == 'Agi' and resistencia_entidade == 'fogo') or (turno_3 == 'Bufu' and resistencia_entidade == 'gelo') or (turno_3 == 'Zio' and resistencia_entidade == 'eletricidade'):
                    atingiu_resistencia_3 = True
                    dano_resistencia_entidade = int((seu_ataque - defesa_entidade) * 0.5)
            #Caso atinja uma fraqueza
                elif (turno_3 == 'Agi' and fraqueza_entidade == 'fogo') or (turno_3 == 'Bufu' and fraqueza_entidade == 'gelo') or (turno_3 == 'Zio' and fraqueza_entidade == 'eletricidade'):
                    atingiu_fraqueza = True
                    dano_fraqueza_entidade = int((seu_ataque - defesa_entidade) * 1.7)
            #Para ataque físico e magias que não atingem nada
            elif((atingiu_fraqueza == False and atingiu_resistencia_3 == False) or elemento_magico_3 == False):
                dano_entidade = int(seu_ataque - defesa_entidade)
                atingiu_normal_3 = True

            #Mensagens
            numero_turno = 3
            print(f'Turno: {numero_turno}')

            #Variáveis das mensagens
            magia = turno_3
            atacante = seu_nome
            ataque = turno_3
            atacado = nome_entidade

            #Mensagem da fraqueza
            if (atingiu_fraqueza == True):
                dano_ataque = dano_fraqueza_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0
                    game_over = True                
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            #Mensagem da resistência
            elif (atingiu_resistencia_3 == True):
                dano_ataque = dano_resistencia_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0
                    game_over = True                
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            #Outra mensagem
            elif (atingiu_normal_3 == True):
                dano_ataque = dano_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0
                    game_over = True            
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')

            #Resultados
            if (game_over == True):
                print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
            else:
                print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
