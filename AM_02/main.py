import pygame
from pygame.locals import *
import sys
import random
from ball import *

FPS = 60

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def callback_click():
    print("Click!!!")
    for b in balls:
        b.active = True

def ball_hit():
    global hits
    hits += 1

hits = 0
ball = Ball(window, 640, 480, True, ball_hit)
balls = [ball]
show_ship = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                show_ship = True
            if event.key == pygame.K_s:
                show_shop = False
            if event.key == pygame.K_d:
                new_ball = Ball(window, 620, 480, True, ball_hit)
                new_ball.x = 0
                new_ball.y = 0
                balls.append(new_ball)
            if event.key == pygame.K_f:     
                new_ball = Ball(window, 620, 480, True, ball_hit)
                new_ball.x = new_ball.max_width
                new_ball.y = 0
                balls.append(new_ball)
        if event.type == pygame.MOUSEBUTTONUP:
            callback_click()
    
    window.fill((0,0,0)) # fill black
    
    for b in balls:
        b.draw()
    
    ball.update()
        
    
    pygame.display.update()

    clock.tick(FPS)