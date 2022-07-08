mensagem = input()
nome = input()

#.captalize formata o texto
mensagem = mensagem.capitalize()

print("{}, {}!".format(mensagem, nome))
print(f"{mensagem},{nome}!\n") #fstrings
print(mensagem + ", " + nome + "!\n")
print(mensagem, ", ", nome, "!")
