import pygame
from pygame import event, display

from time import time as t_time

class Engine:
    def __init__(self, title:str="Window Title", resolution:tuple=(800, 600), fps_limit:int=60):  
        pygame.init()
        
        self.display = display
        self.window = self.display.set_mode(resolution)
        self.display.set_caption(title)
    
        self.CLOCK = pygame.time.Clock()
        self.FPS_LIMIT = fps_limit
        self.FPS_TARGET = 60
        
        self.RUNNING = True
        self.PREV_TIME = t_time()
        self.DELTATIME = 0
        
        self.on_game = {"START": None, "STOP": None}
        
        self.game_setup()
        self._game_loop()
        
    def _game_loop(self):
        self.on_game["START"]() if callable(self.on_game["START"]) else None
        
        while self.RUNNING:
            self.CLOCK.tick(self.FPS_LIMIT)
            self.DELTATIME = self._get_dt()
            self.event_handler()
            self.during_loop()
            self.display.flip()
        
        self.on_game["STOP"]() if callable(self.on_game["STOP"]) else None
        
        pygame.quit()
    
    def _get_dt(self):
        dt = (t_time() - self.PREV_TIME) * self.FPS_TARGET
        self.PREV_TIME = t_time()
        return dt
    
    def _pass(self):
        pass
    
    def quit(self):
        self.RUNNING = False
    
    def game_setup(self):
        pass
        
    def event_handler(self):
        for e in event.get():
            if e.type == pygame.QUIT:
                self._quit()
    
    def during_loop(self):
        pass
    
    def show_object(self, game_object):
        self.window.blit(game_object[0], game_object[1])    