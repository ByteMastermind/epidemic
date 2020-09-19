import pygame
import random
import math

BLUE=(71,200,209)
RED = (229,52,70)
WHITE = (255,255,255)
BACKGROUND = (20, 20, 20)
WIDTH = 800
HEIGHT = 600
border = 10
width = 10
radius = 20
font_size = 17
x1 = 0
y1 = 0
x2 = 0
y2 = 0
people = 200
infected = 1
inf_counter = infected
citizen = [[0 for i in range(5)] for j in range(people)]
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

def counter():
    global infected
    infected = 0
    for i in range(people):
        if citizen[i][4] == 1:
            infected = infected + 1

def encounter(i):
    global infected
    for j in range(people):
        if (abs(citizen[j][0] - citizen[i][0]) <= radius) and (abs(citizen[j][1] - citizen[i][1]) <= radius):
            if citizen[j][4] == 1:
                probability = random.randint(1,200)
                if probability <= 2:
                    citizen[i][4] = 1
                    infected = infected + 1

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (70,20)
    gameDisplay.blit(TextSurf, TextRect)


pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
gameDisplay.fill(BACKGROUND)
pygame.display.set_caption('Corona is everywhere')
clock = pygame.time.Clock()

for i in range(people):
    randomness()
    citizen[i][0] = x1
    citizen[i][1] = y1
    citizen[i][2] = x2
    citizen[i][3] = y2
    if inf_counter > 0:
        citizen[i][4] = 1
        inf_counter = inf_counter - 1

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    for i in range(people):
        encounter(i)
        if citizen[i][4] == 1:
            pygame.draw.rect(gameDisplay, RED,(citizen[i][0],citizen[i][1],width,width))
        else:
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
    counter()
    message_display("INFECTED: " + str(infected))
    pygame.display.update()
    gameDisplay.fill(BACKGROUND)
    clock.tick(45)