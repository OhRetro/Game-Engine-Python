import pygame
from time import time as t_time

class Engine:
    def __init__(self, title:str, resolution:tuple, fps_limit:int, during_loop=None, before_loop=None, after_loop=None, event_loop=None):
        self.DURING_LOOP = during_loop
        self.BEFORE_LOOP = before_loop
        self.AFTER_LOOP = after_loop
        self.EVENT_LOOP = event_loop
        
        if self.DURING_LOOP is None:
            self.DURING_LOOP = self._pass
        
        if before_loop is None:
            self.BEFORE_LOOP = self._pass
        
        if after_loop is None:
            self.AFTER_LOOP = self._pass    

        if event_loop is None:
            self.EVENT_LOOP = self._pass
            
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
        self.BEFORE_LOOP()
        while self.RUNNING:
            self.CLOCK.tick(self.FPS_LIMIT)
            self.DURING_LOOP()
            self.DELTA_TIME = self._get_dt()
            self._event_handler()
            self.EVENT_LOOP()
            pygame.display.flip()
        self.AFTER_LOOP()
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