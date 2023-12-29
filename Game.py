from Settings import *


class Game:
    def __init__(self):
        self.game_loop()
        self.button = Button(screen, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, colour=(0, 0, 0), onClick=print("Clicked"))

    def game_loop(self):
        running = True
        while running:
            clock.tick(FPS)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        myquit()

            pygame_widgets.update(events)

            pygame.display.update()
