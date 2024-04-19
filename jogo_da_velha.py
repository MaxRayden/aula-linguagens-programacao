
def bem_vindo():
    print('----------')
    print('Bem vindo ao jogo da Velha!')
    print('----------')

def exibe_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j])


#def marcar_jogo(jogador, a, b):

tabuleiro = [['','',''],
             ['','',''],
             ['','','']]
bem_vindo()
exibe_tabuleiro(tabuleiro)
