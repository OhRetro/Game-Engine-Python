import pygame
from pygame import event, display

from time import time as t_time

class Engine:
    def __init__(self, title:str="Window Title", resolution:tuple=(800, 600), fps_limit:int=60):  
        pygame.init()
        
        self.window = display.set_mode(resolution)
        display.set_caption(title)
    
        self.CLOCK = pygame.time.Clock()
        self.FPS_LIMIT = fps_limit
        self.FPS_TARGET = 60
        
        self.RUNNING = True
        self.PREV_TIME = t_time()
        self.DELTATIME = 0
        
        self._game_loop()
        
    def _game_loop(self):
        self.on_game_startup()
        
        while self.RUNNING:
            self.CLOCK.tick(self.FPS_LIMIT)
            self.DELTATIME = self._get_dt()
            self.event_handler()
            self.during_loop()
            display.flip()
        
        self.on_game_stop()
        
        pygame.quit()
    
    def _get_dt(self):
        dt = (t_time() - self.PREV_TIME) * self.FPS_TARGET
        self.PREV_TIME = t_time()
        return dt
    
    def quit(self):
        self.RUNNING = False
        
    def on_game_startup(self):
        pass
    
    def on_game_stop(self):
        pass
    
    def event_handler(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                self._quit()
    
    def during_loop(self):
        pass
    
    def display_object(self, game_object):
        self.window.blit(game_object[0], game_object[1])
        