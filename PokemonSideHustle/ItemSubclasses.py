import Main_Class as MC


class Potions(MC.Items):
    def __init__(self, Name, Value, Heal_Amount):
        super().__init__(Name, Value, Type="Potions")
        self.__name = Name
        self.__value = Value
        self.__heal_amount = Heal_Amount

    def get_strength(self):
        return self.__heal_amount

class Berries(MC.Items):
    def __init__(self, Name, Value):
        super().__init__(Name, Value, Type="Berries")
        self.__name = Name
        self.__value = Value

class BattleItems(MC.Items):
    def __init__(self, Name, Value, AffectedStat, Effect):
        super().__init__(Name, Value, Type="Battle Items")
        self.__name = Name
        self.__value = Value
        self.__affected_stat = AffectedStat
        self.__effect = Effect
