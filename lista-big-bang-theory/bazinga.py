piada = input()

piadas_boas = 0
piadas_ruins = 0

bom = True
ruim = True
mediano = True

while (piada != 'Fim do Show!'):
    reacao = input()
    piada = input()

    if (reacao == 'BAZINGA!'):
        piadas_boas += 1
    elif (reacao != 'BAZINGA!'):
        piadas_ruins += 1

if ((piadas_boas/(piadas_boas + piadas_ruins)) > 0.6):
    ruim = False
    mediano = False
elif ((piadas_ruins/(piadas_boas + piadas_ruins)) > 0.6):
    bom = False
    mediano = False
else:
    ruim = False
    bom = False

if (bom):
    print('BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!')
elif (mediano):
    print('Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!')
elif (ruim):
    print ('Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!')
