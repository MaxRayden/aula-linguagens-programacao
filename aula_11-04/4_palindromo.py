texto = input("Digite um texto: ")

texto = texto.replace("-", "")
texto = texto.replace(".", "")
texto = texto.replace(",", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")
texto = texto.replace(" ", "").lower()

texto_invertido = texto[::-1]
print(texto_invertido)

if texto == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")