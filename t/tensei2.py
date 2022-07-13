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

ataque_fisico = 'Ataque Físico'

Agi = 'fogo', 'Agi'
Bufu = 'gelo', 'Bufu'
Zio = 'eletricidade', 'Zio'

ataque_magia = Agi, Bufu, Zio

if (sua_fraqueza != 'fogo', sua_fraqueza != 'gelo', sua_fraqueza != 'eletricidade'):
    sua_fraqueza = ''

if (sua_resistencia != 'fogo', sua_resistencia != 'gelo', sua_resistencia != 'eletricidade'):
    sua_resistencia = ''

if (resistencia_entidade != 'fogo', resistencia_entidade != 'gelo', resistencia_entidade != 'eletricidade'):
    resistencia_entidade = ''

if (fraqueza_entidade != 'fogo', fraqueza_entidade != 'gelo', fraqueza_entidade != 'eletricidade'):
    fraqueza_entidade = ''

#Condições
#Turnos
numero_turno = 1
turno_1 = input()
print(f'Turno: {numero_turno}')
if (turno_1 == ataque_magia):
    if (ataque_magia == resistencia_entidade):
        #Resultados
        atacante = 'São João'
        magia = ataque_magia
        dano_ataque = int(seu_ataque - defesa_entidade)*0.5
        atacado = nome_entidade
        vida_restante = int(pontos_vida_entidade - dano_ataque)
        print(f'{atacante} usou {magia}, mas acertou uma resistência, portanto causou apenas {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
    elif (ataque_magia == fraqueza_entidade):
        #Resultados
        seu_nome = 'São João'
        magia = ataque_magia
        dano_ataque = int(seu_ataque - defesa_entidade)*1.7
        adversario = nome_entidade
        vida_restante = int(pontos_vida_entidade - dano_ataque)
        print(f'Isso! {seu_nome} usou {magia} e acertou a fraqueza do adversário! A magia causou {dano_ataque} de dano em {adversario} que agora tem {vida_restante} de vida.')
else:
    #Resultado
    atacante = 'São João'
    ataque = turno_1
    dano_ataque = int(seu_ataque - defesa_entidade)
    atacado = nome_entidade
    vida_restante = int(pontos_vida_entidade - dano_ataque)
    print(f'{atacante} usou {ataque} e causou {dano_ataque} de dano em {atacado} que agora tem {vida_restante} de vida.')
