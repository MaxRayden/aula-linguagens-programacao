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
    if tabuleiro[linha][coluna] == ' ':
        tabuleiro[linha][coluna] = jogador

def atualiza_txt():
    string = tabuleio_string(tabuleiro)
    with open('tabuleiro.txt', 'w') as arquivo:
        arquivo.write(string)

def tabuleio_string(tabuleiro):
    string = ""
    for linha in tabuleiro:
        string += "|".join(linha) + "\n"
    return string

bem_vindo()
imprimir_tabuleiro(tabuleiro)
jogador = 'X'

while resultado != 0:
    print(f'É a vez do Jogador {jogador}, em qual posição você deseja jogar?\n>')
    jogada = input()
    linha, coluna = jogada.split(' ')
    linha = int(linha)
    coluna = int(coluna)
    marcar_jogada(jogador,linha,coluna)
    imprimir_tabuleiro(tabuleiro)
    atualiza_txt()
    #verifica_vitoria(resultado,tabuleiro,jogador)
    resultado = verifica_vitoria(resultado,tabuleiro,jogador)
    jogador = 'O' if jogador == 'X' else 'X'
print('Fim de Jogo')
    