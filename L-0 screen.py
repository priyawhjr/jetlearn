import pgzrun

TITLE = "Quiz Master"
WIDTH=500
HEIGHT=300

#------To draw rectangle------

#START multiline comment
red = (255,0,0) #clr
     #Rect((start x_coor,start y_coor),(w,h))
BOX = Rect((220, 20), (200, 100)) # rectangle
BOX2 = Rect((20, 200), (50, 50)) 
        #or
#BOX = Rect((100, 120), (100, 100)) # for square

def draw():
    #screen.draw.rect(Rect((start x_coor,start y_coor),(w,h)),clr)
    screen.draw.rect(BOX,red)
    screen.draw.rect(BOX2,red)

    #to draw line
    #screen.draw.line((start_x,start_y),(end_x,end_y), color)
    screen.draw.line((10,50),(150,50),'yellow')

    #To draw circle
    #screen.draw.circle((Center_x,Center_y),radius,color)
    screen.draw.circle((250,150),20,'orange')

# END multiline comment
#---------------------------------

pgzrun.go()
#---------------------------------------
'''
Python pygame, pgzero and Visual Studio Code Set up

Link

Recommended platform:

Visual Studio Code with Backing up the files on https://replit.com/

For learners who are still not ready for Visual Studio Code continue with https://replit.com/ preferably moving them to Visual Studio Code by the end of the course.

All the upcoming modules in Python should be conducted in Visual Studio Code

Github repository creation

Github repository creation process'''