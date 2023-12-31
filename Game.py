import pygame.font

from Settings import *
from Player import Player


class Game:
    def __init__(self):
        self.counter = 0

        self.fonts = {
            "menu_font": "data/fonts/menu_font.ttf"
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
                    radius=SCREEN_WIDTH // 8,
                    onClick=self.main_on_click,
                ),
            "button_settings":
                ButtonArray(
                    main_screen, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 * 3,
                    shape=(1, 4),
                    border=10,
                    texts=("настройка а", "настройка б", "настройка с", "настройка д"),
                    colour="WHITE",
                    onClicks=(print, print, print, print),
                    onClickParams=(["a"], ["b"], ["c"], ["d"])
                ),
            "button_active_upgrades":
                ButtonArray(
                    main_screen, SCREEN_WIDTH // 5 * 3, SCREEN_HEIGHT // 16, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 * 3,
                    shape=(1, 3),
                    border=10,
                    texts=(
                        self.player.get_upgrades("active", "double_click", "name"),
                        self.player.get_upgrades("active", "triple_click", "name"),
                        self.player.get_upgrades("active", "quadro_click", "name")
                    ),
                    colour="WHITE",
                    onClicks=(
                        self.player.buy_active_upgrade,
                        self.player.buy_active_upgrade,
                        self.player.buy_active_upgrade,
                    ),
                    onClickParams=(["double_click"], ["triple_click"], ["quadro_click"])
                ),
            "button_passive_upgrades":
                ButtonArray(
                    main_screen, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8, SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4 * 3,
                    shape=(1, 4),
                    border=10,
                    texts=(
                        self.player.get_upgrades("passive", "bot", "name"),
                        self.player.get_upgrades("passive", "AI", "name"),
                        self.player.get_upgrades("passive", "student", "name"),
                        self.player.get_upgrades("passive", "chinese", "name"),
                    ),
                    colour="WHITE",
                    onClicks=(
                        self.player.buy_passive_upgrades,
                        self.player.buy_passive_upgrades,
                        self.player.buy_passive_upgrades,
                        self.player.buy_passive_upgrades
                    ),
                    onClickParams=(["bot"], ["AI"], ["student"], ["chinese"])
                ),
            "button_open_updates_main":
                ButtonArray(
                    main_screen, 0, SCREEN_HEIGHT // 8 * 7 - SCREEN_HEIGHT // 16, SCREEN_WIDTH, SCREEN_HEIGHT // 8 + SCREEN_HEIGHT // 16,
                    shape=(2, 1),
                    border=20,
                    texts=("пассивные улучшения", "активные улучшения"),
                    colour="WHITE",
                    onClicks=(self.passive_upgrades_loop, self.active_upgrades_loop),
                ),
            "button_settings_main":
                Button(
                    main_screen, SCREEN_WIDTH // 8 * 7, 0, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8,
                    colour="WHITE",
                    borderThickness=3,
                    borderColour="BLACK",
                    text="importImageSettings",
                    onClick=self.settings_loop,

                ),
            "button_back":
                Button(
                    main_screen, SCREEN_WIDTH // 8 * 3, SCREEN_HEIGHT // 8 * 7, SCREEN_WIDTH // 8, SCREEN_HEIGHT // 8,
                    colour="GREEN",
                    textColour="BLUE",
                    borderThickness=10,
                    borderColour="GREEN",
                    pressedBorderColour="PURPLE",
                    pressedColour=(50, 50, 50),
                    text="голосуй за молодежную столицу!",
                    textHAlign="left",  # выравнивание по ширине
                    textVAlign="mid",  # выравнивание по высоте
                    onClick=self.main_loop
                ),

        }
        self.main_loop()

    def start_main_loop(self):
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

        self.show_buttons_group(
            self.buttons["main_button"],
            self.buttons["button_open_updates_main"],
            self.buttons["button_settings_main"]
        )

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

            self.draw_score(main_screen)
            self.update(main_screen, events)

    def active_upgrades_loop(self):
        self.switching_between_activities()
        running["active_upgrades"] = True

        self.show_buttons_group(
            self.buttons["button_back"],
            self.buttons["button_active_upgrades"]
        )

        while running["active_upgrades"]:
            clock.tick(FPS)
            events = pygame.event.get()
            main_screen.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["active_upgrades"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["active_upgrades"] = False
                        myquit()

            self.update(main_screen, events)

    def settings_loop(self):

        self.switching_between_activities()
        running["settings"] = True

        self.show_buttons_group(
            self.buttons["button_back"],
            self.buttons["button_settings"]
        )

        while running["settings"]:
            clock.tick(FPS)
            events = pygame.event.get()
            main_screen.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["settings"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["settings"] = False
                        myquit()

            self.update(main_screen, events)

    def passive_upgrades_loop(self):
        self.switching_between_activities()
        running["passive_upgrades"] = True

        self.show_buttons_group(
            self.buttons["button_back"],
            self.buttons["button_passive_upgrades"]
        )

        while running["passive_upgrades"]:
            clock.tick(FPS)
            events = pygame.event.get()
            main_screen.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["passive_upgrades"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["passive_upgrades"] = False
                        myquit()

            self.update(main_screen, events)

    def update(self, surface: pygame.Surface, events) -> None:
        pygame_widgets.update(events)
        self.player.update()
        screen.blit(surface, (0, 0))
        pygame.display.update()

    def draw_score(self, surface):
        score_surface = self.get_font(30, "menu_font").render(
            f"Ваших голосов: {self.player.get_counter()}", False, "BLACK")
        surface.blit(score_surface, (100, 400))

    def show_buttons_group(self, *buttons):
        for button in self.buttons:
            self.buttons[button].hide()

        for button in buttons:
            button.show()
            button.enable()

    @staticmethod
    def switching_between_activities():
        for i in running.keys():
            running[i] = False