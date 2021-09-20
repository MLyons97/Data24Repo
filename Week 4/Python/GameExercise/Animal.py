import Master_Class as MC

class Animal(MC.Animal):
    def __init__(self, name: int, colour: str, type: str, health: int, damage: int):
        self.__name = name
        self.__colour = colour
        self.__type = type
        self.__health = health  # Number of lives
        self.__damage = damage  # Attack power
        self.__is_good = None
    def get_name(self):
        return self.__name
    def get_colour(self):
        return self.__colour
    def get_type(self):
        return self.__type
    def get_health(self):
        return self.__health
    def set_health(self, new_health):
        self.__health = new_health
    def get_damage(self):
        return self.__damage
    def get_good(self):
        return self.__is_good
    def set_allignment(self, good: bool):
        if good:
            self.__is_good = True
        else:
            self.__is_good = False

list_of_animals = ["Dog", "Horse", "Wolf", "Troll", "Werewolf"]