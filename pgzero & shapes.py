import pgzrun   # import pygame zero library

from random import randint
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH = 300
HEIGHT = 300


def draw():
    r = 255
    g = 0
    b = randint(120, 255)

    width = WIDTH
    height = HEIGHT - 200

    screen.draw.filled_circle((150,150), 50.0,(0,200,0))

    
    for i in range(20):
        rect = Rect((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect, (r, g, b))

        r -= 10      # r = r-10
        g += 10     # g = g + 10

        width -= 10
        height += 10


pgzrun.go()