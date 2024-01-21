import pygame.font

from Button import *
from Player import Player
from Competitor import Competitor


class Game:
    def __init__(self):
        self.counter = 0

        self.fonts = {
            "menu_font": "data/fonts/menu_font.ttf",
            "button_font": "data/fonts/SAIBA-45-Regular-(v1.1).otf",
            "rd_font": "data/fonts/PressStart2P-Regular.ttf"
        }

        self.player = Player()

        self.competitor = Competitor()

        self.sounds = {
            "background_music":
                pygame.mixer.Sound("data/sounds/background_music.mp3")
        }

        self.set_sound()

        self.sounds["background_music"].play(-1)

        self.backgrounds = {
            "main":
                pygame.transform.scale(
                    pygame.image.load("data/backgrounds/фон кликер с надписями 2.png"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
            "other":
                pygame.transform.scale(
                    pygame.image.load("data/backgrounds/фон кликер затемненный.png"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
            "active_upgrades":
                pygame.transform.scale(
                    pygame.image.load("data/backgrounds/фон активные улучшения.png"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                ),
            "passive_upgrades":
                pygame.transform.scale(
                    pygame.image.load("data/backgrounds/фон пассивные улучшения.png"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                )
        }

        self.images = {
            "button_main": {
                "inactive":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 1.png"),
                "hover":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 2.png"),
                "pressed":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 3.png")
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
            },
            "button_buy": {
                "inactive":
                    pygame.image.load("data/images/кнопка купить1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка купить2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка купить3.png")
            },
            "button_purchased": {
                "inactive":
                    pygame.image.load("data/images/кнопка куплено1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка куплено2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка куплено3.png")
            },
            "sound": {
                "inactive":
                    pygame.image.load("data/images/кнопка звук1.png"),
                "hover":
                    pygame.image.load("data/images/кнопка звук2.png"),
                "pressed":
                    pygame.image.load("data/images/кнопка звук3.png")
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
                    x=0,
                    y=SCREEN_HEIGHT // 10 * 9,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    inactive_image=self.images["button_back"]["inactive"],
                    hover_image=self.images["button_back"]["hover"],
                    pressed_image=self.images["button_back"]["pressed"],
                    on_click=self.main_loop,
                    padding=10
                ),
            "passive_upgrade_1":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 25,
                    y=SCREEN_HEIGHT // 800 * 210,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=1_000_000,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["bot"],
                    padding=10
                ),
            "passive_upgrade_2":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 25,
                    y=SCREEN_HEIGHT // 800 * 325,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["AI"],
                    padding=10
                ),
            "passive_upgrade_3":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 25,
                    y=SCREEN_HEIGHT // 800 * 450,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["student"],
                    padding=10
                ),
            "passive_upgrade_4":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 25,
                    y=SCREEN_HEIGHT // 800 * 565,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["chinese"],
                    padding=10
                ),
            "active_upgrade_1":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 580,
                    y=SCREEN_HEIGHT // 800 * 220,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["double_click"],
                    padding=10
                ),
            "active_upgrade_2":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 580,
                    y=SCREEN_HEIGHT // 800 * 400,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["triple_click"],
                    padding=10
                ),
            "active_upgrade_3":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 800 * 580,
                    y=SCREEN_HEIGHT // 800 * 580,
                    width=SCREEN_WIDTH // 4,
                    height=SCREEN_HEIGHT // 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["quadro_click"],
                    padding=10
                ),
            "settings_sound":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH // 6 * 5,
                    y=0,
                    width=SCREEN_WIDTH // 6,
                    height=SCREEN_HEIGHT // 6,
                    inactive_image=self.images["sound"]["inactive"],
                    hover_image=self.images["sound"]["hover"],
                    pressed_image=self.images["sound"]["pressed"],
                    on_click=self.switch,
                    on_click_params=["sound"]
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
        for button in self.buttons:
            self.buttons[button].set_sound()
        self.set_sound()

    def set_sound(self):
        for sound in self.sounds.values():
            sound.set_volume(settings["sound"]["turned"] * settings["sound"]["sound"])

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
            self.buttons["open_competitors_score"],
            self.buttons["settings_sound"]
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

            self.update(main_screen, events, [self.draw_score, self.competitors_update], [[main_screen], []])

    def active_upgrades_loop(self):
        self.background = self.backgrounds["active_upgrades"]

        self.switching_between_activities()
        running["active_upgrades"] = True

        self.show_buttons_group(
            self.buttons["back"],
            self.buttons["active_upgrade_1"],
            self.buttons["active_upgrade_2"],
            self.buttons["active_upgrade_3"],
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
        self.background = self.backgrounds["other"]

        self.switching_between_activities()
        running["settings"] = True

        self.show_buttons_group(
            self.buttons["back"]
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
        self.background = self.backgrounds["passive_upgrades"]

        self.switching_between_activities()
        running["passive_upgrades"] = True

        self.show_buttons_group(
            self.buttons["back"],
            self.buttons["passive_upgrade_1"],
            self.buttons["passive_upgrade_2"],
            self.buttons["passive_upgrade_3"],
            self.buttons["passive_upgrade_4"],
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
        self.background = self.backgrounds["other"]

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

            self.update(main_screen, events, [self.draw_competitor_text, self.competitors_update], [[main_screen], []])

    def draw_competitor_text(self, surface):
        self.draw_text_with_outline(
            surface,
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT // 2,
            self.get_font(SCREEN_HEIGHT // 20, "rd_font"),
            f"{self.competitor.get_score()}",
            "WHITE",
            "BLACK"
        )

    def competitors_update(self):
        self.competitor.update()

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
            self.buttons[buttons].draw()

    def draw_score(self, surface):
        score_surface = self.get_font(40, "rd_font").render(
            f"{self.player.get_counter()}", False, "WHITE"
        )
        surface.blit(score_surface, (SCREEN_WIDTH // 1.75, SCREEN_HEIGHT // 1.37123054904489))

    def draw_passive_updates_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT // 800 * 232, SCREEN_HEIGHT // 800 * 120
        start_text_x, delta_text_x = SCREEN_WIDTH // 800 * 250, 0
        for index, upgrade in enumerate(self.upgrades["passive"]):
            self.draw_text_with_outline(
                surface,
                start_text_x + delta_text_x * index,
                start_text_y + delta_text_y * index,
                self.get_font(SCREEN_HEIGHT // 20, "button_font"),
                f"{self.get_int_form(self.player.get_actual_cost_of_passive_upgrade(upgrade))}",
                "WHITE",
                "BLACK"
            )
            passive_upgrade_surface = self.get_font(SCREEN_HEIGHT // 20, "button_font").render(
                f"{self.get_int_form(self.player.get_actual_cost_of_passive_upgrade(upgrade))}",
                False,
                "WHITE"
            )
            surface.blit(passive_upgrade_surface,
                         (start_text_x + delta_text_x * index, start_text_y + delta_text_y * index))

    def draw_active_update_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT // 100 * 38, SCREEN_HEIGHT // 100 * 23
        start_text_x, delta_text_x = SCREEN_WIDTH // 800 * 620, 0
        for index, upgrade in enumerate(self.upgrades["active"]):
            self.draw_text_with_outline(
                surface,
                start_text_x + delta_text_x * index,
                start_text_y + delta_text_y * index,
                self.get_font(SCREEN_HEIGHT // 20, "button_font"),
                f"{self.get_int_form(int(self.upgrades["active"][upgrade]["cost"] * (not self.upgrades["active"][upgrade]["levels"])))}",
                "WHITE",
                "BLACK"
            )

    def show_buttons_group(self, *buttons):
        for button in self.buttons:
            self.buttons[button].hide()

        for button in buttons:
            button.show()

    @staticmethod
    def switching_between_activities():
        for i in running.keys():
            running[i] = False

    @staticmethod
    def get_int_form(integer):
        integer_str = str(integer)
        cases = {
            0: "",
            1: "k",
            2: "m",
            3: "b"
        }
        check = sum([len(integer_str) > 3, len(integer_str) > 6, len(integer_str) > 9])
        return str(integer // (1000 ** check)) + ("." + str(integer % (1000 ** check) // 10) if check else "") + cases[
            check]

    @staticmethod
    def draw_text_with_outline(surface, x, y, font, text, text_color, outline_color):
        outline = font.render(text, False, outline_color)
        main_text = font.render(text, False, text_color)

        for dx in range(-1, 1):
            for dy in range(-1, 1):
                if dx and dy:
                    surface.blit(outline, (x + dx, y + dy))

        surface.blit(main_text, (x, y))
