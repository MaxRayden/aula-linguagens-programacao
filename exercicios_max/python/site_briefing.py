all_projects = []
rascunhos = []
def main():
    print('\n', '############## Bem Vindo ao BRIEFING.COM!!! ##############\n\n########################## MENU ##########################')
    print('\n\n\n|| 1.CRIAR || 2.MEU PORTIFÓLIO || 3.BUSCAR PROJETO || 4.SAIR ||", "\n\n\n')
    opcao_menu = input("DIGITE A OÇÃO DESEJADA:  \n>>")
    if opcao_menu == '1':
        funcao_criar()

def detalha_projeto():
    projeto = []
    resumo = input('Escreva um breve resumo sobre como seu projeto deve ser criado\n>>')
    while resumo =='':
        print('########## Campo Obrigatório ##########\n')
        resumo = input('Escreva um breve resumo sobre como seu projeto deve ser criado\n>>')
        projeto.append(resumo)
    
    prazo = int(input('Qual o prazo para entrega do seu projeto? (mínimo de 3 dias!!!)\n'))
    while prazo < 3:
        print('########## Digite um prazo de no mínimo 3 dias ##########\n')
        prazo = input('Qual o prazo para entrega do seu projeto? (mínimo de 3 dias!!!)\n')
        projeto.append(prazo)
    op = input('Deseja Enviar Projeto?(s/n)\n')
    opt = op.lower()
    while opt != 's' and opt != 'n':
        print('Digite s/n')
        op = input('>>')
        opt = op.lower()
    if op == 's':
        print('\n########## Projeto enviado com Sucesso! ##########\n')
        print(projeto)
    else:
        print('\n######## Seu rascunho foi salvo!! ########\n')
        print(projeto)

def funcao_criar():
    tipo_projeto = ['MOTION DESING','WEB-DESIGN','FILMAKER','LOGO','VETORIZAÇÃO']
    print('\n\n','Perfeito! Vamos criar um projeto! \n\nEscolha a categoria do projeto digitando uma das opçõeses: \n(1)-Motion-design\n(2)-Webdesign\n(3)-Filmaker\n(4)-Logo e Logotipo\n(5)-Vetorização\n\n')
    cat = int(input('\n>> '))
    while cat < 1 or cat > 5:
        print('########## Opção inválida ##########\nEscolha uma opção Válida\n')
        cat = input('\n>> ')
    if cat == 1:
        print(f'########## Projeto de {tipo_projeto[0]} ##########\n')
        detalha_projeto()
    elif cat == 2:
        print(f'########## Projeto de {tipo_projeto[1]} ##########\n')
        detalha_projeto()
    elif cat == 3:
        print(f'########## Projeto de {tipo_projeto[2]} ##########\n')
        detalha_projeto()
    elif cat == 4:
        print(f'########## Projeto de {tipo_projeto[3]} ##########\n')
        detalha_projeto()
    elif cat == 5:
        print(f'########## Projeto de {tipo_projeto[5]} ##########\n')
        detalha_projeto()

main()
