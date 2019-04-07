from pplay.window import *
from pplay.sprite import *
from pplay.gameimage import *
from pplay.sound import *
import random
random.seed()
 
# janela = Window(517,310)
# player = Sprite("assets/imgs/farmer2.png")
# player.set_position(300,100)
# fundo = GameImage("assets/imgs/bg.png")
# speed_per_FRAME = 300
# speed_per_SECOND = 1

GAME_SPEED = 1
 
GAME_STATE = 0 
"""
Controla em que estágio o jogo se encontra:
0 - Menu Inicial
1 - Jogo
2 - Finalização do jogo (Pontuação)
"""

# ============JANELA===========
width = 517
height = 310
background_color = [0, 0, 0]
title = "Space Invaders"


window = Window(width, height)
window.set_title(title)
window.set_background_color(background_color)

#Background Image - 2 para scrolling
background_01 = GameImage("assets/imgs/bg.png")
background_02 = GameImage("assets/imgs/bg.png")

# Posições iniciais
background_01.y = 0
background_02.y = -background_02.height

# Velocidade de rolagem
background_roll_speed = 50

# teclado e mouse
keyboard = window.get_keyboard()
mouse = window.get_mouse()


# ==========JOGAR===========
# Sprite da nave do jogador
player = Sprite("assets/imgs/farmer2.png")
 
# Posição inicial
player.set_position((window.width - player.width)/2,
                        (window.height - player.height))

# Velocidade do jogador
player.speed = 200
 
# Direção do jogador
player.direction = -1  # [cima]
 
# Pontuação
player.score = 0



# Tamanho limite da matriz
MAXSIZE = 10

# Numero de linhas da matriz
matrix_x = 10
 
# Numero de coluna da matriz
matrix_y = 5

# Associar uma variável à instância de teclado contida em Window
teclado = Window.get_keyboard()  # Função da CLASSE e não da instância! W maiúsculo!

 
while(True):
    janela.set_background_color((255,255,255))
     
    if(teclado.key_pressed("UP")):  # Direcional ^
        player.move_y(-speed_per_FRAME * janela.delta_time())
    if(teclado.key_pressed("DOWN")):  # Direcional \/
        player.move_y(speed_per_FRAME * janela.delta_time())
    if(teclado.key_pressed("LEFT")):  # Direcional 
        player.move_x(-speed_per_FRAME * janela.delta_time())
    if(teclado.key_pressed("RIGHT")):  # Direcional 
        player.move_x(speed_per_FRAME * janela.delta_time())
     
    if(teclado.key_pressed("ESC")):  # Esc, escape..
        janela.close()  # Fecha o programa


        # Irá se mover 60 pixels a cada FRAME - sumirá da tela instantaneamente
    
     
    # Irá se mover 60 pixels a cada SEGUNDO - independente do processador
    # kobra.move_x(speed_per_SECOND * janela.delta_time())
    fundo.draw()
    player.draw()
     
    janela.update()   