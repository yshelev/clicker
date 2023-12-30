import pygame.font

from Settings import *
from Player import Player


class Game:
    def __init__(self):
        self.counter = 0

        self.fonts = {
            "menu_font": "data/menu_font.ttf"
        }

        self.player = Player()

        self.buttons = {
            "main_button":
                Button(
                    main_screen, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4,
                    colour="GREEN",
                    textColour="BLUE",
                    borderThickness=10,
                    borderColour="GREEN",
                    pressedBorderColour="PURPLE",
                    pressedColour=(50, 50, 50),
                    text="голосуй за молодежную столицу!",
                    textHAlign="left",  # выравнивание по ширине
                    textVAlign="mid",  # выравнивание по высоте
                    onClick=self.main_on_click,
                    font=self.get_font(8, "menu_font")
                ),
            "button_open_updates_main":
                ButtonArray(
                    main_screen, 0, SCREEN_HEIGHT // 8 * 7 - 50, SCREEN_WIDTH, SCREEN_HEIGHT // 8 + 50,
                    shape=(2, 1),
                    border=20,
                    texts=("пассивные улучшения", "активные улучшения"),
                    colour="WHITE",
                    onClicks=(self.passive_upgrades_loop, self.active_upgrades_loop),
                ),
            "button_settings":
                Button(
                    main_screen, SCREEN_WIDTH // 8 * 7, 0, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8,
                    colour="WHITE",
                    borderThickness=3,
                    borderColour="BLACK",
                    text="importImageSettings",
                    onClick=self.settings_loop,

                ),
            "buttons_back": {
                "passive_upgrades":
                    Button(
                        screen_active_upgrades_loop, SCREEN_WIDTH // 8 * 3, SCREEN_HEIGHT - 100, 100, 100,
                        colour="WHITE",
                        borderThickness=3,
                        borderColour="BLACK",
                        text="BACK",
                        onClick=self.main_loop,
                    ),
                "active_upgrades":
                    Button(
                        screen_passive_upgrades_loop, SCREEN_WIDTH // 8 * 3, SCREEN_HEIGHT - 100, 100, 100,
                        colour="WHITE",
                        borderThickness=3,
                        borderColour="BLACK",
                        text="BACK",
                        onClick=self.main_loop
                    ),
                "settings":
                    Button(
                        screen_settings, SCREEN_WIDTH // 8 * 3, SCREEN_HEIGHT - 100, 100, 100,
                        colour="WHITE",
                        borderThickness=3,
                        borderColour="BLACK",
                        text="BACK",
                        onClick=self.main_loop
                    )
            }

        }
        self.main_loop()

    def get_font(self, font_size: int, name: str) -> pygame.font.Font:
        """
        возвращает шрифт, от которого можно строить текст
        :param name:
        :param font_size:
        :return pygame.font.Font:
        """

        return pygame.font.Font(self.fonts[name], font_size)

    def main_on_click(self) -> None:
        """
        функция on_click отвечает за работу кнопки
        :return:
        """
        self.player.handle_click()

    def main_loop(self) -> None:
        """
        основный цикл игры.
        :return None:
        """
        self.switching_between_activities()
        running["main"] = True

        while running["main"]:
            clock.tick(FPS)
            events = pygame.event.get()
            main_screen.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["main"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["main"] = False
                        myquit()

            self.update(main_screen, events)

    def active_upgrades_loop(self):

        self.switching_between_activities()
        running["active_upgrades"] = True

        while running["active_upgrades"]:
            clock.tick(FPS)
            events = pygame.event.get()
            screen_active_upgrades_loop.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["active_upgrades"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["active_upgrades"] = False
                        myquit()

            self.update(screen_active_upgrades_loop, events)

    def settings_loop(self):

        self.switching_between_activities()
        running["settings"] = True

        while running["settings"]:
            clock.tick(FPS)
            events = pygame.event.get()
            screen_settings.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["settings"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["settings"] = False
                        myquit()

            self.update(screen_settings, events)

    def passive_upgrades_loop(self):

        self.switching_between_activities()
        running["passive_upgrades"] = True

        while running["passive_upgrades"]:
            clock.tick(FPS)
            events = pygame.event.get()
            screen_passive_upgrades_loop.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["passive_upgrades"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["passive_upgrades"] = False
                        myquit()

            self.update(screen_passive_upgrades_loop, events)

    def switching_between_activities(self):
        for i in running.keys():
            running[i] = False

    def update(self, surface: pygame.Surface, events) -> None:

        pygame_widgets.update(events)
        self.player.update()
        screen.blit(surface, (0, 0))
        pygame.display.update()
