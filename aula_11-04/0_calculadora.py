def soma(a,b):
    print(a+b)
def subtracao(a,b):
    print(a-b)   
def multiplicacao(a,b):
    print(a*b)
def divisao(a,b):
    print(a/b)
valor1 = float(input("Digite um número: "))
while valor1 != -1:
    operador = input("Digite um operador: ")
    valor2 = float(input("Digite outro número: "))
    if valor2 == -1:
        break
    resultado = 0
    if operador == '+':
        soma(valor1,valor2),"\n\n"
    elif operador == '-':
        subtracao(valor1,valor2),"\n\n"
    elif operador == '*':
        multiplicacao(valor1,valor2),"\n\n"
    elif operador == '/':
        divisao(valor1,valor2),"\n\n"
    else:
        print('operador inválido')
    valor1 = float(input("Digite um número: "))   
print("encerrando...")