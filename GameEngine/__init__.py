import pygame
from time import time as t_time

class Engine:
    def __init__(self, title:str, resolution:tuple, fps_limit:int):  
        pygame.init()
        
        self.SCREEN = pygame.display.get_surface()
        pygame.display.set_mode(resolution)
        pygame.display.set_caption(title)
        
        self.CLOCK = pygame.time.Clock()
        self.FPS_LIMIT = fps_limit
        self.FPS_TARGET = 60
        
        self.RUNNING = True
        self.PREV_TIME = t_time()
        self.DELTA_TIME = 0
        
        self._game_loop()
        
    def _game_loop(self):
        self.before_loop()
        while self.RUNNING:
            self.CLOCK.tick(self.FPS_LIMIT)
            self.during_loop()
            self.DELTA_TIME = self._get_dt()
            self._event_handler()
            self.event_loop()
            pygame.display.flip()
        self.after_loop()
        pygame.quit()
    
    def _pass(self):
        pass
    
    def _event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
    
    def _quit(self):
        self.RUNNING = False
        
    def _get_dt(self):
        dt = (t_time() - self.PREV_TIME) * self.FPS_TARGET
        self.PREV_TIME = t_time()
        return dt
    
    def before_loop(self):
        pass
    
    def after_loop(self):
        pass
    
    def event_loop(self):
        pass
    
    def during_loop(self):
        pass