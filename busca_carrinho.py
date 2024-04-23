def menu():
    opcoes = ('\n\n\tNOVA BUSCA\t|\tADICIONAR ITEM NO CARRINHO\t|\tVISUALIZAR ITENS NO CARRINHO')
    print(opcoes)
    busca, adicionar, visualizar = opcoes.strip(' ').split('|')
    print(busca, adicionar, visualizar)
    opcao = input('Digite a opção desejada: ')
    opcao = opcao.lower()
    contador = 0
    while contador != 0:
        if opcao == busca.lower():
            print ('deu ruim')
            contador +=1
        elif opcao == 'adicionar item no carrinho':
            print('sei lá')
            contador +=1
        elif opcao == 'visualizar iten no carrinho':
            print('outro sei lá')
            contador +=1
        else:
            contador = 0

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
        
welcome()
busca_produto()
menu()