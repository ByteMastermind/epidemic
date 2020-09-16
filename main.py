import pygame
import random
import math

BLUE=(0,0,255)
WIDTH = 800
HEIGHT = 600
border = 10
width = 10
x1 = 0
y1 = 0
x2 = 0
y2 = 0
people = 100
citizen = [[0 for i in range(4)] for j in range(people)]
velocity = 0.5

def randomness():
    global x1, y1, x2, y2, velocity
    z = random.randint(0,1)
    x1 = random.randint(0, WIDTH - width)
    y1 = random.randint(0,HEIGHT - width)
    x2 = random.uniform(-velocity, velocity)
    y2 = math.sqrt( (velocity**2) - (x2**2) )
    if z == 1:
        y2 = -y2



pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
gameDisplay.fill([88, 83, 83])
pygame.display.set_caption('Corona is everywhere')
clock = pygame.time.Clock()

for i in range(people):
    randomness()
    citizen[i][0] = x1
    citizen[i][1] = y1
    citizen[i][2] = x2
    citizen[i][3] = y2


crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    for i in range(people):
        pygame.draw.rect(gameDisplay, BLUE, (citizen[i][0],citizen[i][1],width,width))



    for i in range(people):
        citizen[i][0] = citizen[i][0] + citizen[i][2]
        citizen[i][1] = citizen[i][1] + citizen[i][3]
        if (citizen[i][0] ) >= WIDTH - width:
            citizen[i][2] = -citizen[i][2]
        if (citizen[i][0]) <= 0:
            citizen[i][0] = -citizen[i][0]
            citizen[i][2] = -citizen[i][2]
        if citizen[i][1] <= 0:
            citizen[i][1] = -citizen[i][1]
            citizen[i][3] = -citizen[i][3]
        if citizen[i][1] >= HEIGHT - width:
            citizen[i][1] = HEIGHT - 2*width - (citizen[i][1] - HEIGHT)
            citizen[i][3] = -citizen[i][3]


    pygame.display.update()
    gameDisplay.fill([88, 83, 83])
    clock.tick(30)