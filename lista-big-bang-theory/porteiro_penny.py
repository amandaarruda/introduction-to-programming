batida = input()

contador = 0

while (batida != 'Boa noite'):
    if (batida == 'toc-toc-toc'):
        batida_penny = input()
        if (batida_penny == 'Penny'):
            contador += 1
            print(contador)
            for i in range(1):
                if (contador == 3):
                    print('Pode entrar Sheldon')
                    contador = 0
            batida = input()
        else:
            contador = 0
            print('Não pode entrar, se identifique!!!')
            batida = input()
    else:
        contador = 0
        print('Não pode entrar, se identifique!!!')
        batida = input()
else:
    print('Boa noite Penny')
