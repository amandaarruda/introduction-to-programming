def separador_silabas(palavra):
    palavra_separada = [] #reseta a palavra anterior
    silaba_atual = [] #representa a sílaba que vai ser formada
    vogais = ['a', 'e', 'i', 'o', 'u']

    for letra in palavra:
        silaba_atual.append(letra) #vai adicionando cada letra na sílaba atual
        if letra in vogais:
            silaba_final = ('').join(silaba_atual) #se a letra for uma vogal, a sílaba acaba ali 
            palavra_separada.append(silaba_final) #adiciona a sílaba dividida
            silaba_atual = [] #reseta a sílaba atual

    checador_mnemonico(palavra_separada)

def checador_mnemonico(palavra_separada):
    ordem_formada = [] #é a ordem das sílabas que estão na palavra e no nome do hospital
    for silaba in palavra_separada:
        if (silaba in hospital):
            ordem_formada.append(silaba)
            if (silaba not in silabas_encontradas):
                silabas_encontradas.append(silaba)
            else:
                ordem_formada.remove(silaba)

    resposta(ordem_formada, palavra_separada)

def resposta(ordem_formada, palavra_separada):
    if (len(ordem_formada) == 0):
        print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')
    elif (len(ordem_formada) == 1):
        print(f'Lembrei! A sílaba {ordem_formada[0]} está no nome do hospital. Obrigada, Totoro!')
    elif (len(ordem_formada) > 1):
        if (palavra_separada == ordem_formada):
            if (palavra in palavras_embutidas_hospital):
                print(f'A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!')
            else:
                silabas = (', ').join(ordem_formada)
                print(f'Lembrei! As sílabas: {silabas} estão no nome do hospital. Obrigada, Totoro!')        
        else:
            silabas = (', ').join(ordem_formada)
            print(f'Lembrei! As sílabas: {silabas} estão no nome do hospital. Obrigada, Totoro!')

hospital = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']
palavras_embutidas_hospital = ['shichi', 'chiko', 'koku', 'kuya', 'yama', 'shichiko', 'chikoku', 'kokuya', 'kuyama', 
'shichikoku', 'chikokuya', 'kokuyama', 'shichikokuya', 'chikokuyama','shichikokuyama']
silabas_encontradas = [] #guarda todas as sílabas corretas até o momento
ordem_formada = []

while (len(silabas_encontradas) != 6): #enquanto não tivermos achado todas as sílabas
    palavra = input()
    separador_silabas(palavra)
else:
    print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
