from turtle import *
turtle = Turtle()
tela = Screen()
vez = 10
jogada = True
q1, q2, q3, q4, q5, q6, q7, q8, q9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
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
        linha = 2 -int((y + 226) // 100)
        coluna = 2 - int((x + 174) // 100)
        turtle.penup()
        turtle.goto(x, y)
        jogador = circulo(x, y) if jogada else xis(x, y)
        atualizar_tabuleiro(jogador)
    else:
        tela.textinput("Erro", "Olá, parece que você clicou fora da área de jogo,\npor favor clique dentro do tabuleiro (┬┬﹏┬┬)")

def atualizar_tabuleiro(jogador):
    global q1, q2, q3, q4, q5, q6, q7, q8, q9
    posicao = linha * 3 + coluna
    if posicao == 0:
        turtle.penup()
        turtle.goto(-105, 49)
        turtle.pendown()
        q1 = jogador
    elif posicao == 1:
        turtle.penup()
        turtle.goto(1, 49)
        turtle.pendown()
        q2 = jogador
    elif posicao == 2:
        turtle.penup()
        turtle.goto(107, 51)
        turtle.pendown()
        q3 = jogador
    elif posicao == 3:
        turtle.penup()
        turtle.goto(-109, -51)
        turtle.pendown()
        q4 = jogador
    elif posicao == 4:
        turtle.penup()
        turtle.goto(-5, -48)
        turtle.pendown()
        q5 = jogador
    elif posicao == 5:
        turtle.penup()
        turtle.goto(99, -58)
        turtle.pendown()
        q6 = jogador
    elif posicao == 6:
        turtle.penup()
        turtle.goto(-109, -154)
        turtle.pendown()
        q7 = jogador
    elif posicao == 7:
        turtle.penup()
        turtle.goto(-3, -153)
        turtle.pendown()
        q8 = jogador
    elif posicao == 8:
        turtle.penup()
        turtle.goto(99, -158)
        turtle.pendown()
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
    if q1 == q2 == q3 == 'X' or q1 == q2 == q3 == 'O':
        ganhador = True
    if q4 == q5 == q6 == 'X' or q4 == q5 == q6 == 'O':
        ganhador = True
    if q7 == q8 == q9 == 'X' or q7 == q8 == q9 == 'O':
        ganhador = True
    #verifica as colunas
    if q2 == q5 == q8 == 'X' or q2 == q5 == q8 == 'O':
        ganhador = True
    if q3 == q6 == q9 == 'X' or q3 == q6 == q9 == 'O':
        ganhador = True
    if q1 == q4 == q7 == 'X' or q1 == q4 == q7 == 'O':
        ganhador = True
    # Verificar diagonais
    if q1 == q5 == q9 == 'X' or q1 == q5 == q9 == 'O':
        ganhador = True
    if q3 == q5 == q7 == 'X' or q3 == q5 == q7 == 'O':
        ganhador = True

    ganhador == False

def reinicio():
    while True:
        resposta = tela.textinput("Reiniciar", "Agora que a partida acabou deseja jogar novamente? (sim/não): ").lower()
        if resposta == "sim":
            global jogada, vez, q1, q2, q3, q4, q5, q6, q7, q8, q9
            turtle.clear()
            jogada = True
            vez = 0
            q1, q2, q3, q4, q5, q6, q7, q8, q9 = ' ', ' ',' ', ' ',' ', ' ',' ', ' ',' '
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


listen()
tabuleiro()
onscreenclick(desenho)
mainloop() 