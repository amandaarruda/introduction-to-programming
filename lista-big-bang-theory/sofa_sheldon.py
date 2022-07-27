#Condições iniciais:
temperatura = 30
fome = True
internet = 0

#Entradas
acoes = input()

while (acoes != 'parar'):
    if (acoes == 'ir para o grad'):
        temperatura -= 5
        internet += 300
        acoes = input()
    elif (acoes == 'sair para a rua'):
        temperatura += 5
        acoes = input()
    elif (acoes == 'comer uma quentinha'):
        fome = False
        acoes = input()
    elif (acoes == 'conectar no wifi'):
        internet += 100
        acoes = input()
    else:
        print('Entrada inválida')
        acoes = input()
else:
    if (temperatura >= 30):
        print('A temperatura aqui não está agradável')
    
    if (temperatura <= 25):
        print('Agora sim, está aconchegante')
    
    if (fome == True):
        print('Meu corpo precisa de comida')

    if (internet < 100):
        print('Essa conexão está horrível')

    if (fome == False and temperatura <= 25 and internet >= 300):
        print('Finalmente um lugar preciso para mim!')
