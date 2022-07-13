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

if (sua_fraqueza != 'fogo' or sua_fraqueza != 'gelo' or sua_fraqueza != 'eletricidade'):
    sua_fraqueza = ''

if (sua_resistencia != 'fogo' or sua_resistencia != 'gelo' or sua_resistencia != 'eletricidade'):
    sua_resistencia = ''

if (resistencia_entidade != 'fogo' or resistencia_entidade != 'gelo' or resistencia_entidade != 'eletricidade'):
    resistencia_entidade = ''

if (fraqueza_entidade != 'fogo' or fraqueza_entidade != 'gelo' or fraqueza_entidade != 'eletricidade'):
    fraqueza_entidade = ''

#Condições
if (sua_defesa < ataque_entidade and defesa_entidade < seu_ataque):
    if (sua_resistencia != sua_fraqueza and resistencia_entidade != fraqueza_entidade):
        #Ataques
        ataque_fisico = 'Ataque Físico'

        Agi = 'fogo'
        Bufu = 'gelo'
        Zio = 'eletricidade'

        ataque_magia = Agi, Bufu, Zio

        #Atributos turnos
        turno_1 = input()
        turno_2 = input()
        turno_3 = input()

        #Turnos
        numero_turno = 1
        print(f'Turno: {numero_turno}')
        dano_geral = int(seu_ataque - ataque_entidade)
        if (turno_1 == ataque_magia):
            if (ataque_magia == resistencia_entidade):
                dano_geral *= 0.5
                #Resultados
                atacante = 'São João'
                magia = ataque_magia
                dano_ataque = dano_geral
                atacado = nome_entidade
                vida_restante = (pontos_vida_entidade - dano_geral)
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            elif (ataque_magia == fraqueza_entidade):
                dano_geral *= 1.7
                #Resultados
                seu_nome = 'São João'
                magia = ataque_magia
                dano_ataque = dano_geral
                adversario = nome_entidade
                vida_restante = (pontos_vida_entidade - dano_geral)
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
        else:
            dano_geral = dano_geral
            #Resultado
            atacante = 'São João'
            ataque = seu_ataque 
            dano_ataque = dano_geral
            atacado = nome_entidade
            vida_restante = (pontos_vida_entidade - dano_geral)
            print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')


        numero_turno = 2
        if (dano_geral >= pontos_vida_entidade):
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        elif (dano_geral >= seus_pontos_vida):
            adversario = nome_entidade
            print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
        elif (turno_2 == ataque_magia == fraqueza_entidade):
            #Resultado
            atacante = nome_entidade
            elemento_magia = fraqueza_entidade
            print(f'{atacante} teve sua fraqueza em {elemento_magia} acertada, portanto não poderá agir.')
            print(f'Turno: {numero_turno}')
            dano_geral = int(seu_ataque - ataque_entidade)
            if (ataque_magia == resistencia_entidade):
                dano_geral *= 0.5
                #Resultados
                atacante = 'São João'
                magia = ataque_magia
                dano_ataque = dano_geral
                atacado = nome_entidade
                vida_restante = (pontos_vida_entidade - dano_geral)
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            elif (ataque_magia == fraqueza_entidade):
                dano_geral *= 1.7
                #Resultados
                seu_nome = 'São João'
                magia = ataque_magia
                dano_ataque = dano_geral
                adversario = nome_entidade
                vida_restante = (pontos_vida_entidade - dano_geral)
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            else:
                dano_geral = dano_geral
                #Resultado
                atacante = 'São João'
                ataque = seu_ataque 
                dano_ataque = dano_geral
                atacado = nome_entidade
                vida_restante = (pontos_vida_entidade - dano_geral)
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')                
        else:
            print(f'Turno: {numero_turno}')
            dano_geral = int(ataque_entidade - seu_ataque)
            if (turno_2 == ataque_magia):
                if (ataque_magia == sua_resistencia):
                    dano_geral *= 0.5
                    #Resultados
                    atacante = nome_entidade
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    atacado = 'São João'
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                elif (ataque_magia == sua_fraqueza):
                    dano_geral *= 1.7
                    #Resultados
                    seu_nome = nome_entidade
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    adversario = 'São João'
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            else:
                dano_geral = dano_geral
                #Resultado
                atacante = nome_entidade
                ataque = ataque_entidade 
                dano_ataque = dano_geral
                atacado = 'São João'
                vida_restante = (seus_pontos_vida - dano_geral)
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')

        numero_turno = 3
        if (dano_geral >= pontos_vida_entidade):
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        elif (dano_geral >= seus_pontos_vida):
            adversario = nome_entidade
            print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
        elif (turno_3 == ataque_magia == sua_fraqueza):
            #Resultados
            atacante = 'São João'
            elemento_magia = sua_fraqueza
            print(f'{atacante} teve sua fraqueza em {elemento_magia} acertada, portanto não poderá agir.')
            print(f'Turno: {numero_turno}')
            dano_geral = int(ataque_entidade - seu_ataque)
            if (turno_3 == ataque_magia):
                if (ataque_magia == sua_resistencia):
                    dano_geral *= 0.5
                    #Resultados
                    atacante = nome_entidade
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    atacado = 'São João'
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')                    
                elif (ataque_magia == sua_fraqueza):
                    dano_geral *= 1.7
                    #Resultados
                    seu_nome = 'São João'
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    adversario = nome_entidade
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            else:
                dano_geral = dano_geral
                #Resultado
                atacante = nome_entidade
                ataque = ataque_entidade 
                dano_ataque = dano_geral
                atacado = 'São João'
                vida_restante = (seus_pontos_vida - dano_geral)
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        else:
            print(f'Turno: {numero_turno}')
            dano_geral = int(seu_ataque - ataque_entidade)
            if (turno_3 == ataque_magia):
                if (ataque_magia == resistencia_entidade):
                    dano_geral *= 0.5
                    #Resultados
                    atacante = 'São João'
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    atacado = nome_entidade
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')                    
                elif (ataque_magia == fraqueza_entidade):
                    dano_geral *= 1.7
                    #Resultados
                    seu_nome = nome_entidade
                    magia = ataque_magia
                    dano_ataque = dano_geral
                    adversario = 'São João'
                    vida_restante = (pontos_vida_entidade - dano_geral)
                    print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            else:
                dano_geral = dano_geral
                #Resultado
                atacante = 'São João'
                ataque = ataque_entidade 
                dano_ataque = dano_geral
                atacado = nome_entidade
                vida_restante = (seus_pontos_vida - dano_geral)
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')

        #Resultados
        if (seus_pontos_vida > pontos_vida_entidade):
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
        elif (pontos_vida_entidade > seus_pontos_vida):
            adversario = nome_entidade
            print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
        else:
            print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
