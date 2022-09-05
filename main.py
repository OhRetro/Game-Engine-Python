from GameEngine import Engine, mouse

import pygame
import pygame.locals as pl

from rich import print
from time import time
from traceback import format_exc as tb_format_exc

START_TIME = time()

class Game(Engine):
    def before_loop(self):
        print(f"It took {round(time() - START_TIME, 2)} seconds to start.")
        
        #mouse.set_visible(False)
    
    def after_loop(self):
        print(f"It have been running for {round(time() - START_TIME, 2)} seconds.")
    
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pl.KEYDOWN and event.key == pl.K_ESCAPE or event.type != pl.KEYDOWN and event.type == pl.QUIT:
                self._quit()

    
    def during_loop(self):
        self.SCREEN.fill((123, 123, 123))
        
if __name__ == "__main__":
    try:
        Game("Test Program", (800, 600), 60)
    except Exception:
        print(tb_format_exc())