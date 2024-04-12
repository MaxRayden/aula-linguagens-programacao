n = int(input())
for numero in range(1, n + 1):
    if numero % 2 == 0:
        quadrado = numero * numero
        print(f"{numero}^2 = {quadrado}")