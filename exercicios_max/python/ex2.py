idade = int(input())

if idade < 13:
    print ("é criança")
elif idade > 12 and idade < 19 :
    print("é adolescente")
elif idade >=19 and idade < 61 :
    print("é adulto ")
else:
    print("é velho")