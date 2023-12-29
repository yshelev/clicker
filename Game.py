from Settings import *

class Game:
    def __init__(self):
        self.game_loop()

    def game_loop(self):
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    myquit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.key == pygame.K_ESCAPE:
                        myquit()
            pygame.display.flip()
