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
                    "levels": [False for _ in range(5)]
                },
                "AI": {
                    "cost": 1_000,
                    "description": "работает быстрее кликера, еще и накрутку исключает. пAI мальчик",
                    "name": "искусственный интеллект",
                    "update_for_level": 5,
                    "levels": [False for _ in range(5)]
                },
                "IMKT": {
                    "cost": 1_000_000,
                    "description": "теперь студенты ИМКТ голосуют за вас! (не забудьте +10% к рейтингу)",
                    "name": "студенты ИМКТ",
                    "update_for_level": 100,
                    "levels": [False for _ in range(5)]
                },

                "chinese": {
                    "cost": 1_000_000_000,
                    "description": "азиат, что еще сказать",
                    "name": "азиат (бог)",
                    "update_for_level": 1_000,
                    "levels": [False for _ in range(5)]
                },
            },
            "active": {

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

