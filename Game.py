import pygame.font

from Settings import *


class Game:
    def __init__(self):
        self.counter = 0
        self.button = Button(screen, 100, 100, 100, 100,
                             colour=(255, 255, 255),
                             textColour="BLUE",
                             borderThickness=10,
                             borderColour="GREEN",
                             pressedBorderColour="PURPLE",
                             pressedColour=(50, 50, 50),
                             text="big_bros\n",
                             onClick=self.on_click,
                             font=self.get_font(10)
                             )
        self.game_loop()

    def get_font(self, font_size: int) -> pygame.font.Font:
        """
        возвращает шрифт, от которого можно строить текст
        :param font_size:
        :return None:
        """

        return pygame.font.Font("data/menu_font.ttf", font_size)

    def on_click(self, *args: list) -> None:
        """
        функция on_click отвечает за работу кнопки
        :param args:
        :return:
        """

        self.counter += 1
        print(self.counter)

    def game_loop(self) -> None:
        """
        основный цикл игры.
        :return None:
        """

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
