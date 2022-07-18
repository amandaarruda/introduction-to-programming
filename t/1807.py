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

#Cálculos dos danos
dano_fraqueza_entidade = int((seu_ataque - defesa_entidade) * 1.7)
dano_resistencia_entidade = int((seu_ataque - defesa_entidade) * 0.5)
dano_fisico_entidade = int(seu_ataque - defesa_entidade)

dano_fraqueza_sua = int((ataque_entidade - sua_defesa) * 1.7)
dano_resistencia_sua = int((ataque_entidade - sua_defesa) * 0.5)
dano_fisico_seu = int(ataque_entidade - sua_defesa)

#Turno 1
#Condições
if (sua_fraqueza != sua_resistencia and fraqueza_entidade != resistencia_entidade):
    if (seu_ataque > defesa_entidade and ataque_entidade > sua_defesa):
        turno_1 = input()
        numero_turno = 1
        print(f'Turno: {numero_turno}')

        #Variávies das mensagens
        seu_nome = 'São João'
        magia = turno_1
        adversario = nome_entidade
        atacante = seu_nome
        ataque = turno_1
        atacado = nome_entidade

        #Para definir o próximo turno
        pegou_na_fraqueza = False

        if (turno_1 == 'Agi'):
            if (fraqueza_entidade == 'fogo'):
                pegou_na_fraqueza = True
                dano_ataque = dano_fraqueza_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            elif (resistencia_entidade == 'fogo'):
                dano_ataque = dano_resistencia_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            else:
                dano_ataque = dano_fisico_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0            
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante        
        elif (turno_1 == 'Bufu'):
            if (fraqueza_entidade == 'gelo'):
                pegou_na_fraqueza = True
                dano_ataque = dano_fraqueza_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0                
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            elif (resistencia_entidade == 'gelo'):
                dano_ataque = dano_resistencia_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0                
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            else:
                dano_ataque = dano_fisico_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0            
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante        
        elif (turno_1 == 'Zio'):
            if (fraqueza_entidade == 'eletricidade'):
                pegou_na_fraqueza = True
                dano_ataque = dano_fraqueza_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0                
                print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            elif (resistencia_entidade == 'eletricidade'):
                dano_ataque = dano_resistencia_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0                
                print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
            else:
                dano_ataque = dano_fisico_entidade
                vida_restante = pontos_vida_entidade - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0            
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                pontos_vida_entidade = vida_restante
        else:
            dano_ataque = dano_fisico_entidade
            vida_restante = pontos_vida_entidade - dano_ataque
            if (vida_restante <= 0):
                vida_restante = 0            
            print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        

        #Turno 2
        if (pegou_na_fraqueza == True):
            elemento_magia = fraqueza_entidade
            atacante = nome_entidade
            print(f'{atacante} teve sua fraqueza em {elemento_magia} acertada, portanto não poderá agir.')
        elif (pontos_vida_entidade == 0):
            print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
            quit()
        else:
            #Atributos
            numero_turno = 2
            turno_2 = input()
            print(f'Turno: {numero_turno}')

            #Variáveis
            magia = turno_2
            ataque = turno_2

            #Variável para saber se a próxima rodada acontece
            pegou_na_fraqueza_sua = False

            #Variáveis
            atacante = nome_entidade
            atacado = seu_nome
            if (turno_2 == 'Agi'):
                if (sua_fraqueza == 'fogo'):
                    pegou_na_fraqueza_sua = True
                    dano_ataque = dano_fraqueza_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0 
                    print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante
                elif (sua_resistencia == 'fogo'):
                    dano_ataque = dano_resistencia_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                     
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante
                else:
                    dano_ataque = dano_fisico_seu
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                 
                    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante            
            elif (turno_2 == 'Bufu'):
                if (sua_fraqueza == 'gelo'):
                    pegou_na_fraqueza_sua = True
                    dano_ataque = dano_fraqueza_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                     
                    print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante
                elif (sua_resistencia == 'gelo'):
                    dano_ataque = dano_resistencia_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                     
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante            
                else:
                    dano_ataque = dano_fisico_seu
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                 
                    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante               
            elif (turno_2 == 'Zio'):
                if (sua_fraqueza == 'eletricidade'):
                    pegou_na_fraqueza_sua = True
                    dano_ataque = dano_fraqueza_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                     
                    print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante
                elif (sua_resistencia == 'eletricidade'):
                    dano_ataque = dano_resistencia_sua
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                     
                    print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante
                else:
                    dano_ataque = dano_fisico_seu
                    vida_restante = seus_pontos_vida - dano_ataque
                    if (vida_restante <= 0):
                        vida_restante = 0                 
                    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                    seus_pontos_vida = vida_restante              
            else:
                dano_ataque = dano_fisico_seu
                vida_restante = seus_pontos_vida - dano_ataque
                if (vida_restante <= 0):
                    vida_restante = 0                 
                print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
                seus_pontos_vida = vida_restante

        #Turno 3



                    



