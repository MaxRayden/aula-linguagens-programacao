valor1 = float(input("Digite um número: "))

while valor1 != -1:
    operador = input("Digite um operador: ")
    valor2 = float(input("Digite outro número: "))
    if valor2 == -1:
        break
    resultado = 0
    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1-valor2
    elif operador == '*':
        resultado = valor1*valor2
    elif operador == '/':
        resultado = valor1/valor2
    else:
        print('operador inválido')
    print(resultado,"\n\n")
    valor1 = float(input("Digite um número: "))
    
print("encerrando...")