#informações
nome_do_fogo = input()
decibeis_fogos = float(input())
max_caruaru = float(input())
max_campina_grande = float(input())

#resultados
if (decibeis_fogos <= max_campina_grande and decibeis_fogos <= max_caruaru):
    print(f'Boa Felipe, o {nome_do_fogo} será um sucesso em Campina Grande e Caruaru!')
elif (decibeis_fogos > max_campina_grande and decibeis_fogos <= max_caruaru):
    print(f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_do_fogo} vai ser extouro!')
elif (decibeis_fogos > max_caruaru and decibeis_fogos <= max_campina_grande):
    print(f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_do_fogo} vai ser extouro!')
else:
    print(f'Poxa Felipe, não vai ser dessa vez que {nome_do_fogo} fará um sucesso pelas festas juninas do Brasil')
