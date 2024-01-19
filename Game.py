import pygame.font

from Settings import *
from Player import Player


class Game:
    def __init__(self):
        self.counter = 0

        self.fonts = {
            "menu_font": "data/fonts/menu_font.ttf",
            "button_font": "data/fonts/SAIBA-45-Regular-(v1.1).otf",
            "rd_font": "data/fonts/PressStart2P-Regular.ttf"
        }

        self.player = Player()

        self.backgrounds = {
            "main": pygame.transform.scale(pygame.image.load("data/backgrounds/фон кликер с надписями 2.png"),
                                           (SCREEN_WIDTH, SCREEN_HEIGHT)),
        }

        self.images = {
            "button_main": {
                "inactive":
                    pygame.image.load("data/images/кнопка голосовать1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка голосовать2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка голосовать3.png")
            },
            "button_open_active_upgrades": {
                "inactive":
                    pygame.image.load("data/images/кнопка активные улучшения1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка активные улучшения2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка активные улучшения3.png"),
            },
            "button_open_passive_upgrades": {
                "inactive":
                    pygame.image.load("data/images/кнопка пассивные улучшения1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка пассивные улучшения2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка пассивные улучшения3.png"),
            },
            "button_open_competitors_score": {
                "inactive":
                    pygame.image.load("data/images/кнопка счет других участников1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка счет других участников2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка счет других участников3.png"),
            },
            "button_back": {
                "inactive":
                    pygame.image.load("data/images/кнопка назад1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка назад2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка назад3.png"),
            }
        }

        self.background = self.backgrounds["main"]

        self.buttons = {
            "main":
                CircleButton(
                    surface=main_screen,
                    center_x=SCREEN_WIDTH // 2,
                    center_y=SCREEN_HEIGHT // 2,
                    width=SCREEN_WIDTH // 3,
                    height=SCREEN_HEIGHT // 3,
                    radius=SCREEN_HEIGHT // 8,
                    inactive_image=self.images["button_main"]["inactive"],
                    hover_image=self.images["button_main"]["hover"],
                    pressed_image=self.images["button_main"]["pressed"],
                    on_click=self.main_on_click,
                ),
            "open_active_upgrades":
                Button(
                    surface=main_screen,
                    x=0,
                    y=SCREEN_HEIGHT // 5 * 4,
                    width=SCREEN_WIDTH // 3,
                    height=SCREEN_HEIGHT // 5,
                    inactive_image=self.images["button_open_active_upgrades"]["inactive"],
                    hover_image=self.images["button_open_active_upgrades"]["hover"],
                    pressed_image=self.images["button_open_active_upgrades"]["pressed"],
                    on_click=self.active_upgrades_loop,
                    padding=10
                ),
            "open_passive_upgrades":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 3,
                    y=SCREEN_HEIGHT // 5 * 4,
                    width=SCREEN_WIDTH // 3,
                    height=SCREEN_HEIGHT // 5,
                    inactive_image=self.images["button_open_passive_upgrades"]["inactive"],
                    hover_image=self.images["button_open_passive_upgrades"]["hover"],
                    pressed_image=self.images["button_open_passive_upgrades"]["pressed"],
                    on_click=self.passive_upgrades_loop,
                    padding=10
                ),
            "open_competitors_score":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 3 * 2,
                    y=SCREEN_HEIGHT // 5 * 4,
                    width=SCREEN_WIDTH // 3,
                    height=SCREEN_HEIGHT // 5,
                    inactive_image=self.images["button_open_competitors_score"]["inactive"],
                    hover_image=self.images["button_open_competitors_score"]["hover"],
                    pressed_image=self.images["button_open_competitors_score"]["pressed"],
                    on_click=self.competitors_score,
                    padding=10,
                ),
            "back":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 2,
                    y=SCREEN_HEIGHT // 20 * 19,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 20,
                    inactive_image=self.images["button_back"]["inactive"],
                    hover_image=self.images["button_back"]["hover"],
                    pressed_image=self.images["button_back"]["pressed"],
                    on_click=self.main_loop,
                    padding=10
                )
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
            self.buttons["main"],
            self.buttons["open_active_upgrades"],
            self.buttons["open_passive_upgrades"],
            self.buttons["open_competitors_score"]
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

            self.update(main_screen, events, [self.draw_score], [[main_screen]])

    def active_upgrades_loop(self):
        self.switching_between_activities()
        running["active_upgrades"] = True

        self.show_buttons_group(
            self.buttons["back"],
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
            self.update(main_screen, events, [self.draw_active_update_text], [[main_screen]])

    def settings_loop(self):

        self.switching_between_activities()
        running["settings"] = True

        self.show_buttons_group(
            self.buttons["back"],
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

            self.update(main_screen, events, [], [])

    def passive_upgrades_loop(self):
        self.switching_between_activities()
        running["passive_upgrades"] = True

        self.show_buttons_group(
            self.buttons["back"],
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
            self.update(main_screen, events, [self.draw_passive_updates_text], [[main_screen]])

    def competitors_score(self):
        self.switching_between_activities()
        running["competitors"] = True

        self.show_buttons_group(
            self.buttons["back"]
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

            self.update(main_screen, events, [], [])

    def update(self, surface: pygame.Surface, events, funcs, funcs_params) -> None:
        surface.blit(self.background, (0, 0))
        for param_index, func in enumerate(funcs):
            func(*funcs_params[param_index])
        self.update_buttons(events)
        self.player.update()
        screen.blit(surface, (0, 0))
        pygame.display.update()

    def update_buttons(self, events):
        for buttons in self.buttons.keys():
            for event in events:
                self.buttons[buttons].handle_event(event=event)
                print(self.player.get_counter())
            self.buttons[buttons].draw()

    def draw_score(self, surface):
        score_surface = self.get_font(40, "rd_font").render(
            f"{self.player.get_counter()}", False, "WHITE"
        )
        surface.blit(score_surface, (SCREEN_WIDTH // 1.75, SCREEN_HEIGHT // 1.37123054904489))

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

    @staticmethod
    def switching_between_activities():
        for i in running.keys():
            running[i] = False
