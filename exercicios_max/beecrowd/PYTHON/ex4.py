num =input()
num = num.split()
a = int(num[0])
b = int(num[1])

if a > b:  
    if a % b == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if b % a == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
