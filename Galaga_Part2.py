import pgzrun
import random
#screen dimensions
W = 950
H = 650

#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')
ship.pos = (W//2, H-60)

speed = 2

bullets = [] #define a list for bullets

enemies = [] #defining a list of enemies

'''(Add code in Part 1 game)'''
for x in range(10): #we want 8 enemies
    enemies.append(Actor('bug'))
    #now all the enemies will be in a straight line
    enemies[-1].x = 100+ 70*x # to get more dist. b/w enemies, increase 70*x else vise-versa
    #starting off the screen thats why putting it at enemies[-1].y=-30 or enemies[-1].y = -100,
    #slowly the enemy will come down
    enemies[-1].y =-30
    
score = 0
'''(Add code in Part 1 game)'''
direction = 1 #to move bugs left 1st.To rgt, direction=-1
#for updating the score
def displayScore():
    screen.draw.text(str(score), (50,30),fontsize=50,color='red') # to display score at (100,30) position with white color

def on_key_down(key):
    if key == keys.SPACE:        
        bullets.append(Actor('bullet'))
        #the last bullet added, set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

   
def update():
    global score
    '''(Add code in Part 1 game)'''
    global direction 
    '''(Add code in Part 1 game)''' 
    moveDown = False 
    #move the ship left or right with arrow keys
    if keyboard.left:
        ship.x -= 5
        if ship.x <= 0:
            ship.x = 0
    #move the ship right with arrow key           
    elif keyboard.right:
        ship.x += speed
        if ship.x >= W:
            ship.x = W
    #to fire bullets
    #it should not be while you on hold spapce key event
    #rather it should be on space key down event
    '''
    if keyboard.space:
        print("Pressing space")
        bullets.append(Actor('bullet'))
        #the last bullet added , set its position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y
    '''
    for bullet in bullets:
        #if the bullet reaches the top of the screen it should get removed
        #else the list will become huge
        if bullet.y <=0 :
            bullets.remove(bullet)
        else:
            bullet.y -= 10 # to move bullet up
    
    #check the position of the last enemy
    #if total no. of enemies>0 & (0 index enemy's x pos<20 or 
    # last index enemy's x pos > W-30)
    '''(Add next 7 lines in Part 1 game)'''
    if len(enemies)>0  and (enemies[0].x < 20  or enemies[-1].x > W-30):
        moveDown = True
        direction = direction*(-1) #to move in opposite direction(left to right 
        #or right to left)
    for enemy in enemies:
        enemy.x += 5*direction #to inc./dec. enemy speed horizontally, chg this no.
        if moveDown == True:
            enemy.y += 10#to inc./dec. enemy's speed to come down, inc/dec this no. 
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                '''(Add code in part 1 game)'''
                sounds.eep.play() # to add sound 
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                enemies.remove(enemy)
        
                     
def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    ship.draw()
    displayScore()
    
pgzrun.go()              
