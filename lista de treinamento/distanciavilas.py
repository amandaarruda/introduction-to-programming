#coordenadas das cidades
hogsmeade_X = 34
hogsmeade_Z = 220

kakariko_X = 0
kakariko_Z = 0

solitude_X = 140
solitude_Z = 456

#coordenadas de Steve
X = int(input())
Z = int(input())

#distâncias
distancia_hogsmeade = ((X - hogsmeade_X)**2 + (Z - hogsmeade_Z)**2)**(1/2)
distancia_kariko = ((X - kakariko_Z)**2 + (Z - kakariko_Z)**2)**(1/2)
distancia_solitude = ((X - solitude_X)**2 + (Z - solitude_Z)**2)**(1/2)

#resultados
print(f'Distância para Hogsmeade: {distancia_hogsmeade:.2f}')
print(f'Distância para Kakariko: {distancia_kariko:.2f}')
print(f'Distância para Solitude: {distancia_solitude:.2f}')
