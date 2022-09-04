from GameEngine import Engine
from rich import print

class Game(Engine):
    def before_loop(self):
        pass
    
    def after_loop(self):
        pass
    
    def event_loop(self):
        pass
    
    def during_loop(self):
        pass

if __name__ == "__main__":
    Game("Game Engine Test Program", (800, 600), 60)