import pygame
from pygame.locals import *
import random

class Ball:

    def __init__(self, window, window_width, window_height, enable_random, hit_callback):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        self.image = pygame.image.load('images/ball.png')
        self.sound = pygame.mixer.Sound('sounds/boing.wav')
        
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height
        
        self.active = False
        self.enable_random = enable_random
        self.x = (window_width - self.width) / 2
        self.y = (window_height - self.height) / 2
        
        self.initial_speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.speeds_list = [1, 2, 3, 4]
        self.x_speed = None
        self.y_speed = None
        
        self.hit_callback = hit_callback
        
        self.stop_req = False

    def update_pos(self, x, y):
        # if x or y is opposite, ignore them.
        if x >= 0:
            self.x = x
        if y >= 0:
            self.y = y
    
    def update(self):
        if self.enable_random:
            if self.x_speed is None:
                self.x_speed = random.choice(self.initial_speeds_list)
            if self.y_speed is None:
                self.y_speed = random.choice(self.initial_speeds_list)
        
        if self.active:
            if (self.x < 0) or (self.x >= self.max_width):
                self.x_speed = -self.x_speed
                self.sound.play()
                self.hit_callback()
                if self.stop_req:
                    self.stop_req = False
                    self.active = False
                
            
            if (self.y < 0) or (self.y >= self.max_height):
                 self.y_speed = -self.y_speed
                 self.sound.play()
                 self.hit_callback()
                 if self.stop_req:
                    self.stop_req = False
                    self.active = False
                
            self.x = self.x + self.x_speed
            self.y = self.y + self.y_speed
    
    def randomize(self):
        self.x_speed = random.choice(self.initial_speeds_list)
        self.y_speed = random.choice(self.initial_speeds_list)
        
    def reset(self):
        self.x = self.max_width / 2
        self.y = self.max_height / 2
                
        

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))