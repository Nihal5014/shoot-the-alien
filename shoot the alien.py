import pgzrun
import random

WIDTH = 750
HEIGHT = 750
counter = 0
score = 0
nihal = Actor('alien_image')
nihal.pos=(375,375)
def draw():
    screen.fill('dark blue')
    nihal.draw()
    screen.draw.text(str(score),(75,75),color='light green')

def on_mouse_down(pos):
    global score   
    if nihal.collidepoint(pos):
        nihal.pos = (random.randint(50,700),random.randint(50,700))
        score = score+1
        
def update():
    global counter
    counter = counter+1 
    if counter %60 == 0:
        nihal.pos = (random.randint(50,700),random.randint(50,700))


pgzrun.go()

    