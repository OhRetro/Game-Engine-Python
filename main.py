from GameEngine import Engine
from pygame import mouse, locals, event, display

from rich import print
from time import time
from traceback import format_exc as tb_format_exc

START_TIME = time()

class Game(Engine):
    def on_game_startup(self):
        print(f"It took {round(time() - START_TIME, 2)} seconds to start.")
        
        #mouse.set_visible(False)
    
    def on_game_stop(self):
        print(f"It have been running for {round(time() - START_TIME, 2)} seconds.")
    
    def event_handler(self):
        for e in event.get():
            if e.type == locals.KEYDOWN and e.key == locals.K_ESCAPE or e.type != locals.KEYDOWN and e.type == locals.QUIT:
                self._quit()

    
    def during_loop(self):
        self.screen.fill((10, 10, 10))
        
        self.text("This is a Text", 10, 10)
        self.text_list([
            "This is a",
            "list of text"
            ], 10, 35)
        
if __name__ == "__main__":
    try:
        Game("Test Program", (800, 600), 60)
    except Exception:
        print(tb_format_exc())