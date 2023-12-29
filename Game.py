import pygame.font

from Settings import *


class Game:
    def __init__(self):
        self.counter = 0

        self.fonts = {
            "menu_font": "data/menu_font.ttf"
        }

        self.buttons = {
            "main_button": Button(screen, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8, SCREEN_WIDTH, 800,
                                  colour=(255, 255, 255),
                                  textColour="BLUE",
                                  borderThickness=10,
                                  borderColour="GREEN",
                                  pressedBorderColour="PURPLE",
                                  pressedColour=(50, 50, 50),
                                  text="ниггеры меня заждались на вписке",
                                  onClick=self.on_click,
                                  font=self.get_font(20, "menu_font")
                                  )

        }
        self.game_loop()

    def get_font(self, font_size: int, name: str) -> pygame.font.Font:
        """
        возвращает шрифт, от которого можно строить текст
        :param name:
        :param font_size:
        :return pygame.font.Font:
        """

        return pygame.font.Font(self.fonts[name], font_size)

    def on_click(self, *args: list) -> None:
        """
        функция on_click отвечает за работу кнопки
        :param args:
        :return:
        """

        self.counter += 1

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
