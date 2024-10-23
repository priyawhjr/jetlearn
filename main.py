import pgzrun
from random import randint
TITLE = 'Shoot the Alien'
WIDTH = 500
HEIGHT = 500

msg = ''

alien = Actor("alien")

def draw():
    screen.clear()
    screen.fill(color=(128,0,0))
    alien.draw()

    screen.draw.text(msg, center = (250,25),fontsize = 30, color = ("yellow"))

def place_alien():
    alien.x = randint(100,450)
    alien.y = randint(100,450)

def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
        msg = "GOOD SHOT!"
        place_alien()

    else:
        msg = "YOU MISSED!"

place_alien()

pgzrun.go()
