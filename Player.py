from Settings import *


class Player:
    def __init__(self):
        self.__counter = 0
        self.__add_money_per_click = 1
        self.__add_money_in_second = 0

        self.__available_updates = {
            "Бот": [1, 2, 3, 4, 5],
            "Искуственный Интеллект": [1, 2, 3, 4, 5]
        }

    def update(self) -> None:
        """
        добавляет очки игроку за одну секунду
        :return:
        """
        self.__counter += (self.__add_money_in_second / FPS)

    def handle_click(self) -> None:
        """
        добавляет очки игроку за клик
        :return:
        """
        self.__counter += self.__add_money_per_click

    def get_counter(self) -> int:
        """
        возвращает текущие очки игрока
        :return:
        """
        return int(self.__counter)

