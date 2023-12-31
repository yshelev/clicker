from Settings import *


class Player:
    def __init__(self):
        self.__counter = 0
        self.__add_money_per_click = 1
        self.__add_money_in_second = 0

        self.__upgrades = {
            "passive": {
                "bot": {
                    "cost": 50,
                    "description": "сам КЛИКАЕТ?!!??! ЧТО!?!?!?!?!",
                    "name": "автокликер",
                    "update_for_level": 1,
                    "levels": [False for _ in range(5)],
                    "cost_multiplier": 1.2
                },

                "AI": {
                    "cost": 1_000,
                    "description": "работает быстрее кликера, еще и накрутку исключает. пAI мальчик",
                    "name": "искусственный интеллект",
                    "update_for_level": 5,
                    "levels": [False for _ in range(5)],
                    "cost_multiplier": 1.2
                },

                "student": {
                    "cost": 1_000_000,
                    "description": "теперь студенты ИМКТ голосуют за вас! (не забудьте +10% к рейтингу)",
                    "name": "студенты ИМКТ",
                    "update_for_level": 100,
                    "levels": [False for _ in range(5)],
                    "cost_multiplier": 1.2
                },

                "chinese": {
                    "cost": 1_000_000_000,
                    "description": "азиат, что еще сказать",
                    "name": "азиат (бог)",
                    "update_for_level": 1_000,
                    "levels": [False for _ in range(5)],
                    "cost_multiplier": 1.2
                },
            },
            "active": {
                "double_click": {
                    "cost": 10,
                    "name": "двойной клик",
                    "description": "сломайте мышку... и получите даблКлик!",
                    "multiplier": 2,
                    "levels": False,
                },

                "triple_click": {
                    "cost": 10_000,
                    "name": "ТРОйной клик",
                    "description": "купите мышку с боковыми кнопками..",
                    "multiplier": 3,
                    "levels": False,
                },

                "quadro_click": {
                    "cost": 10_000_000,
                    "name": "ЧЕТВЕРНОЙ клик",
                    "description": "макросы.",
                    "multiplier": 4,
                    "levels": False,
                }
            }
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

    def get_upgrades(self, type_: str, ID: str, parameter: str) -> str | int | bool | list[bool] | float:
        return self.__upgrades[type_][ID][parameter]

    def buy_passive_upgrades(self, ID: str) -> int:
        # в Game можно обернуть эту функцию в другую, которая будет выводить текст в зависимости от exit_code
        """
        возвращает:
        0 - если покупка выполнена и деньги потрачены,
        1 - если денег не хватило,
        2 - если усилитель уже действует
        :param ID:
        :return:
        """
        exit_code = 2

        current_index = sum(self.__upgrades["passive"][ID]["levels"])
        if current_index != len(self.__upgrades["passive"][ID]["levels"]):
            if self.__counter >= self.__upgrades["passive"][ID]["cost"] * self.__upgrades["passive"][ID]["cost_multiplier"]:
                self.__counter -= self.__upgrades["passive"][ID]["cost"] * self.__upgrades["passive"][ID]["cost_multiplier"]
                self.__upgrades["passive"][ID]["levels"][current_index] = True
                self.__add_money_in_second += self.__upgrades["passive"][ID]["update_for_level"]
                exit_code = 0
            else:
                exit_code = 1

        return exit_code

    def buy_active_upgrade(self, ID: str) -> int:
        # в Game можно обернуть эту функцию в другую, которая будет выводить текст в зависимости от exit_code
        """
        возвращает:
        0 - если покупка выполнена и деньги потрачены,
        1 - если денег не хватило,
        2 - если усилитель уже действует
        :param ID:
        :return:
        """
        exit_code = 2
        if not self.__upgrades["active"][ID]["levels"]:
            if self.__counter >= self.__upgrades["active"][ID]["cost"]:
                self.__counter -= self.__upgrades["active"][ID]["cost"]
                self.__upgrades["active"][ID]["levels"] = True
                self.__add_money_per_click *= self.__upgrades["active"][ID]["multiplier"]
                exit_code = 0
            else:
                exit_code = 1

        return exit_code
