import pygame, sys, pygame_widgets
from pygame_widgets.button import Button, ButtonArray

pygame.font.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 800)
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # добавить pygame.RESIZABLE для динамического разрешения экрана.
                                                                # работает криво)

main_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()

running = {
    "main": False,
    "active_upgrades": False,
    "passive_upgrades": False,
    "settings": False
}

def myquit():
    pygame.quit()
    sys.exit()
