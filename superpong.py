from pplay.window import *
from pplay.sprite import *
from pplay.gameimage import *
from pplay.sound import *
import random
random.seed()
 

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
title = "Super Pong"
red = (255,0,0)

window = Window(width, height)
window.set_title(title)
window.set_background_color(background_color)


player = pygame.draw.rect(window, red, [400,300,10,100])

# teclado e mouse
keyboard = window.get_keyboard()
mouse = window.get_mouse()



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


    
    
    player.draw()
     
    janela.update()   