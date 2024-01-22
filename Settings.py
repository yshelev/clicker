import pygame, sys

pygame.font.init()
pygame.mixer.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (1200, 1000)
FPS = 60

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))  # добавить pygame.RESIZABLE для динамического разрешения экрана.
                                    # работает криво)

main_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

running = {
    "main": False,
    "active_upgrades": False,
    "passive_upgrades": False,
    "settings": False,
    "competitors": False
}

settings = {
    "sound": {
        "name": "звук",
        "turned": True,
        "sound": 0.2
    },
    "music": {
        "name": "музыка",
        "turned": False
    },
}


def myquit():
    pygame.quit()
    sys.exit()
