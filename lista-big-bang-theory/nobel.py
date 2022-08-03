feito = input()

#Checkpoints para conferir a ordem dos feitos
checkpoint_1 = False
checkpoint_2 = False
checkpoint_3 = False
checkpoint_4 = False
checkpoint_5 = False
checkpoint_6 = False

while (feito != 'É o fim da Estrada pra Sheldon Cooper'): #Conferindo se ele não desistiu
    if (feito == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito == 'Leonard seu anão covarde' or feito == 'Tu é muito burro Raj'):
        print('Não xingue seus amigos Sheldon!') #Rebatendo xingamentos
        feito = input()
    else:
        if (feito == 'Começou a Trabalhar na Caltech'): 
            feito_2 = input()
            if (feito_2 != 'Bazinga'): #Conferindo se o Bazinga não atrapalhou
                checkpoint_1 = True #Se deu tudo certo, ele entra aqui
                break #Foi mal por ter usado o break e o pass... Não consegui fazer sem
            elif (feito_2 == 'É o fim da Estrada pra Sheldon Cooper'): #Se ele tiver desistido depois de ter entrado em Caltech
                print('Tão perto, mas tão longe')
            else:
                feito = input() #Caso o Bazinga tenha atrapalhado
                pass
        else:
            feito = input() #Caso o feito 1 tenha sido diferente da ordem
            pass
else:
    print('Que potencial desperdiçado...') #Se ele tiver desistido sem ter entrado em Caltech

if (checkpoint_1 == True): #Tava dando errado se eu usava só a booleana sem a comparação... Foi malll
    while (feito_2 != 'É o fim da Estrada pra Sheldon Cooper'):
        if (feito_2 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_2 == 'Leonard seu anão covarde' or feito_2 == 'Tu é muito burro Raj'):
            print('Não xingue seus amigos Sheldon!') 
            feito_2 = input()
        else:
            if (feito_2 == 'Trabalho sobre a String Theory'): 
                feito_3 = input()
                if (feito_3 != 'Bazinga'): 
                    checkpoint_2 = True 
                    break
                elif (feito_3 == 'É o fim da Estrada pra Sheldon Cooper'):
                    print('Tão perto, mas tão longe')
                else:
                    feito_2 = input() 
                    pass
            else:
                feito_2 = input() 
                pass                            
    else:
        print('Tão perto, mas tão longe')

if (checkpoint_2 == True):
    while (feito_3 != 'É o fim da Estrada pra Sheldon Cooper'):
        if (feito_3 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_3 == 'Leonard seu anão covarde' or feito_3 == 'Tu é muito burro Raj'):
            print('Não xingue seus amigos Sheldon!') 
            feito_3 = input()
        else:
            if (feito_3 == 'Ganhar o Chancellor de ciência'): 
                feito_4 = input()
                if (feito_4 != 'Bazinga'): 
                    checkpoint_3 = True
                    break
                elif (feito_4 == 'É o fim da Estrada pra Sheldon Cooper'):
                    print('Não desista Sheldon, você ainda têm muito para alcançar!')
                else:
                    feito_3 = input() 
                    pass
            else:
                feito_3 = input() 
                pass                            
    else:
        print('Tão perto, mas tão longe')

if (checkpoint_3 == True):
    while (feito_4 != 'É o fim da Estrada pra Sheldon Cooper'):
        if (feito_4 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_4 == 'Leonard seu anão covarde' or feito_4 == 'Tu é muito burro Raj'):
            print('Não xingue seus amigos Sheldon!') 
            feito_4 = input()
        else:
            if (feito_4 == 'Pensar na Teoria de Cooper-Hofstader'): 
                feito_5 = input()
                if (feito_5 != 'Bazinga'): 
                    checkpoint_4 = True
                    break
                elif (feito_5 == 'É o fim da Estrada pra Sheldon Cooper'):
                    print('Não desista Sheldon, você ainda têm muito para alcançar!')
                else:
                    feito_4 = input() 
                    pass
            else:
                feito_4 = input() 
                pass                            
    else:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')


if (checkpoint_4 == True):
    while (feito_5 != 'É o fim da Estrada pra Sheldon Cooper'):
        if (feito_5 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_5 == 'Leonard seu anão covarde' or feito_5 == 'Tu é muito burro Raj'):
            print('Não xingue seus amigos Sheldon!') 
            feito_5 = input()
        else:
            if (feito_5 == 'Criou a Super Assimetria'): 
                feito_6 = input()
                if (feito_6 != 'Bazinga'): 
                    checkpoint_5 = True
                    break
                elif (feito_6 == 'É o fim da Estrada pra Sheldon Cooper'):
                    print('Nãoooooo, esse momento ia ser seu Sheldon')
                else:
                    feito_5 = input() 
                    pass
            else:
                feito_5 = input() 
                pass                            
    else:
        print('Não desista Sheldon, você ainda têm muito para alcançar!')

if (checkpoint_5 == True):
    if (feito_6 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_6 == 'Leonard seu anão covarde' or feito_6 == 'Tu é muito burro Raj'):
        print('Não xingue seus amigos Sheldon!') 
        feito_6 = input()
    elif (feito_6 == 'Bazinga'):
        feito_6 = input()
        pass
    elif (feito_6 == 'Ganhar o Nobel'):  
        print('Você conseguiu Sheldon, o Nobel é seu!!!')
    elif (feito_6 == 'É o fim da Estrada pra Sheldon Cooper'):
        print('Nãoooooo, esse momento ia ser seu Sheldon')
    else:
        feito_6 = input()
        pass

if (checkpoint_5 == True):
    while (feito_6 != 'É o fim da Estrada pra Sheldon Cooper'):
        if (feito_6 == 'Tinha que ser o engenheiro sem Phd do Wolowitz' or feito_6 == 'Leonard seu anão covarde' or feito_6 == 'Tu é muito burro Raj'):
            print('Não xingue seus amigos Sheldon!') 
            feito_6 = input()
        else:
            if (feito_6 != 'Ganhar o Nobel'): 
                feito_7 = input()
                if (feito_7 != 'Bazinga'): 
                    checkpoint_6 = True
                elif (feito_7 == 'É o fim da Estrada pra Sheldon Cooper'):
                    print('Nãoooooo, esse momento ia ser seu Sheldon')
                else:
                    feito_6 = input() 
                    pass
            else:
                checkpoint_6 == True
                break                
    else:
        print('Nãoooooo, esse momento ia ser seu Sheldon')


if (checkpoint_6 == True):
    print()
