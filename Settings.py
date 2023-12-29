import pygame, sys, pygame_widgets
from pygame_widgets.button import Button

pygame.font.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()


def myquit():
    pygame.quit()
    sys.exit()
