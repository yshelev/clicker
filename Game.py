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

        self.competitors = {
            "moscow":
                Competitor(),
            "krasnoyarsk":
                Competitor(),
            "omsk":
                Competitor(),
            "murmansk":
                Competitor()
        }

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
                ),
            "competitors":
                pygame.transform.scale(
                    pygame.image.load("data/backgrounds/счет других игроков с текстом.png"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT)
                )
        }

        self.background = self.backgrounds["main"]
        self.images = {
            "button_main": {
                "inactive":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 1 (3).png"),
                "hover":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 2 (3).png"),
                "pressed":
                    pygame.image.load("data/images/ГОЛОСОВАНИЕ 3 (3).png")
            },
            "button_open_active_upgrades": {
                "inactive":
                    pygame.image.load("data/images/АКТИВНЫЕ 1.png"),
                "hover":
                    pygame.image.load("data/images/АКТИВНЫЕ 2.png"),
                "pressed":
                    pygame.image.load("data/images/АКТИВНЫЕ 3.png"),
            },
            "button_open_passive_upgrades": {
                "inactive":
                    pygame.image.load("data/images/ПАССИВНЫЕ 1.png"),
                "hover":
                    pygame.image.load("data/images/ПАССИВНЫЕ 2.png"),
                "pressed":
                    pygame.image.load("data/images/ПАССИВНЫЕ 3.png"),
            },
            "button_open_competitors_score": {
                "inactive":
                    pygame.image.load("data/images/СЧЕТ ДРУГИХ ИГРОКОВ 1.png"),
                "hover":
                    pygame.image.load("data/images/СЧЕТ ДРУГИХ ИГРОКОВ 2.png"),
                "pressed":
                    pygame.image.load("data/images/СЧЕТ ДРУГИХ ИГРОКОВ 3.png"),
            },
            "button_back": {
                "inactive":
                    pygame.image.load("data/images/НАЗАД 1 (2).png"),
                "hover":
                    pygame.image.load("data/images/НАЗАД 2 (2).png"),
                "pressed":
                    pygame.image.load("data/images/НАЗАД 3 (2).png"),
            },
            "button_buy": {
                "inactive":
                    pygame.image.load("data/images/КУПИТЬ 1.png"),
                "hover":
                    pygame.image.load("data/images/КУПИТЬ 2.png"),
                "pressed":
                    pygame.image.load("data/images/КУПИТЬ 3.png")
            },
            "button_purchased": {
                "inactive":
                    pygame.image.load("data/images/КУПЛЕНО 1.png"),
                "hover":
                    pygame.image.load("data/images/КУПЛЕНО 2.png"),
                "pressed":
                    pygame.image.load("data/images/КУПЛЕНО 3.png")
            },
            "sound": {
                "inactive":
                    pygame.image.load("data/images/ЗВУК 1.png"),
                "hover":
                    pygame.image.load("data/images/ЗВУК 2.png"),
                "pressed":
                    pygame.image.load("data/images/ЗВУК 3.png")
            },
            "digit": {
                str(i):
                    pygame.transform.scale(pygame.image.load("data/images/ЦИФРЫ.png"), (pygame.image.load("data"
                                                                                                          "/images/ЦИФРЫ.png").get_width(), 40)).subsurface(
                        (14 * (i + 1)) + (14 * i) + (40 * max(0, (i - 2))) + (18 if i > 1 else 0) + (
                            40 if i > 0 else 0),
                        0,
                        40 if i != 1 else 14,
                        40
                    ) for i in range(10)
            }
        }

        self.buttons = {
            "main":
                CircleButton(
                    surface=main_screen,
                    center_x=SCREEN_WIDTH / 2,
                    center_y=SCREEN_HEIGHT / 2,
                    width=SCREEN_WIDTH / 800 * 300,
                    height=SCREEN_HEIGHT / 800 * 300,
                    radius=SCREEN_HEIGHT / 8,
                    inactive_image=self.images["button_main"]["inactive"],
                    hover_image=self.images["button_main"]["hover"],
                    pressed_image=self.images["button_main"]["pressed"],
                    on_click=self.main_on_click,
                ),

            "open_active_upgrades":
                Button(
                    surface=main_screen,
                    x=0,
                    y=SCREEN_HEIGHT / 5 * 4,
                    width=SCREEN_WIDTH / 3,
                    height=SCREEN_HEIGHT / 5,
                    inactive_image=self.images["button_open_active_upgrades"]["inactive"],
                    hover_image=self.images["button_open_active_upgrades"]["hover"],
                    pressed_image=self.images["button_open_active_upgrades"]["pressed"],
                    on_click=self.active_upgrades_loop,
                    padding=20
                ),
            "open_passive_upgrades":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 3,
                    y=SCREEN_HEIGHT / 5 * 4,
                    width=SCREEN_WIDTH / 3,
                    height=SCREEN_HEIGHT / 5,
                    inactive_image=self.images["button_open_passive_upgrades"]["inactive"],
                    hover_image=self.images["button_open_passive_upgrades"]["hover"],
                    pressed_image=self.images["button_open_passive_upgrades"]["pressed"],
                    on_click=self.passive_upgrades_loop,
                    padding=20
                ),
            "open_competitors_score":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 3 * 2,
                    y=SCREEN_HEIGHT / 5 * 4,
                    width=SCREEN_WIDTH / 3,
                    height=SCREEN_HEIGHT / 5,
                    inactive_image=self.images["button_open_competitors_score"]["inactive"],
                    hover_image=self.images["button_open_competitors_score"]["hover"],
                    pressed_image=self.images["button_open_competitors_score"]["pressed"],
                    on_click=self.competitors_score,
                    padding=20,
                ),
            "back":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 10,
                    y=SCREEN_HEIGHT / 800 * 700,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    inactive_image=self.images["button_back"]["inactive"],
                    hover_image=self.images["button_back"]["hover"],
                    pressed_image=self.images["button_back"]["pressed"],
                    on_click=self.main_loop,
                    padding=20
                ),
            "passive_upgrade_1":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 25,
                    y=SCREEN_HEIGHT / 800 * 210,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=1_000_000,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["bot"],
                    padding=20
                ),
            "passive_upgrade_2":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 25,
                    y=SCREEN_HEIGHT / 800 * 325,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["AI"],
                    padding=20
                ),
            "passive_upgrade_3":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 25,
                    y=SCREEN_HEIGHT / 800 * 450,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["student"],
                    padding=20
                ),
            "passive_upgrade_4":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 25,
                    y=SCREEN_HEIGHT / 800 * 565,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=5,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_passive_upgrades,
                    on_click_params=["chinese"],
                    padding=20
                ),
            "active_upgrade_1":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 580,
                    y=SCREEN_HEIGHT / 800 * 220,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["double_click"],
                    padding=20
                ),
            "active_upgrade_2":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 580,
                    y=SCREEN_HEIGHT / 800 * 400,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["triple_click"],
                    padding=20
                ),
            "active_upgrade_3":
                BuyButton(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 800 * 580,
                    y=SCREEN_HEIGHT / 800 * 580,
                    width=SCREEN_WIDTH / 4,
                    height=SCREEN_HEIGHT / 10,
                    levels=1,
                    inactive_image=self.images["button_buy"]["inactive"],
                    hover_image=self.images["button_buy"]["hover"],
                    pressed_image=self.images["button_buy"]["pressed"],
                    purchased_inactive_image=self.images["button_purchased"]["inactive"],
                    purchased_hover_image=self.images["button_purchased"]["hover"],
                    purchased_pressed_image=self.images["button_purchased"]["pressed"],
                    on_click=self.player.buy_active_upgrade,
                    on_click_params=["quadro_click"],
                    padding=20
                ),
            "settings_sound":
                Button(
                    surface=main_screen,
                    x=SCREEN_WIDTH / 6 * 5,
                    y=0,
                    width=SCREEN_WIDTH / 6,
                    height=SCREEN_HEIGHT / 6,
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
            self.update(main_screen, events, [self.draw_passive_updates_text], [[main_screen]])

    def competitors_score(self):
        self.background = self.backgrounds["competitors"]

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

            self.update(main_screen, events, [self.draw_competitor_text, self.competitors_update],
                        [[main_screen], []])

    def draw_competitor_text(self, surface):
        start_x, delta_x = SCREEN_WIDTH / 800 * 325, 0
        start_y, delta_y = SCREEN_HEIGHT / 800 * 270, SCREEN_HEIGHT / 800 * 112

        for index, competitor in enumerate(self.competitors.values()):
            self.draw_number(
                surface,
                f"{competitor.get_score()}",
                start_x + delta_x * index,
                start_y + delta_y * index,
                self.get_font(SCREEN_HEIGHT // 20, "rd_font"),
                "WHITE",
                "BLACK"
            )

    def competitors_update(self):
        for competitor in self.competitors.values():
            competitor.update()

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
        self.draw_number(
            surface,
            f"{self.player.get_counter()}",
            SCREEN_WIDTH / 1.75,
            SCREEN_HEIGHT / 1.37123054904489,
            self.get_font(40, "button_font"),
            "WHITE",
            "BLACK"
        )

    def draw_passive_updates_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT / 800 * 225, SCREEN_HEIGHT / 800 * 120
        start_text_x, delta_text_x = SCREEN_WIDTH / 800 * 220, 0
        for index, upgrade in enumerate(self.upgrades["passive"]):
            self.draw_number(
                surface,
                f"{self.get_int_form(self.player.get_actual_cost_of_passive_upgrade(upgrade))}",
                start_text_x + delta_text_x * index,
                start_text_y + delta_text_y * index,
                self.get_font(55, "button_font"),
                "WHITE",
                "BLACK"
            )


    def draw_active_update_text(self, surface):
        start_text_y, delta_text_y = SCREEN_HEIGHT / 100 * 37, SCREEN_HEIGHT / 100 * 22
        start_text_x, delta_text_x = SCREEN_WIDTH / 800 * 620, 0
        for index, upgrade in enumerate(self.upgrades["active"]):
            self.draw_number(
                surface,
                f"{self.get_int_form(int(self.upgrades["active"][upgrade]["cost"] * (not self.upgrades["active"][upgrade]["levels"])))}",
                start_text_x + delta_text_x * index,
                start_text_y + delta_text_y * index,
                self.get_font(55, "button_font"),
                "WHITE",
                "BLACK",
            )

    def draw_number(self, surface, number, x, y, font, text_color, outline_color):
        number = str(number)
        to_output = ""
        dx = 0
        for index, char in enumerate(number):
            if char.isdigit():
                surface.blit(self.images["digit"][char], (x + dx, y))
                dx += 40 if char != "1" else 20
                to_output += "  " if char != "1" else " "
            else:
                dx += 40 if char != "." else 20
                to_output += char if char == "." else " " + char

        self.draw_text_with_outline(
            surface,
            x,
            y,
            font,
            to_output,
            text_color,
            outline_color
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
        return str(integer // (1000 ** check)) + ("." + str(integer % (1000 ** check))[0] if check and len(str(integer // (1000 ** check))) <= 1 else "") + cases[
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
