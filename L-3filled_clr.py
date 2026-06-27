import pgzrun   # import pygame zero library

from random import randint
# Pygame Standard for deciding the width and height for your game window in pixels
WIDTH = 300
HEIGHT = 300
TITLE="Filled Shapes with pgzrun"

def draw():
    r = 255
    g = 0
    b = randint(120, 255)

    width = WIDTH-90
    height = HEIGHT - 270
    rect1 = Rect((20,40),(width,height))
    rect2 = Rect((20,132),(width,height))
    rect3 = Rect((20,202),(width,height)) # declare for text box    

    screen.draw.text('Rectangle',(50,15), color='yellow') # TO CREATE OUTLINE OF RECTANGLE
    screen.draw.rect(rect1,(r,0,b))
        
    screen.draw.filled_circle((100,100), 20,(0,200,0)) # filled_circle(pos,radius,(r,g,b))
    screen.draw.circle((200,100), 20,(235,255,200)) # OUTLINE OF circle
    
    screen.draw.text(' Filled Rectangle',(50,170)) 
    screen.draw.filled_rect(rect2,(r,g,b))
    screen.draw.textbox('I m Text box',rect3) # to create TEXT BOX

pgzrun.go()
#==============================================================
'''
 #           H.W.
# Draw the flag with 3 filled rectangles (blue, white & red)
# Solution: 

import pgzrun

WIDTH = 600
HEIGHT = 400
def draw():
  screen.fill((255, 255, 255))
  #Fill the screen with white

    #Draw the blue of the flag
  screen.draw.filled_rect(Rect((0, 0), (WIDTH / 3, HEIGHT)), (0, 85, 164))

    #Draw the white of the flag
  screen.draw.filled_rect(Rect((WIDTH / 3, 0), (WIDTH / 3, HEIGHT)), (255, 255, 255))

    #Draw the red of the flag
  screen.draw.filled_rect(Rect((2 * WIDTH / 3, 0), (WIDTH / 3, HEIGHT)), (239, 65, 53))

pgzrun.go()
'''