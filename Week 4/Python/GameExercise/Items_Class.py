import Master_Class as MC

class Weapon(MC.Items):
    def __init__(self, Damage: int):
        super().__init__()
        self.__damage = Damage
        self.__cost = Cost


class Consumables(MC.Items):
    pass


class Misc(MC.Items): # Letters and keys and ting
    pass