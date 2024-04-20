def verifica_vitoria(resultado, tabuleiro,jogada):
    resultado = ' '
    for linha in tabuleiro:
        for jogada in linha:
            if jogada == ' ':
                resultado = 'o jogo ainda não acabou'
    
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            resultado = linha[0]+' Ganhou!'
            print (resultado)
            return 0
    for coluna in [0,1,2]:
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            resultado = tabuleiro[0][coluna]+' Ganhou!'
            print (resultado)
            return 0
    if tabuleiro [0][0] == tabuleiro[1][1] == tabuleiro[2][2] or tabuleiro [2][0] == tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[1][1] != ' ':
        resultado = tabuleiro[1][1]+' Ganhou!'
        print (resultado)
        return 0
    if resultado == ' ':
        resultado = 'Empate'
        print (resultado)
        return 0