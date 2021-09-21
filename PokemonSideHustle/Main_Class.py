class Pokemon(object):
    def __init__(self, Name, HP, Attack, Defence, Type1, Type2=0, Nickname = None):
        self.__name       = Name
        if Nickname != None:
            self.__nickname = Nickname
        else:
            self.__nickname   = Name
        self.__max_hp     = HP
        self.__current_hp = HP
        self.__defence    = Defence
        self.__attack     = Attack
        self.__type1      = Type1
        self.__type2      = Type2
        self.__feint      = False

    def get_hp(self):
        return self.__current_hp

    def set_hp(self, value):
        self.__current_hp = value

    def take_damage(self, damage):
        self.__current_hp = self.__current_hp-damage

    def heal_to_full(self):
        self.__current_hp = self.__max_hp

    def heal_by_amount(self, amount):
        self.__current_hp += amount

    def get_attack(self):
        return self.__attack

    def set_attack(self, New_Attack):
        self.__attack = New_Attack

    def get_defence(self):
        return self.__defence

    def set_defence(self, New_Defence):
        self.__defence = New_Defence

    def get_type(self):
        if self.__type2 != 0:
            return f"{self.__type1}, {self.__type2}"
        else:
            return self.__type1

    def get_name(self):
        if len(self.__nickname) > 0:
            return self.__nickname
        else:
            return self.__name

    def feinted(self):
        self.__feint = True

class Moves:
    def __init__(self, Name, BasePower, Type):
        self.__name = Name
        self.__base_power = BasePower
        self.__type = Type

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__base_power

    def get_type(self):
        return self.__type
