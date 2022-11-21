# Thanks goes to @SahruzRiyad

import pygame
import math
import numpy as np

# print("Enter Fighter Initial Position")
# fighter_pos = [int(input()) , int(input())]

# print("Enter Fighter Velocity")
# VF = int(input())

VF = 20
fighter_pos = (50,50)

pygame.init()
pygame.display.set_caption("Pure Pursuit")

width , height = 1000 , 800
screen = pygame.display.set_mode((width , height))

f = pygame.font.get_default_font()
font = pygame.font.SysFont(f , 45)

boomberPos = font.render("B" , True , (255,0,0) , (0,0,0))
fighterPos = font.render("F" , True , (0,255,0) , (0,0,0))
caught = font.render("Caught" , True , (0,255,0) , (0,0,0))
escaped = font.render("Escaped" , True , (255,0,0) , (0,0,0))

textRect1 = boomberPos.get_rect()
textRect2 = fighterPos.get_rect()
textRect3 = caught.get_rect()
textRect4 = escaped.get_rect()

def calcDistance(fighter_pos , boomber_pos):
    x = pow(boomber_pos[0] - fighter_pos[0] , 2)
    y = pow(boomber_pos[1] - fighter_pos[1] , 2)
    return math.sqrt(x+y)
    
t = 0
prev_fighter_pos = (0,0)
prev_boomber_pos = (0.0)
running = True 


while running:
    pygame.time.delay(600)

    timerPos = font.render("Time: "+str(t) , True , (255,255,255) , (0,0,0))
    textRect5 = timerPos.get_rect()
    textRect5.center = (90,height-50)
    screen.blit(timerPos , textRect5)

    x = np.random.randint( 10 , width - 100)
    y = np.random.randint(10 , height - 100)
    boomber_pos = (x,y)

    if t == 0:
        textRect1.center = boomber_pos ; textRect2.center = fighter_pos
        screen.blit(boomberPos , textRect1) ; screen.blit(fighterPos , textRect2)

    else :
        pygame.draw.line(screen , (255,0,0) , prev_boomber_pos , boomber_pos , 2)
        pygame.draw.line(screen , (0,255,0) , prev_fighter_pos , fighter_pos , 2)
        pygame.draw.circle(screen , (255,255,255) , fighter_pos , 4)
        pygame.draw.circle(screen , (255,255,255) , boomber_pos , 4)
    
    
    dist = calcDistance(fighter_pos , boomber_pos)

    if t > 15:
        textRect4.center = (width / 2 , height / 2)
        screen.blit(escaped , textRect4)
        running = False

    if dist <= 100 : 
        textRect3.center = (width / 2 , height / 2)
        screen.blit(caught , textRect3)
        running = False
    
    prev_boomber_pos = boomber_pos
    prev_fighter_pos = fighter_pos


    x = fighter_pos[0] + (VF * ((boomber_pos[0] - fighter_pos[0]) / dist))
    y = fighter_pos[1] + (VF * ((boomber_pos[1] - fighter_pos[1]) / dist)) 
    fighter_pos = (x,y)

    t += 1
    pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()
    
