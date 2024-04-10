#minha solução
#print("inicio\n")
#nome = input()
#nome = nome.split()
#nome1 = nome[0]
#sobrenome = nome[1]
#print("\n")
#print(nome1[0]+nome1[1:].upper())
#print(sobrenome[:1].upper()+sobrenome[1:])


#solução da professora

nome = input()
sobrenome = input()
print(nome.lower()[:1]+nome.upper()[1:])
print(sobrenome.upper()[:1]+sobrenome.lower()[1:])