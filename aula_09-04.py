nome = input("Digite seu nome: ")
i = int(input("Digite a posição que deseja adicionar a letra: "))
print(nome[i])

if nome[i] == "s":
    print(nome[:i]+"r"+nome[i+1:])
elif nome[i] == "m" : 
    print(nome[:i]+"n"+nome[i+1:])
else:
    print(nome[:i]+nome[i+1:])
