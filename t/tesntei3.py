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

#Turno_1
numero_turno = 1
turno_1 = input()
print(f'Turno: {numero_turno}')
pegou_na_fraqueza = False
if(turno_1 == 'Agi'):
    if (fraqueza_entidade == 'fogo'):
        pegou_na_fraqueza = True
        seu_nome = 'São João'
        magia = turno_1
        dano_ataque = (seu_ataque - defesa_entidade) * 1.7
        adversario = nome_entidade
        vida_restante = 
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
    elif (resistencia_entidade == 'fogo'):
        print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
elif(turno_1 == 'Bufu'):
    if (fraqueza_entidade == 'gelo'):
        pegou_na_fraqueza = True
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
    elif (resistencia_entidade == 'gelo'):
        print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
elif(turno_1 == 'Zio'):
    if (fraqueza_entidade == 'eletricidade'):
        pegou_na_fraqueza = True
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
    elif (resistencia_entidade == 'eletricidade'):
        print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
else:
    atacante = 'São João'
    ataque = turno_1
    dano_ataque = seu_ataque - defesa_entidade
    atacado = nome_entidade
    vida_restante = 
    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')

#Turno 2
numero_turno = 2
if (pegou_na_fraqueza == True):
