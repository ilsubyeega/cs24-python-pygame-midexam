import pygame
from pygame.locals import *
import sys
import random
from button import *
from ball import *
from text import *

FPS = 60

pygame.init()
window = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def callback_start():
    global ball
    print("Start!!!")
    ball.reset()
    ball.randomize()
    ball.active = True
    
def callback_stop():
    global ball
    print("Stop!!!")
    ball.stop_req = True
    
def callback_reset():
    global ball, ticks, hits
    print("Reset!!!")
    ball.reset()
    
    ticks = 0
    hits = 0

def ball_hit():
    global hits
    hits += 1

bgm = pygame.mixer.Sound('sounds/background.mp3')
button_start = Button(window, (20, 428), "images/button_start_none.png", "images/button_start_hovered.png", "images/button_start_pressed.png", callback_start)
button_stop = Button(window, (164, 428), "images/button_stop_none.png", "images/button_stop_hovered.png", "images/button_stop_pressed.png", callback_stop)
button_reset = Button(window, (308, 428), "images/button_reset_none.png", "images/button_reset_hovered.png", "images/button_reset_pressed.png", callback_reset)

ball = Ball(window, 640, 480, True, ball_hit)

ticks = 0
hits = 0
text_tick = Text(window, (520, 0), "00m 00s 00", text_color=(255, 255, 255))
text_hits = Text(window, (0, 0), "0 times", text_color=(255, 255, 255))

bgm.play()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        button_start.handle_event(event)
        button_stop.handle_event(event)
        button_reset.handle_event(event)
    
    window.fill((0,0,0)) # fill black
    ball.update()

    
    if ball.active:
        ticks += 1
    
    minutes = int(ticks / FPS / 60)
    seconds = int(ticks / FPS % 60)
    frames = int(ticks % 60 % 60)
    text_tick.set_value(f'{minutes:02d}m {seconds:02d}s {frames:02d}')
    text_hits.set_value(f'{hits} hits')
    
    
    ball.draw()
    text_tick.draw()
    text_hits.draw()    
    button_start.draw()
    button_stop.draw()
    button_reset.draw()
    
    pygame.display.update()

    clock.tick(FPS)