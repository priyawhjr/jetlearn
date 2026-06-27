import pgzrun           #step 1
import random
#screen dimensions
WIDTH = 750
HEIGHT = 600            #step 1
TITLE = "Galaga Game"     #step 1
#definiting colours
#WHITE = (255,255,255)
BLUE = (0,0,255) # RED = (255,0,0) Green=(0,255,0)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')
#specify initial position of ship 
ship.pos = (WIDTH//2, HEIGHT-60)  # OR ship.x = WIDTH//2
                                   # OR HEIGHT = HEIGHT-60
speed = 10

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

'''Next 3 lines should be replace by part 2 game code'''
enemies.append(bug)
#enemies.append(Actor('bug')) # adding bugs in enemies list
#now the enemies will be in a straight line
'''Replace enemies[-1].x = 10 to enemies[-1].x = 100 +70*x in part 2 game'''
enemies[-1].x = 100 # OR enemies[-1].x = random.randint(20,WIDTH-20) 

#starting enemies should be off the screen that's y putting it at y=-100 position,
#slowly the enemy will come down
enemies[-1].y = -100
    
score = 0
#direction=1 # (part 2 game line)

#for updating the score
def displayScore():
    screen.draw.text(str(score), (100,30),fontsize=50) # to display score at (100,30) position with white color

def on_key_down(key):
    if key == keys.SPACE: #press spacebar to add a bullet in list. any key with caps can be used(try A, P etc)       
        bullets.append(Actor('bullet'))
        
        #last bullet added, set its position. 
        #bullet[-1]=index of last bullet in list bullet 
        bullets[-1].x = ship.x 
        bullets[-1].y = ship.y - 50

# to update ship position. Moving it left or right   
def update():    #step 1
    global score
    #global direction # part 2 line
    #moveDown = False # part 2 line
    #move the ship left with arrow keys
    if keyboard.left:         # step 1
        ship.x -= 5 #to move ship left with a speed of 5
        if ship.x <= 0:
            ship.x = 0

    #move the ship right with arrow key        
    elif keyboard.right:      #Step 1
        ship.x += 5 #to move ship right with a speed of 5
        if ship.x >= WIDTH:
            ship.x = WIDTH
    #to fire bullets
    #it should not be while you on hold spapce key event
    #rather it should be on space key down event
    '''
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('bullet'))
        # the last bullet added , set its position
        bullets[-1].x = ship.x   # -1 is to represent. last bullet
        bullets[-1].y = ship.y
    '''
    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        '''top left window is (0,0) but as we move down, the y-coordinate will 
        increase for bullet .'''

        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10 # to move bullet up.
    '''Replace next 5 lines from part 2 game lines to create galaga 2 game'''
    for enemy in enemies:
        enemy.y += 2 # to move it straight down, increase the y-values
        #as the bug touches the bottom, make it go back up
        if enemy.y >= HEIGHT:
            enemy.y  = -100
            enemy.x = random.randint(50,WIDTH-50)
    
    
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                score +=100
                sounds.eep.play()
                #we also want to destory the bullet
                bullets.remove(bullet)
                #destroy the bug
                enemies.remove(enemy)
                             
def draw():                     # step 1
    screen.clear() # to clear screen (predefined method)
    screen.fill((0,0,255))#(BLUE) # predefined method
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()              # Step 1
    displayScore()
    
pgzrun.go()                # Step 1





















# https://www.youtube.com/watch?v=9xTiifL05GI -Part 1 Watch this
# https://www.youtube.com/watch?v=D-KnpqYVF1U - Part 2
# https://www.youtube.com/watch?v=5vWxkHUZJvk  - Part 3

