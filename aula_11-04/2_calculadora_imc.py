peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura**2)

if imc < 18.5:
    classificacao = "Baixo peso"
elif imc >= 18.5 and imc < 25:
    classificacao = "Peso normal"
elif imc >= 25 and imc <30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc} e sua classificação é: {classificacao}")