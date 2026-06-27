import pgzrun
import random
import time, math #optional
#screen dimensions
WIDTH = 900
HEIGHT = 700

#definiting colours
WHITE = (255,255,255)
BLUE = (0,0,255)

#create a ship
ship = Actor('galaga')
bug = Actor('bug')

ship.pos = (WIDTH//2, HEIGHT-30)

speed = 5

#define a list for bullets
bullets = []

#defining a list of enemies
enemies = []

#we want 8 enemies
for x in range(8): #no. of columns of enemies
    '''(Add code in Part 2 game)'''
    for y in range(4): # no. of rows of enemies
        enemies.append(Actor('bug'))
        #now the enemies will be in a straight line
        enemies[-1].x = 100+ 70*x  # 70*x is to set the dist b/w enemies & 100 = starting x pos.
        #starting off the screen thats why putting it at -80,
        #slowly the enemy will come down
        '''(Add code in Part 2 game)'''
        enemies[-1].y = -80 + 50*y # -80= starting y pos. 50*y is enemies's speed coming down
    
score = 0
direction = 1
'''(Add next 2 code ines in Part 2 game)'''
ship.dead = False
ship.countdown = 90 # to start the game after 90 secs(ship appers after 90 sec.)

#for updating the score
def displayScore():
    screen.draw.text(str(score), (50,30))

def gameOver():
    screen.draw.text("GAME OVER", (250,300))
    
def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:        
            bullets.append(Actor('bullet'))
            #the last bullet added , set its position
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 5

   
def update():
    global score
    global direction
    moveDown = False
    
    #move the ship left or right with arrow keys
    if ship.dead == False:
        if keyboard.left:
            ship.x -= speed
            if ship.x <= 0:
                ship.x = 0
                
        elif keyboard.right:
            ship.x += speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
    #to fire bullets
    #it should not be while you on hold space key event
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
            bullet.y -= 10
    
    #check the position of the last enemy
    '''(Add next 2code lines in Part 2 game)'''
    if len(enemies) == 0:
        gameOver()
        
    if len(enemies)>0  and (enemies[0].x < 80 or enemies[-1].x > WIDTH-80 ):
        moveDown = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x += 6*direction
        if moveDown == True:
            enemy.y += 1
        '''(Add next 2 code lines in Part 2 game)'''
        if enemy.y > HEIGHT :
            enemies.remove(enemy)
            
        #checking if the enemy hits a bullet while moving down
        #iterate over all the bullets and check for a collision
        for bullet in bullets :
            if enemy.colliderect(bullet):
                sounds.eep.play() #add sound, whn bullet hit the bug(enemy)
                score +=100
                #we also want to destory the bullet
                bullets.remove(bullet)
                #instead of removing the enemy we could send it back up?
                enemies.remove(enemy)
                '''(Add next 2 code lines in Part 2 game)'''
                if len(enemies) == 0:
                    gameOver()
        #checking for enemy hits the ship
        '''(Add next 3 code lines in Part 2 game)'''            
        if enemy.colliderect(ship):
            sounds.eep.play()#add sound, whn bug hit the ship
            ship.dead = True
    '''(Add next 5 code lines in Part 2 game)'''
    if ship.dead:
        ship.countdown -=1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90 # start the game after 90 secs(ship appers after 90 sec.)
            
    #==================
    #ADDITIONAL ACTIVITY
    '''
    enemy_speed_y = 2  # Add vertical speed for zig-zag movement

    # In the update function, modify enemy movement:
    for enemy in enemies:
        enemy.x += 3 * direction
        enemy.y += enemy_speed_y  # Add vertical speed
        if moveDown:  # Still move downward when hitting bounds
            enemy.y += 2
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
    
    #------------------------
    
    #FOR RANDOM MOVEMENT
    for enemy in enemies:
        enemy.x += random.choice([-5, 0, 5])  # Random horizontal movement
        enemy.y += random.choice([0, 5])  # Occasionally move downward
        if moveDown:
            enemy.y += 15
   
    #-----------------------------------
    # WAVE PATTERNS
    
    wave_amplitude = 50  # Height of the wave
    wave_frequency = 0.05  # Speed of the wave
    time = 0

   
    #global time
    time += wave_frequency
    for idx, enemy in enumerate(enemies):
        enemy.x += 5 * direction  # Normal horizontal movement
        enemy.y += wave_amplitude * math.sin(time + idx) * 0.1  # Wave motion
        if moveDown:
             enemy.y += 15
    
    '''
#=====================
                     
def draw():
    screen.clear()
    screen.fill(BLUE)
    #ship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    #ship to be drawn last
    if ship.dead == False:
        ship.draw()
    displayScore()
    if len(enemies) == 0:
        gameOver()
    
    
pgzrun.go()
