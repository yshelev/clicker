from Settings import *


class Button:
    def __init__(
            self,
            surface,
            x,
            y,
            height,
            width,
            inactive_image=None,
            hover_image=None,
            pressed_image=None,
            on_click=None,
            on_click_params=None,
            border=0,
            border_thickness=0,
            padding=0
    ):
        self.surface = surface

        self.clicked = False

        self.padding = padding

        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.rect = pygame.Rect(
            self.x + self.padding,
            self.y + self.padding,
            self.width - self.padding * 2,
            self.height - self.padding * 2
        )

        self.inactive_image, self.hover_image, self.pressed_image = map(
            lambda x: pygame.transform.scale(x, (width, height)), [
                inactive_image,
                hover_image,
                pressed_image
            ])
        self.image = self.inactive_image

        self.border = border
        self.border_thickness = border_thickness

        self.on_click_params = on_click_params
        self.on_click = on_click
        self.hidden = False

        self.sounds = {
            "click": pygame.mixer.Sound("data/sounds/clickb6.mp3")
        }

        self.set_sound()

    def handle_event(self, event):
        if not self.hidden:
            x, y = pygame.mouse.get_pos()
            if self.check_mouse_pos(x, y):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sounds["click"].play()

                    if self.on_click_params:
                        self.on_click(*self.on_click_params)

                    else:
                        self.on_click()
                    self.clicked = True
                    self.image = self.pressed_image
                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = False

        self.update_image()

    def update_image(self):
        x, y = pygame.mouse.get_pos()
        if self.check_mouse_pos(x, y):
            if self.clicked:
                self.image = self.pressed_image
            else:
                self.image = self.hover_image
        else:
            self.image = self.inactive_image

    def check_mouse_pos(self, x, y):
        return self.rect.collidepoint(x, y)

    def draw(self):
        if not self.hidden:
            self.surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw()

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    def set_sound(self):
        self.sounds["click"].set_volume(settings["sound"]["turned"])


class CircleButton(Button):
    def __init__(
            self,
            surface,
            center_x,
            center_y,
            height,
            width,
            radius,
            inactive_image=None,
            hover_image=None,
            pressed_image=None,
            on_click=None,
            on_click_params=None,
            border=0,
            border_thickness=0,
            padding=0
    ):
        super().__init__(
            surface,
            center_x - width // 2,
            center_y - height // 2,
            height,
            width,
            inactive_image,
            hover_image,
            pressed_image,
            on_click,
            on_click_params,
            border,
            border_thickness,
            padding
        )
        self.radius = radius
        self.center = self.center_x, self.center_y = center_x, center_y

    def check_mouse_pos(self, x, y):
        return (x - self.center_x) ** 2 + (y - self.center_y) ** 2 <= self.radius ** 2


class BuyButton(Button):
    def __init__(
            self,
            surface,
            x,
            y,
            height,
            width,
            levels,
            inactive_image=None,
            hover_image=None,
            pressed_image=None,
            purchased_inactive_image=None,
            purchased_hover_image=None,
            purchased_pressed_image=None,
            on_click=None,
            on_click_params=None,
            border=0,
            border_thickness=0,
            padding=0
    ):
        super().__init__(
            surface,
            x,
            y,
            height,
            width,
            inactive_image,
            hover_image,
            pressed_image,
            on_click,
            on_click_params,
            border,
            border_thickness,
            padding
        )
        self.levels = levels

        self.purchased_pressed_image, self.purchased_hover_image, self.purchased_inactive_image = map(
            lambda x: pygame.transform.scale(x, (self.width, self.height)), [
                purchased_pressed_image,
                purchased_hover_image,
                purchased_inactive_image
            ]
        )

    def handle_event(self, event):
        if not self.hidden:
            x, y = pygame.mouse.get_pos()
            if self.check_mouse_pos(x, y):

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sounds["click"].play()

                    if self.on_click_params:
                        if self.levels > 0:

                            if self.on_click(*self.on_click_params) == 0:
                                self.levels -= 1
                    self.clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.clicked = False

            self.update_image()

    def update_image(self):
        x, y = pygame.mouse.get_pos()
        if self.levels > 0:
            if self.check_mouse_pos(x, y):
                if self.clicked:
                    self.image = self.pressed_image
                else:
                    self.image = self.hover_image
            else:
                self.image = self.inactive_image
        else:
            if self.check_mouse_pos(x, y):
                if self.clicked:
                    self.image = self.purchased_pressed_image
                else:
                    self.image = self.purchased_hover_image
            else:
                self.image = self.purchased_inactive_image

