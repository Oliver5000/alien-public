import pgzrun
from pgzhelper import *
import random

HEIGHT = 400
WIDTH = 500

alien = Actor("alien") 
alien.x = 250
alien.y = 200
alien.scale = 0.001

flower = Actor("flower")
flower.x = 150
flower.y = 200

score = 0

game_over = False


def draw():
    screen.blit("background", (0,0))
    alien.draw()
    flower.draw()
    screen.draw.text("score: " + str(score), (200,350))
    if game_over:
        screen.fill("red")
        screen.draw.text("Times up! Your score is: " + str(score), (250,200))
        

def update():
    global score
    if keyboard.left:
        alien.x = alien.x - 3
    if keyboard.right:
        alien.x = alien.x + 3
    if keyboard.up:
        alien.y = alien.y - 3
    if keyboard.down:
        alien.y = alien.y + 3
    if alien.colliderect(flower):
        potato()
        score = score + 1
        
def potato():    
    flower.x = random.randint(50,450)
    flower.y = random.randint(50,350)

def timer():
    global game_over
    game_over = True

clock.schedule(timer, 15.0)

pgzrun.go()