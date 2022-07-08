#Quantidade de diamantes necessários
D = int(input())

#Oferendas
arthur = 10
luiz = 30
pedro = 100

#Resultado
if (D <= arthur):
    print("Arthur")
elif (arthur < D <= luiz):
    print("Luiz")
elif (luiz < D <= pedro):
    print("Pedro")
else:
    print("Nenhum")
