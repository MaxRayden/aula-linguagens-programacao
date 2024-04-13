def tamanho_da_lista(a):
    i = 0
    j = 0 
    for n in a:
        i += 1
        for k in n:
            j +=1

    print(i)
    print(j)        
    

entrada = ["oi", "tudo", "bem"]
print("usando len(): ", len(entrada))
print("usando minha função: ",tamanho_da_lista(entrada))



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#def tamanho_palavra(palavra):
#    i = 0
#    for n in palavra:
#        i += 1
#    return i
#palavra = input()
#print("usando len(): ", len(palavra))
#print("usando minha função: ",tamanho_palavra(palavra))