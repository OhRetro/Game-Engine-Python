from Engine.engine import Engine

def before():
    print("before")

if __name__ == "__main__":
    game = Engine(
        "Game Engine",
        (800, 600),
        60,
        before_loop=before
        )