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

#Turno 1
numero_turno = 1
turno_1 = input()

pegou_na_fraqueza = False
magia = turno_1
adversario = nome_entidade
seu_nome = 'São João'
atacado = nome_entidade
atacante = 'São João'
ataque = turno_1 

if(turno_1 == 'Agi'):
    if (fraqueza_entidade == 'fogo'):
        pegou_na_fraqueza = True
        dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
    elif (resistencia_entidade == 'fogo'):
        dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
elif(turno_1 == 'Bufu'):
    if (fraqueza_entidade == 'gelo'):
        pegou_na_fraqueza = True
        dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
    elif (resistencia_entidade == 'gelo'):
        dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
elif(turno_1 == 'Zio'):
    if (fraqueza_entidade == 'eletricidade'):
        pegou_na_fraqueza = True
        dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
    elif (resistencia_entidade == 'eletricidade'):
        dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
        vida_restante = pontos_vida_entidade - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
else:
    atacante = 'São João'
    ataque = turno_1
    dano_ataque = int(seu_ataque - defesa_entidade)
    vida_restante = pontos_vida_entidade - dano_ataque
    print(f'Turno: {numero_turno}')
    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
    pontos_vida_entidade = vida_restante
#Turno 2
numero_turno = 2
turno_2 = input()
magia = turno_2
ataque = turno_2

if (dano_ataque >= vida_restante):
    print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
elif(pegou_na_fraqueza == True):
    adversario = nome_entidade
    atacado = nome_entidade
    atacante = 'São João'
    if(turno_2 == 'Agi'):
        if (fraqueza_entidade == 'fogo'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'fogo'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    elif(turno_2 == 'Bufu'):
        if (fraqueza_entidade == 'gelo'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'gelo'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    elif(turno_2 == 'Zio'):
        if (fraqueza_entidade == 'eletricidade'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'eletricidade'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    else:
        pegou_na_fraqueza = False
        dano_ataque = int(seu_ataque - defesa_entidade)
        vida_restante = vida_restante - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
elif(pegou_na_fraqueza == False):
    adversario = nome_entidade
    seu_nome = 'São João'
    atacado = 'São João'    
    if(turno_2 == 'Agi'):
        if (sua_fraqueza == 'fogo'):
            pegou_na_fraqueza = True
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'fogo'):
            pegou_na_fraqueza = False
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
    elif(turno_2 == 'Bufu'):
        if (sua_fraqueza == 'gelo'):
            pegou_na_fraqueza = True
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'gelo'):
            pegou_na_fraqueza = False
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida')
            seus_pontos_vida = vida_restante
    elif(turno_2 == 'Zio'):
        if (sua_fraqueza == 'eletricidade'):
            pegou_na_fraqueza = True
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'eletricidade'):
            pegou_na_fraqueza = False
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida')
            seus_pontos_vida = vida_restante
    else:
        pegou_na_fraqueza = False
        dano_ataque = int(ataque_entidade - sua_defesa)
        atacado = 'São João'
        vida_restante = seus_pontos_vida - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        seus_pontos_vida = vida_restante

#Turno 3
numero_turno = 3
turno_3 = input()
magia = turno_3
ataque = turno_3

if (dano_ataque >= pontos_vida_entidade):
    print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
elif (dano_ataque >= seus_pontos_vida):
    adversario = nome_entidade
    print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
elif(pegou_na_fraqueza == True):
    adversario = nome_entidade
    seu_nome = 'São João'
    if(turno_3 == 'Agi'):
        if (fraqueza_entidade == 'fogo'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'fogo'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    elif(turno_3 == 'Bufu'):
        if (fraqueza_entidade == 'gelo'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'gelo'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    elif(turno_3 == 'Zio'):
        if (fraqueza_entidade == 'eletricidade'):
            pegou_na_fraqueza = True
            dano_ataque = int((seu_ataque - defesa_entidade) * 1.7)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
        elif (resistencia_entidade == 'eletricidade'):
            pegou_na_fraqueza = False
            dano_ataque = int((seu_ataque - defesa_entidade) * 0.5)
            vida_restante = vida_restante - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            pontos_vida_entidade = vida_restante
    else:
        pegou_na_fraqueza = False
        atacante = 'São João'
        ataque = turno_3
        dano_ataque = int(seu_ataque - defesa_entidade)
        atacado = nome_entidade
        vida_restante = vida_restante - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        pontos_vida_entidade = vida_restante
elif(pegou_na_fraqueza == False):
    adversario = nome_entidade
    seu_nome = 'São João'     
    if(turno_3 == 'Agi'):
        if (sua_fraqueza == 'fogo'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'fogo'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida')
            seus_pontos_vida = vida_restante
    elif(turno_3 == 'Bufu'):
        if (sua_fraqueza == 'gelo'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'gelo'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida')
            seus_pontos_vida = vida_restante
    elif(turno_3 == 'Zio'):
        if (sua_fraqueza == 'eletricidade'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 1.7)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'Vixe! {adversario} usou {magia} e acertou sua fraqueza! A magia causou {dano_ataque} de dano em {seu_nome} que agora tem {vida_restante} de vida.')
            seus_pontos_vida = vida_restante
        elif (sua_resistencia == 'eletricidade'):
            dano_ataque = int((ataque_entidade - sua_defesa) * 0.5)
            vida_restante = seus_pontos_vida - dano_ataque
            print(f'Turno: {numero_turno}')
            print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida')
            seus_pontos_vida = vida_restante
    else:
        atacante = nome_entidade
        dano_ataque = int(ataque_entidade - sua_defesa)
        atacado = 'São João'
        vida_restante = seus_pontos_vida - dano_ataque
        print(f'Turno: {numero_turno}')
        print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
        seus_pontos_vida = vida_restante

#Resultados
if (seus_pontos_vida > pontos_vida_entidade):
    print('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
elif (pontos_vida_entidade > seus_pontos_vida):
    adversario = nome_entidade
    print(f'Morremos… Parece que {adversario} tem mais chances de ascender ao trono da Midsommar…')
elif (pontos_vida_entidade == seus_pontos_vida):
    print('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
