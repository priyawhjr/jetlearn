import pgzrun
import random

WIDTH = 300
HEIGHT = 300

'''
RED = 200, 0, 0
BOX = Rect((20, 20), (100, 100))
def draw():
    screen.draw.rect(BOX, RED)
'''

def draw():
    r = 255
    g = 0
    b = random.randint(120, 255)
    # to draw circle
    radius = 100

    for i in range(20):  # no. of circles
        #x = random.randint(radius, WIDTH - radius)  # Random x position within screen bounds
        #y = random.randint(radius, HEIGHT - radius)  # Random y position within screen bounds
        #screen.draw.circle((x,y), radius, (r, g, b))# circle at random pos on screen

        # to draw circle at center-> (WIDTH//2, HEIGHT//2)
        screen.draw.circle((WIDTH//2, HEIGHT//2), radius, (r, g, b))
        
        # to draw filled circle
        #screen.draw.filled_circle((WIDTH//2, HEIGHT//2), radius, (r, g, b))
        r -= 10
        g += 10
        radius -= 5




pgzrun.go()