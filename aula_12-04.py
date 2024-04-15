def tamanho_lista(lista):
    contador = 0
    for elemento in lista:
        contador +=1
    return contador

def tamanho_palavras(lista):
    qtd_palavras = tamanho_lista(lista)
    print('quantidade de palavras na lista:', qtd_palavras)
    posicao = 1
    for palavra in lista:
        print('quantidade de letras na palavra', posicao,':', tamanho_lista(palavra) )
        posicao += 1

lista = ["oii", "tubem", "palavra", "quadro"]
tamanho_palavras(lista)
