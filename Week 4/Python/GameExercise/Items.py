from Master_Class import *


class Weapons(Items):

    def __init__(self, cost: int, category: str, name: str):
        super().__init__(cost,category)
        self.category = 'Weapons'
        self.name = name


class Consumables(Items):

    def __init__(self, cost: int, category: str, name: str, health: int):
        super().__init__(cost,category)
        self.category = 'Consumables'
        self.name = name
        self.health = health
        self.get_name()

    def get_name(self):
        return self.name


class Miscellaneous(Items):

    def __init__(self, cost: int, category: str, name: str):
        super().__init__(cost, category)
        self.category = 'Miscellaneous'
        self.name = name
        self.get_name()

    def get_name(self):
        return self.name
