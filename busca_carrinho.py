def menu_inicial():
    opcoes = ('\n\n\tNOVA BUSCA\t|\tADICIONAR ITEM NO CARRINHO\t|\tFINALIZAR COMPRA')
    print(opcoes)
    opcao = input('Digite a opção desejada: ')
    opcao = opcao.lower()
    if opcao == 'nova busca':
        busca_produto()
    elif opcao == 'adicionar item no carrinho':
        print('sei lá')
        return opcao
    elif opcao == 'finalizar compra':
        print('outro sei lá')

def welcome():
    print('Seja Bem vindo!')
    print('-'*10)

def busca_produto():
    with open ('produtos.csv', 'r') as arquivo:
        next(arquivo)
        lista_linhas = arquivo.readlines()
        busca =(input('Digite o que você procura: '))
        busca = busca.lower() 
    contador  = 0
    for linha in lista_linhas:
        produto, categoria, valor, quantidade, codigo = linha.strip('\n').split(',')
        if busca in produto.lower() or busca in categoria.lower () or busca in codigo.lower():
            print(f'Produto: {produto} | Código: {codigo} | Quantidade Disponível: {quantidade} \t|\t Valor: R$ {float(valor):.2f}')
            contador += 1
            if contador == 5:
                break
    else:
        print('Produto indisponível!')

def adiciona_item(carrinho):
    item = input('Para adicionar um item ao carrinho digite o ódigo do item desejado:\n>> ')
    with open ('produtos.csv', 'r') as arquivo:
        next(arquivo)
        todos_itens = arquivo.readlines()
        item = input('Para adicionar um item ao carrinho digite o ódigo do item desejado:\n>> ')
        for linha in todos_itens:
            produto, categoria, valor, quantidade, codigo = linha.strip('\n').split(',')
            if item in codigo:
                carrinho.append(linha)
                print(carrinho)
                break
            else:
                print('Produto não encontrado! ')

    
    carrinho.append(item)
    return carrinho

carrinho = []     
#welcome()
busca_produto()
#menu_inicial()
adiciona_item(carrinho)
print(carrinho)