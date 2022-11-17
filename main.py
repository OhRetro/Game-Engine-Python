from time import time
from traceback import format_exc as tb_format_exc

from GameEngine import Engine, text
from pygame import event, locals, mouse
from rich import print

START_TIME = time()

def timer():
    return round(time() - START_TIME, 2)

class Game(Engine):
    def on_startup(self):
        print(f"STARTUP TIME: {timer()} seconds.")
        #mouse.set_visible(False)
    
    def on_stop(self):
        print(f"RUNNING TIME: {timer()} seconds.")
    
    def game_setup(self):
        self.on_game["START"] = lambda:self.on_startup()
        self.on_game["STOP"] = lambda:self.on_stop()
    
    def event_handler(self):
        for e in event.get():
            if e.type == locals.KEYDOWN and e.key == locals.K_ESCAPE or e.type != locals.KEYDOWN and e.type == locals.QUIT:
                self.quit()

    def during_loop(self):
        self.window.fill((10, 10, 10))
        
        hello_text = text.text("Hello", 10, 10)
        self.show_object(hello_text)
        
        multi_texts = text.text_list([
            "AAA",
            "BBB",
            "CCC",
            ], 10, 25)
        for texts in multi_texts:
            self.show_object(texts)
        
if __name__ == "__main__":
    try:
        Game()
    except Exception:
        print(tb_format_exc())