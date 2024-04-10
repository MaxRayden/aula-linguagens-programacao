nome = input("Digite seu nome: ")
i = int(input("Digite a posição que deseja adicionar a letra: "))
print(nome[i])

if nome[i] == "s":
    print(nome[:i]+"r"+nome[-1:])
elif nome[i] == "m" : 
    print(nome[:i]+"n"+nome[-1:])
else:
    print(nome[:i-1]+nome[-1:])
