import pygame

def position():
    return pygame.mouse.get_pos()

def set_visible(visible:bool):
    pygame.mouse.set_visible(visible)