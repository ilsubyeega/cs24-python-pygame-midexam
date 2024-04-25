import pygame
from pygame.locals import *

class Button:
    STATUS_NONE = 'none'
    STATUS_HOVERED = 'hovered'
    STATUS_PRESSED = 'pressed'
    
    def __init__(self, window, loc, state_none_image_path, state_hovered_image_path, state_pressed_image_path, callback):
        self.window = window
        self.loc = loc
        self.surface_none = pygame.image.load(state_none_image_path)
        self.surface_hovered = pygame.image.load(state_hovered_image_path)
        self.surface_pressed = pygame.image.load(state_pressed_image_path)

        self.rect = self.surface_none.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]
        
        self.callback = callback

        self.state = Button.STATUS_NONE
        self.state_pressing = False
        
    def handle_event(self, event):
        
        # ignore some events
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        is_event_point_in_button_rect = self.rect.collidepoint(event.pos)

        if self.state == Button.STATUS_NONE:
            if is_event_point_in_button_rect:
                self.state = Button.STATUS_HOVERED
                
        elif self.state == Button.STATUS_PRESSED:
            if (event.type == MOUSEBUTTONUP) and is_event_point_in_button_rect:
                self.state = Button.STATUS_HOVERED
                
                self.callback()
                    
                return True

            if (event.type == MOUSEMOTION) and (not is_event_point_in_button_rect):
                self.state = Button.STATUS_NONE
            
        elif self.state == Button.STATUS_HOVERED:
            if (event.type == MOUSEBUTTONDOWN and is_event_point_in_button_rect):
                self.state = Button.STATUS_PRESSED

            if (event.type == MOUSEMOTION) and (not is_event_point_in_button_rect):
                self.state = Button.STATUS_NONE
                
    def draw(self):
        if self.state is Button.STATUS_PRESSED:
            self.window.blit(self.surface_pressed, self.loc)
        
        elif self.state is Button.STATUS_HOVERED:
            self.window.blit(self.surface_hovered, self.loc)
        else:
            self.window.blit(self.surface_none, self.loc)