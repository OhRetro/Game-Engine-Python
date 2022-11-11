from GameEngine import Engine, text
from pygame import mouse, locals, event

from rich import print
from time import time
from traceback import format_exc as tb_format_exc

START_TIME = time()

class Game(Engine):
    def on_game_startup(self):
        print(f"STARTUP TIME: {round(time() - START_TIME, 2)} seconds.")
        
        #mouse.set_visible(False)
    
    def on_game_stop(self):
        print(f"RUNNING TIME: {round(time() - START_TIME, 2)} seconds.")
    
    def event_handler(self):
        for e in event.get():
            if e.type == locals.KEYDOWN and e.key == locals.K_ESCAPE or e.type != locals.KEYDOWN and e.type == locals.QUIT:
                self.quit()

    def during_loop(self):
        self.window.fill((10, 10, 10))
        
        hello_text = text.text("Hello", 10, 10)
        self.display_object(hello_text)
        
        multi_texts = text.text_list([
            "AAA",
            "BBB",
            "CCC",
            ], 10, 25)
        for texts in multi_texts:
            self.display_object(texts)
        
if __name__ == "__main__":
    try:
        Game()
    except Exception:
        print(tb_format_exc())