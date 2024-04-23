#def busca_produto():
with open ('produtos.csv', 'r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()
    busca =(input('Digite um produto: '))
    busaca = busca.lower()
contador = 0   

for linha in lista_linhas:
    produto, categoria, valor, quantidade, codigo = linha.strip('\n').split(',')
    if busca in produto.lower() or busca in categoria.lower () or busca in codigo.lower():
        print(linha)
