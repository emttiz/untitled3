class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage
    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        