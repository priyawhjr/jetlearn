import pgzrun
TITLE = 'Quiz Master'
W = 800
H = 500
marquee_box = Rect(0,0,800,80)#(starting x, starting y, width, height)
question_box = Rect(20,90,500,130)
timer_box = Rect(530,90,130,130)
ans_box1 = Rect(20,250,230,130)
ans_box2 = Rect(270,250,230,130)
ans_box3 = Rect(20,400,230,130)
ans_box4 = Rect(270,400,230,130)
skip_box = Rect(530,250,130,300)


answer_boxes = [ans_box1, ans_box2, ans_box3, ans_box4]

#variables:
score = 0
time_left = 15
marquee_message =''
is_game_over = False

question_file = 'Quiz Master/questions.txt'
questions = []
question_count = 0
question_index = 0

def draw():
    screen.fill('black')
    screen.draw.filled_rect(marquee_box,'blue')
    screen.draw.filled_rect(question_box,'magenta')
    screen.draw.filled_rect(timer_box, 'light blue')
    screen.draw.filled_rect(skip_box, 'green')


    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box,'yellow')

#marquee box text:

    marquee_message = 'Welcome to Quiz-Master...'
    marquee_message += f'Q: {question_index} of {question_count}'
    screen.draw.textbox(marquee_message,marquee_box,color = 'white')

    #adding timer box
    screen.draw.textbox(str(time_left),timer_box,color = 'green',shadow = (0.5,0.5),scolor = 'dim grey')
def update():
    move_marquee()

def move_marquee():
    marquee_box.x -=2 
    if marquee_box.right< 0:
        marquee_box.left = W

def read_question_file():
    pass

def read_nextques():
    pass

def on_mouse_down():
    pass

def correct_answer():
    pass

def game_over():
    pass

def skip_question():
    pass

def update_time_left():
    pass
