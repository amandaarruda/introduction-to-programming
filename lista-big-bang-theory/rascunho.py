batida = input()

contador = 0

while (batida != 'Boa noite'):
    if (batida == 'toc-toc-toc'):
        batida_seguinte = input()
        while (batida_seguinte != 'Boa noite'):
            if (batida_seguinte == 'Penny'):
                contador += 1
                print (contador)
                for i in range(contador):
                    if (contador == 3):
                        print ('Pode entrar Sheldon')
                        batida = input()
                    else:
                        batida = input()
            else:
                print ('Não pode entrar, se identifique!!!')
                batida = input()
        batida = input()
    else:
        batida = input()
else:
    print('Boa noite Penny')
    
#######################################################

batida = input()
contador = 0

while (batida != 'Boa noite'):
    if (batida == 'toc-toc-toc'):
        batida_penny = input()
        if (batida_penny == 'Penny'):
            contador += 1
            print(contador)
            if (contador < 3):
                batida = input()
            elif (contador == 3):
                for i in range(3):
                    batida_final = input()
                    if (contador == 3):
                        if (batida_final != 'Boa noite'):
                            print('Não pode entrar, se identifique!!!')
                            batida = input()
                        elif (batida == 'Boa noite'):
                            print ('Pode entrar Sheldon')
                    contador = 0
    else:
        print('Não pode entrar, se identifique!!!')
        contador = 0
        batida = input()
else:
    if (batida == 'Boa noite'):
        print('Boa noite Penny')
