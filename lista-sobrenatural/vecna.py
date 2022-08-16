alertas = ['dor de cabeca', 'insonia', 'pesadelos', 'suor frio', 'visoes'] #sintomas que configuram a maldição
fichas = [] #lista dos relatórios de cada aluno
amaldicoados = [] #lista de todos os alunos amaldicoados
sintomas_iguais = [] #lista que confere quais os sintomas iguais de cada aluno
presença_max = False
relatorio = []
cursed = 0 #quantidade de alunos amaldiçoados

#Recebendo as fichas
while 'descobrir' not in relatorio:
    relatorio = input().split(', ')
    fichas.append(relatorio)
else:
    fichas.pop(-1)

for ficha in fichas:
    (nome, *sintomas) = ficha #separando as categorias
    #Conferindo se os sintomas são compatíveis com os sintomas de alerta
    for sintoma in sintomas: 
        if sintoma in alertas and sintoma not in sintomas_iguais: #se o sintoma for um sintoma de alerta e ainda não estiver nos sintomas iguais
            sintomas_iguais.append(sintoma)

    if (len(sintomas_iguais) == 5):
        amaldicoados.append(nome)
        cursed +=1
    
    sintomas_iguais = []

if (cursed == 0):
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')
else:
    if 'Max' in amaldicoados:
        print('Oh não, Max está em perigo! Let\'s run up that hill com a Kate Bush e ajudar nossa amiga.')
        amaldicoados.remove('Max')
        presença_max = True

    if (presença_max == True):
        if (cursed > 1):
            cursed -=1
            print(f'Além dela, tem mais {cursed} pessoa(s) na mira do Vecna!')
            if (cursed > 1):
                ultimo_aluno = amaldicoados.pop(-1)
                penultimo_aluno = amaldicoados.pop(-1)
                alunos = (', ').join(amaldicoados)
                print(f'Precisamos avisar {alunos}, {penultimo_aluno} e {ultimo_aluno} para prepararem suas músicas favoritas.')
                if (cursed > 2):
                    print(f'Precisamos avisar {alunos}, {penultimo_aluno} e {ultimo_aluno} para prepararem suas músicas favoritas.')
                else:
                    print(f'Precisamos avisar {penultimo_aluno} e {ultimo_aluno} para prepararem suas músicas favoritas.')               
            else:
                print(f'Precisamos avisar {amaldicoados[0]} para preparar sua música favorita.')
    else:        
        print(f'Tem {cursed} pessoa(s) na mira do Vecna!')
        if (cursed > 1):
            ultimo_aluno = amaldicoados.pop(-1)
            penultimo_aluno = amaldicoados.pop(-1)
            alunos = (', ').join(amaldicoados)
            if (cursed > 2):
                print(f'Precisamos avisar {alunos}, {penultimo_aluno} e {ultimo_aluno} para prepararem suas músicas favoritas.')
            else:
                print(f'Precisamos avisar {penultimo_aluno} e {ultimo_aluno} para prepararem suas músicas favoritas.')
        else:
            print(f'Precisamos avisar {amaldicoados[0]} para preparar sua música favorita.')
