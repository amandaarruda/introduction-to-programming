#criando a lista de suspeitos
suspeitos = []
#recebendo os nomes
nomes = input()
#dividindo os nomes para armazenar na lista    
suspeitos = nomes.split(',') #aqui, ele elimina a vírgula e divide o input em uma lista com os nomes

#Entradas:
while (len(suspeitos) != 1):
    pista = input()
    if (pista == 'Não encontrei nada no primeiro suspeito'):
        suspeitos.pop(0)
    elif (pista == 'O último da lista está limpo'):
        suspeitos.pop(-1)
    elif (pista == 'Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita'):
        if (len(suspeitos) % 2 != 0):
            mediana = int((len(suspeitos)+1)/2)
            suspeitos.pop(mediana)
        else:
            mediana = int(((len(suspeitos))/2))
            suspeitos.pop(mediana)
    elif (pista == 'Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:'):
        individuo = int(input())
        suspeitos.pop(individuo)
    elif (pista == 'Acho que temos mais uma opção a ser analisada…'):
        suspeitos.append()    
    else:
        print('Isso não estava no combinado, a lista vai permanecer do mesmo jeito')
else:
    print(f'Acho que encontramos o suspeito. O seu nome é {suspeitos[0]}, vamos salvar o Sam!')
