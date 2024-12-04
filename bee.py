import pgzrun
import random
import time

WIDTH = 600
HEIGHT = 500

#variables
score = 0
game_over = False

# using Actor() to get images
bee = Actor('bee')
flower = ACtor('flower')
#positioning of images
bee.pos = (100,100)
flower.pos = (60,40)

# variable to display message
msg =' '

def draw():
    pass

def place_flower():
    flower.x = random.randint(30, (WIDTH - 30))
    flower.y = random.randint(30,(HEIGHT - 30))

def time_up():
    global game_over
    game_over = True

def update():
    pass

clock.schedule(time_up, 30.0)










pgzrun.go()
