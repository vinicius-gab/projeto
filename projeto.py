from turtle import *
turtle = Turtle()
tela = Screen()
vez = 0
jogada = True
tabuleiro_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ganhador = False
linha = 0
coluna = 0

def jump_O(x, y):
    turtle.penup()
    turtle.goto(x - (x % 100) + 50, y - (y % 100) + 50)
    turtle.pendown()

def jump_x(x, y):
    turtle.penup()
    turtle.goto(x + (x % 2) + 4, y - (y % 100) + 52)
    turtle.pendown()

def tabuleiro():
    turtle.color("black")
    turtle.pensize(5)
    turtle.shape("blank")
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.speed(0) 
    turtle.penup()
    turtle.pensize(4)
    turtle.goto(-150, 0)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-150, -100)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(-50, -200)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(300)

def trocar(x, y):
    global jogada
    if jogada:
        jump_O(x, y)
        circulo(x, y)
    else:
        jump_x(x, y)
        xis(x, y)

def desenho(x, y):
    global jogada, linha, coluna
    if -174 <= x <= 169 and -226 <= y <= 150:
        linha = 2 - int((y + 226) // 100)
        coluna = 2 - int((x + 174) // 100)
        posicao = linha * 3 + coluna
        if tabuleiro_status[posicao] == ' ':
            turtle.penup()
            turtle.goto(x, y)
            jogador = circulo(x, y) if jogada else xis(x, y)
            tabuleiro_status[posicao] = jogador
            verificar_vencedor()
            vitoria()
        else:
            tela.textinput("Erro", "Ops, parece que aqui já tem um desenho, por favor desenhe em outro lugar 〒▽〒")
    else:
        tela.textinput("Erro", "Olá, parece que você clicou fora da área de jogo,\npor favor clique dentro do tabuleiro (┬┬﹏┬┬)")

def atualizar_tabuleiro(jogador):
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    posicao = linha * 3 + coluna
    if posicao == 0:
        q1 = jogador
    elif posicao == 1:
        q2 = jogador
    elif posicao == 2:
        q3 = jogador
    elif posicao == 3:
        q4 = jogador
    elif posicao == 4:
        q5 = jogador
    elif posicao == 5:
        q6 = jogador
    elif posicao == 6:
        q7 = jogador
    elif posicao == 7:
        q8 = jogador
    elif posicao == 8:
        q9 = jogador

    verificar_vencedor()
    vitoria()

def circulo(x, y):
    global jogada, vez
    jump_O(x, y)
    turtle.color("blue")
    turtle.pensize(10)
    turtle.circle(45)
    jogada = not jogada
    vez += 1
    return 'O'

def xis(x, y):
    global jogada, vez
    jump_x(x, y)
    turtle.pensize(20)
    turtle.color('red')
    turtle.right(45)
    turtle.forward(50)
    turtle.backward(100)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(100)
    turtle.right(45)
    jogada = not jogada
    vez += 1
    return 'X'

def verificar_vencedor():
    global ganhador
    # Verificar linhas
    if tabuleiro_status[0] == tabuleiro_status[1] == tabuleiro_status[2] != ' ':
        ganhador = True
    elif tabuleiro_status[3] == tabuleiro_status[4] == tabuleiro_status[5] != ' ':
        ganhador = True
    elif tabuleiro_status[6] == tabuleiro_status[7] == tabuleiro_status[8] != ' ':
        ganhador = True
    # Verificar colunas
    elif tabuleiro_status[0] == tabuleiro_status[3] == tabuleiro_status[6] != ' ':
        ganhador = True
    elif tabuleiro_status[1] == tabuleiro_status[4] == tabuleiro_status[7] != ' ':
        ganhador = True
    elif tabuleiro_status[2] == tabuleiro_status[5] == tabuleiro_status[8] != ' ':
        ganhador = True
    # Verificar diagonais
    elif tabuleiro_status[0] == tabuleiro_status[4] == tabuleiro_status[8] != ' ':
        ganhador = True
    elif tabuleiro_status[2] == tabuleiro_status[4] == tabuleiro_status[6] != ' ':
        ganhador = True
    else:
        ganhador = False
    vitoria()

def reinicio():
    while True:
        resposta = tela.textinput("Reiniciar", "Agora que a partida acabou deseja jogar novamente? (sim/não): ").lower()
        if resposta == "sim":
            global tabuleiro_status, jogada, vez
            turtle.clear()
            jogada = True
            vez = 0
            tabuleiro_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            tabuleiro()
            break
        elif resposta == "não":
            tela.bye()
            break
        else:
            tela.textinput("Erro", "Parece que você digitou algo que não é uma das opções, por favor digite 'sim' ou 'não'")

def vitoria():
    global ganhador
    if ganhador == True:
        tela.textinput("Fim de jogo", "O jogo acabou com uma vitoria (☆▽☆)")
        reinicio()

def verificar_empate():
    global ganhador
    if ' ' not in tabuleiro and not ganhador:
        tela.textinput("Empate", "O jogo empatou. Quer jogar novamente? (sim/não): ")
        reinicio()

listen()
tabuleiro()
onscreenclick(desenho)
mainloop() 