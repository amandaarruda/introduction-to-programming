#Média de diamantes obtidos por hora de Arthur, Luiz e Pedro, respectivamente
A = int(input())
L = int(input()) 
P = int(input())

#Duração da competição(h)
H = int(input())

#Total de diamantes de cada participante
total_arthur = A*H
total_luiz = L*H
total_pedro = P*H

#comparando os valores
#utilizando x,y e z para facilitar as operações
X = total_arthur
Y = total_luiz
Z = total_pedro

primeira_comparacao = ((X + Y + abs(X-Y))//2)
comparacao_final = ((primeira_comparacao + Z + abs(primeira_comparacao-Z))//2)

#Máximo de diamantes de um participante
print(comparacao_final)
