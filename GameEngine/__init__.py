import pygame
from pygame import Surface
from pygame import locals, event, display, font

from time import time as t_time

class Engine:
    def __init__(self, title:str, resolution:tuple, fps_limit:int):  
        pygame.init()
        
        self.screen = display.set_mode(resolution)
        display.set_caption(title)
    
        self.clock = pygame.time.Clock()
        self.fps_limit = fps_limit
        self.fps_target = 60
        
        self.running = True
        self.prev_time = t_time()
        self.delta_time = 0
        
        self._game_loop()
        
    def _game_loop(self):
        self.on_game_startup()
        while self.running:
            self.clock.tick(self.fps_limit)
            self.delta_time = self._get_dt()
            self.event_handler()
            self.during_loop()
            display.flip()
        self.on_game_stop()
        pygame.quit()
    
    def _pass(self):
        pass
    
    def _quit(self):
        self.running = False
        
    def _get_dt(self):
        dt = (t_time() - self.prev_time) * self.fps_target
        self.prev_time = t_time()
        return dt
    
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
    
       #Text Display Function
    def text(self, text, x, y, size=20, color=(255,255,255), center=False):
        text_font = font.Font(None, size)
        text = text_font.render(text, 1, color)
        textrect = text.get_rect()
        textpos = (x,y)
        if center:
            textrect.center = textpos
            self.screen.blit(text, textrect)    
        else:
            textrect.topleft = textpos
            self.screen.blit(text, textpos)
    
    #Text List Function
    def text_list(self, text_list, x, y=0, size=20, color=(255,255,255), center=False):
        for text in text_list:
            self.text(text, x, y+(round((5*(size/5))*(text_list.index(text)))), size, color, center)
   