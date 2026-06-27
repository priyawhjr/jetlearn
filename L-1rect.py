# display 20 rectangles with changing colors and sizes on the screen.
import pgzrun,random #used to run the Pygame Zero game loop.
#import random # or from random import randint

#width and height of the game window.
WIDTH = 300
HEIGHT = 300
TITLE='RECTANGLE PATTERN'
#-----------Box fig-------------
#'draw() function is called repeatedly to draw things on the screen.

def draw():

    r = 255 # 'r' starts at 255 (maximum red), 
    g = 0  # 'g' starts at 0 (no green)
    b = random.randint(120, 255) #'b'-set a random value b/w 120 and 255.
    # or randint(120,255) ,only if - from random import randint

    width = WIDTH-200 #set initial values for width and height of the rectangles.
    height = HEIGHT - 200#-200

    for i  in range(20): # no. of rectangles
        '''create a 'rect'object inside the loop, 
        which is then updated with new dimensions 
        each iteration.''' #Rect object representing a rectangle
        #its top-left corner at (0, 0) and its dimensions as width and height.
        rect = Rect((0,0), (width, height)) #
      
        rect.center = 150, 150 #sets the center of the rect 
        screen.draw.rect(rect, (r, g, b))
        # below code to draw filled rectangle
        '''screen.draw.filled_rect(rect, (r, g, b))'''       
        #dec. r by 10 and inc. g by 10 for the next iteration,to chg the color towards green.
        r -= 10
        g += 10

        width -= 10
        height -= 10

#-----------------
'''this line starts the Pygame Zero game loop, 
which will repeatedly call the draw() function to update the screen.'''
pgzrun.go()

