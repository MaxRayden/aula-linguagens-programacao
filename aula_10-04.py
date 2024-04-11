#ATIVIDADE PARA O GITHUB

notas = []
nota = float(input("Digite sua nota: "))
while nota != -1:
    notas.append(nota)
    nota=float(input("Insira a nota: ")) 
soma = sum(notas)
media = soma / len(notas)
if media < 7:
    print("NÃO FOI APROVADO")
else:
    print("APROVADO")



#minha solução

#notas = []
#soma = 0
#cont = 0
#while cont != -1:
#    notas.append(float(input("Insira a nota: ")))
#    cont=notas[-1]
#notas.pop()
#soma = sum(notas)
#print(soma)
#media = soma / len(notas)
#print(media)
#if media < 7:
#    print("NÃO FOI APROVADO")
#else:
#    print("APROVADO")


#>>>>>>>>>>>>>>>>>>>>>
#com 'for'
#notas = []
#soma = 0
#for i in range(0,10):
#    notas.append(float(input("Insira a nota["+str(i)+"]: ")))
#soma = sum(notas)
#media = soma / len(notas)
#if media < 7:
#    print("NÃO FOI APROVADO")
#print("APROVADO")







#OUTROS CÓDIGOS DA AULA

#DADOS = [1, 2, 3, 4]
#DADOS[0] = input("Digite seu nome: ")
#DADOS[1] = int(input("Digite sua idade: "))
#DADOS[2] = float(input("Digite sua altura: "))
#DADOS[3] = input("Digite o bairro onde você mora: ")

#print(DADOS)

#outra forma

#dados = []
#dados.append(input("Digite seu nome: "))
#dados.append(input("Digite sua idade: "))
#dados.append(input("Digite sua altura: "))
#dados.append(input("Digite o bairro onde você mora: "))
#print(dados)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>