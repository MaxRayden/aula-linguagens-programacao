carrinho = []  
        
def welcome():
    print('Seja Bem vindo!')
    print('-'*10)

def busca_produto():
    with open ('produtos.csv', 'r', encoding='utf-8') as arquivo:
        next(arquivo)
        lista_linhas = arquivo.readlines()
        busca =(input('Digite o que você procura: '))
        busca = busca.lower() 
    contador  = 0
    for linha in lista_linhas:
        produto, categoria, valor, quantidade, codigo = linha.strip('\n').split(',')
        if busca in produto.lower() or busca in categoria.lower () or busca in codigo.lower():
            print(f'Produto: {produto.ljust(40)} | Código: {codigo} | Quantidade Disponível: {quantidade} \t|\t Valor: R$ {float(valor):.2f}')
            contador += 1
            if contador == 5:
                break
    else:
        print('Produto indisponível!')

def adiciona_item(carrinho):
    with open ('produtos.csv', 'r', encoding='utf-8') as arquivo:
        next(arquivo)
        todos_itens = arquivo.readlines()
        prod = input('Para adicionar um item ao carrinho digite o código do item desejado:\n>> ')
        item = prod.upper()
        qtd = int(input(f"Digite a quantidade que deseja adicionar ao carrinho\n>>"))
        for linha in todos_itens:
            
            produto, categoria, valor, quantidade, codigo = linha.strip('\n').split(',')
            if item == codigo:
                for i in range(qtd):
                    carrinho.append(codigo+','+produto+','+valor)
                print('\nProduto Adicionado com Sucesso!\n')
                break
        else:
            print('Produto não encontrado')
    return carrinho

def visualizar_carrinho(carrinho):
    if not len(carrinho) == 0:
        soma = 0
        qtd = 1
        print('\n\n\t\tCARRINHO')
        for item in carrinho:
            linha = item.split(',')
            print(qtd,'.Produto',linha[1],'\t|\t','R$ ',linha[2])
            qtd+=1
            soma = soma + float(linha[2])
            soma_arredondada = round(soma, 2)
        print(f'TOTAL:\t\t\t\t R$ {soma_arredondada}')
    else:
        print('carrinho vazio')

def menu_meio(carrinho):
    opcoes = ('\n\n\t1.NOVA BUSCA\t|\t2.ADICIONAR ITEM NO CARRINHO\t|\t3.VISUALIZAR CARRINHO\t|\t4.FINALIZAR COMPRA')
    print(opcoes)
    opcao = input('Digite a opção desejada: (1 , 2 , 3 , 4)\n>')
    opcao = opcao.lower()
    if opcao == '1':
        busca_produto()
    elif opcao == '2':
        carrinho = adiciona_item(carrinho)
    elif opcao == '4':
        visualizar_carrinho(carrinho)
        return 0
    elif opcao == '3':
        visualizar_carrinho(carrinho)
        
welcome()
busca_produto()

while len(carrinho) == 0:
    opcoes = ('\n\n\t1.NOVA BUSCA\t|\t2.ADICIONAR ITEM NO CARRINHO\t|\t3.FINALIZAR COMPRA')
    print(opcoes)
    opcao = input('Digite a opção desejada: (1 , 2 , 3)\n>')
    opcao = opcao.lower()
    if opcao == '1':
        busca_produto()
    elif opcao == '2':
        carrinho = adiciona_item(carrinho)
    elif opcao == '3':
        if not carrinho:
            print('Saindo....')
            break
        else:
            visualizar_carrinho
            print('Compra Finalizada....')
            break
if not len(carrinho) > 0:
    exit(0)
contador = 1
while contador != 0:          
    contador = menu_meio(carrinho)
print('saindo...')