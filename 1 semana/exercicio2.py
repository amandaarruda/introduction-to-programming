#Objetivo: Ler dois valores inteiros, armazenar o primeiro em A, o segundo em B. 
# se A for maior que B, trocar (e vice-versa).
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

A = valor1
B = valor2
AUX = 0

if (A > B):
    AUX = A
    A = B
    B = AUX
    
print(A)
print(B)