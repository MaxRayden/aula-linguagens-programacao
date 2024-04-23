from verifica_vitoria import verifica_vitoria
tabuleiro = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
resultado = ''
def bem_vindo():
    print('---------------')
    print('Bem vindo ao jogo da Velha!')
    print('---------------')

def imprimir_tabuleiro(tabuleiro):
    for linha in  range(3):
        print('|'.join(tabuleiro[linha]))
        if linha < 2:
            print('-' * 5)

def marcar_jogada (jogador,linha,coluna):
    cont = 0
    while cont == 0:
        if tabuleiro[linha][coluna] == ' 'and tabuleiro[linha][coluna] != 'X' and tabuleiro[linha][coluna] != "O":
            tabuleiro[linha][coluna] = jogador
            cont += 1
        else:
            print('o campo já está preenchido!')
            print(f'É a vez do Jogador {jogador}, em qual posição você deseja jogar?\n>')
            jogada = input()
            linha, coluna = jogada.split(' ')
            linha = int(linha)
            coluna = int(coluna)

def atualiza_txt():
    string = tabuleio_string(tabuleiro)
    with open('tabuleiro.txt', 'w') as arquivo:
        arquivo.write(string)

def tabuleio_string(tabuleiro):
    string = ""
    for linha in  range(3):
        string += '|'.join(tabuleiro[linha])+'\n'
        if linha < 2:
            string += '-'*5 +'\n'
               
    return string

bem_vindo()
imprimir_tabuleiro(tabuleiro)
jogador = 'X'

while resultado != 0:
    print(f'É a vez do Jogador {jogador}, em qual posição você deseja jogar?\n')
    jogada = input('>')
    linha, coluna = jogada.split(' ')
    linha = int(linha)
    coluna = int(coluna)
    marcar_jogada(jogador,linha,coluna)      
    imprimir_tabuleiro(tabuleiro)
    atualiza_txt()
    resultado = verifica_vitoria(resultado,tabuleiro,jogador)
    jogador = 'O' if jogador == 'X' else 'X'
    
print('Fim de Jogo')