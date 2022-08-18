#"desenhando" a matrix do CIn
matriz = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]
cracha = False
rodada_parado = False
zumbi = False
porta = False
fim = False

voceY = int(input())
voceX = int(input())
matriz[voceY][voceX] = 'V'

zumbiY = int(input())
zumbiX = int(input())
matriz[zumbiY][zumbiX] = 'Z'

crachaY = int(input())
crachaX = int(input())
matriz[crachaY][crachaX] = 'C'

portaY = int(input())
portaX = int(input())
matriz[portaY][portaX] = 'P'

while (not(fim)): #enquanto você ainda não chega na porta ou o zumbi ainda não pegou você
    matriz[zumbiY][zumbiX] = '-'
    if (zumbiX != voceX): #alinhando o X
        if (zumbiX > voceX):
            zumbiX -= 1
        else:
            zumbiX += 1
        matriz[zumbiY][zumbiX] = 'Z'
    else: #alinhando o Y
        if (zumbiY > voceY):
            zumbiY -= 1
        else:
            zumbiY += 1
        if (zumbiX == voceX and zumbiY == voceY): #se o zumbi lhe pega
            zumbi = True
        matriz[zumbiY][zumbiX] = 'Z'
        
    if (zumbi == False): #se o zumbi não lhe pegou
        matriz[voceY][voceX] = '-'
        if (cracha == False): #se ainda não tiver pego o crachá
            if (voceX != crachaX):
                if (voceX > crachaX):
                    voceX -= 1
                else:
                    voceX += 1
                matriz[voceY][voceX] = 'V'
            else:
                if (voceY > crachaY):
                    voceY -= 1
                else:
                    voceY += 1   
                matriz[voceY][voceX] = 'V' 
            if (voceX == crachaX and voceY == crachaY):
                matriz[voceY][voceX] = 'V'
                cracha = True
                rodada_parado = True                     
        else: #indo em direção à porta
            if (rodada_parado == True):
                rodada_parado = False
                matriz[voceY][voceX] = 'V'
            else:
                if (voceX != portaX):
                    if (voceX > portaX):
                        voceX -= 1
                    else:
                        voceX += 1
                    matriz[voceY][voceX] = 'V'
                else:
                    if (voceY > portaY):
                        voceY -= 1
                    else:
                        voceY += 1
                    matriz[voceY][voceX] = 'V'
                if (voceY == portaY and voceX == portaX):
                    porta = True
                    matriz[voceY][voceX] = 'V'

    for linha in range(len(matriz)): #imprimindo a matriz
        (' ').join(matriz[linha])
        print(*matriz[linha])

    if (cracha == False and zumbi == False):
        print('Ainda não achei o crachá')
    else:
        if (cracha == True):
            if (rodada_parado == True):
                print('Finalmente! Peguei o crachá')
            else:
                if (porta == False and zumbi == False):
                    print('Já peguei o crachá')

    if (porta == False):
        if(zumbi == False):
            norma = int((((voceX - zumbiX)**2) + ((voceY - zumbiY)**2))**(1/2)) 
            if (norma <= 3):
                print('Preciso acelerar, o zumbi tá na minha cola!\n')
            elif (3 < norma <= 4):
                print('Consigo ver la longe o zumbi, mas é melhor acelerar!\n')
            elif (norma > 4):
                print('O zumbi está longe, mas não posso ficar parado\n')
        else:
            print('Ferrou, agora vou virar um zumbi')
            fim = True
    else:
        print('Consegui achar a porta, agora é so passar na catraca e vazar daqui!')
        fim = True
