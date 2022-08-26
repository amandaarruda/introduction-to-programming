def pedras_quentes(valores):
    valores[2] += ((valores[1] + valores[2]) // 2) #muda a gorjeta
    valores[0] -= 20 #subtrai do tempo total
    valores[1] += 20 #atualiza o tempo decorrido

def massagem_pes(valores):
    if (valores[2] % 10 == 0): #muda a gorjeta
        valores[2] += ((valores[2] % 7) * 6)
    else:
        valores[2] += ((valores[2] % 7)**2)
    valores[0] -= 30 #subtrai do tempo total
    valores[1] += 30 #atualiza o tempo decorrido
        
def servir_refeicao(valores):
    if (valores[2] % 10 == 0): #muda a gorjeta
        valores[2] += 5
    else:
        while (valores[2] % 10 != 0): #muda a gorjeta
            valores[2] += 1
    valores[0] -= 15 #subtrai do tempo total
    valores[1] += 15 #atualiza o tempo decorrido

def massagem_completa(valores):
    valores[2] = str(valores[2]) 
    soma = 0
    for numero in valores[2]: #muda a gorjeta
        soma += int(numero)
    valores[2] = int(valores[2]) + soma
    valores[0] -= 50 #subtrai do tempo total
    valores[1] += 50 #atualiza o tempo decorrido

valores = [120, 0, 10] #onde valores[0] é o tempo total, valores[1] é o tempo decorrido e valores[2] é o total de gorjetas
servico_inexistente = False

while (valores[0] > 0 and valores[2] < 50):
    servico = input()
    if (servico == 'pedras'):
        pedras_quentes(valores)
        nome_servico = 'Pedras Quentes'
    elif (servico == 'pes'):
        massagem_pes(valores)
        nome_servico = 'Massagem nos Pes'
    elif (servico == 'refeicao'):
        servir_refeicao(valores)
        nome_servico = 'Servir Refeicao'
    elif (servico == 'completa'):
        massagem_completa(valores)
        nome_servico = 'Massagem Completa'
    else:
        servico_inexistente = True
        valores[0] -= 5 #subtrai do tempo print('Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.')total
        valores[1] += 5 #atualiza o tempo decorrido
        print(f'O cliente fez voce perder tempo, voce ainda possui {valores[2]} gorjetas.')

    if (not servico_inexistente):
        print(f'Voce concluiu o servico de {nome_servico} e agora possui {valores[2]} gorjetas.')
else:
    if (valores[2] >= 50):
        print(f'Você acumulou {valores[2]} gorjetas, com essa quantidade voce conseguira comprar sua passagem de saida e salvar seus pais.')
    else:
        print('Voce nao conseguiu o minimo necessario para comprar a passagem de saida desse mundo e salvar seus pais.')
