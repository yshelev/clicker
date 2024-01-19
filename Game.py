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

        self.backgrounds = {
            "main": pygame.transform.scale(pygame.image.load("data/backgrounds/фон кликер затемненный.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
        }

        self.background = self.backgrounds["main"]

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
                    shape=(1, 2),
                    border=10,
                    texts=(
                        settings["sound"]["name"],
                        settings["music"]["name"]
                    ),
                    colour="WHITE",
                    onClicks=(self.switch, self.switch),
                    onClickParams=(["sound"], ["music"])
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
                    main_screen, 0, SCREEN_HEIGHT // 8 * 7 - SCREEN_HEIGHT // 16, SCREEN_WIDTH,
                                    SCREEN_HEIGHT // 8 + SCREEN_HEIGHT // 16,
                    shape=(3, 1),
                    border=20,
                    texts=("пассивные улучшения", "активные улучшения", "счет других участников"),
                    colour="WHITE",
                    onClicks=(self.passive_upgrades_loop, self.active_upgrades_loop, self.competitors_score),
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

        self.upgrades = {
            "passive":
                self.player.get_all_upgrades("passive"),
            "active":
                self.player.get_all_upgrades("active")
        }
        self.main_loop()

    def switch(self, to_switch):
        settings[to_switch]["turned"] = not settings[to_switch]["turned"]

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
        self.background = self.backgrounds["main"]

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

            self.draw_active_update_text(main_screen)
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
            self.draw_passive_updates_text(main_screen)
            self.update(main_screen, events)

    def competitors_score(self):
        self.switching_between_activities()
        running["competitors"] = True

        self.show_buttons_group(
            self.buttons["button_back"]
        )

        while running["competitors"]:
            clock.tick(FPS)
            events = pygame.event.get()
            main_screen.fill((255, 255, 255))

            for event in events:
                if event.type == pygame.QUIT:
                    running["competitors"] = False
                    myquit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running["competitors"] = False
                        myquit()

            self.update(main_screen, events)

    def update(self, surface: pygame.Surface, events) -> None:
        surface.blit(self.background, (0, 0))
        pygame_widgets.update(events)
        self.player.update()
        screen.blit(surface, (0, 0))
        pygame.display.update()

    def draw_score(self, surface):
        score_surface = self.get_font(30, "menu_font").render(
            f"Ваших голосов: {self.player.get_counter()}", False, "BLACK"
        )
        surface.blit(score_surface, (100, 400))

    def draw_passive_updates_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT // 6, SCREEN_HEIGHT // 5
        start_text_x, delta_text_x = SCREEN_WIDTH // 2, 0
        for index, upgrade in enumerate(self.upgrades["passive"]):
            passive_upgrade_surface = self.get_font(SCREEN_HEIGHT // 20, "menu_font").render(
                f"{int(self.upgrades["passive"][upgrade]["cost"] + sum(self.upgrades["passive"][upgrade]["levels"]) * self.upgrades["passive"][upgrade]["cost_multiplier"])}",
                False,
                "BLACK"
            )
            surface.blit(passive_upgrade_surface,
                         (start_text_x + delta_text_x * index, start_text_y + delta_text_y * index))

    def draw_active_update_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT // 5, SCREEN_HEIGHT // 4
        start_text_x, delta_text_x = SCREEN_WIDTH // 4, 0
        for index, upgrade in enumerate(self.upgrades["active"]):
            active_upgrade_surface = self.get_font(SCREEN_HEIGHT // 20, "menu_font").render(
                f"{int(self.upgrades["active"][upgrade]["cost"] * (not self.upgrades["active"][upgrade]["levels"]))}",
                False,
                "BLACK"
            )
            surface.blit(active_upgrade_surface,
                         (start_text_x + delta_text_x * index, start_text_y + delta_text_y * index))

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
