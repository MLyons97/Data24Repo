class Moves:
    def __init__(self, Name, BasePower, Accuracy, Type):
        self.__name = Name
        self.__base_power = BasePower
        self.__accuracy = Accuracy
        self.__type = Type

    def get_name(self):
        return self.__name

    def get_power(self):
        return self.__base_power

    def get_accuracy(self):
        return self.__accuracy

    def get_type(self):
        return self.__type


class Pokemon(object):
    def __init__(self, Name, HP, Attack, Defence, Speed, Next_Evolution,
                 Base_Exp_Given, Type1, Type2=0, Nickname = None,
                 Total_EXP = 0, Current_EXP = 0):
        self.__name = Name
        if Nickname is not None:
            self.__nickname = Nickname
        else:
            self.__nickname = Name
        self.__max_hp = HP
        self.__current_hp = HP
        self.__attack = Attack
        self.__defence = Defence
        self.__speed = Speed
        self.__base_exp = Base_Exp_Given
        self.__type1 = Type1
        self.__type2 = Type2
        self.__feint = False
        self.__moves = []
        self.__next_evolution = Next_Evolution
        self.__level = 5
        self.__current_exp = 0
        self.__total_exp = 0

    def get_name(self):
        if len(self.__nickname) > 0:
            return self.__nickname
        else:
            return self.__name

    def get_mon_name(self):
        return self.__name

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

    def get_speed(self):
        return self.__speed

    def set_speed(self, New_Speed):
        self.__speed = New_Speed

    def fetch_next_evol(self):
        return self.__next_evolution

    def get_type(self):
        if self.__type2 != 0:
            return [self.__type1, self.__type2]
        else:
            return [self.__type1]

    def get_moves(self):
        return self.__moves

    def reset_moves(self, moves: list):
        self.__moves.clear()
        self.__moves = moves

    def learn_new_move(self, move: Moves):
        self.__moves.append(move)

    def forget_move(self, move: Moves):
        self.__moves.remove(move)

    def feinted(self):
        self.__feint = True

    def get_level(self):
        return self.__level

    def level_up(self):
        self.__level += 1

    def set_level(self, required_level):
        self.__level = required_level
        self.__total_exp = pow(required_level, 3)
        self.__current_exp = 0

    def get_total_exp(self):
        return self.__total_exp

    def get_current_exp(self):
        return self.__current_exp

    def gain_exp_t(self, gain_amount):
        self.__total_exp += gain_amount

    def gain_exp_c(self, gain_amount):
        self.__current_exp += gain_amount

    def both_gain_exp(self, gain_amount):
        self.gain_exp_t(gain_amount)
        self.gain_exp_c(gain_amount)

    def set_exp_c(self, new_value):
        self.__current_exp = new_value

    def get_base_exp_given(self):
        return self.__base_exp

    def set_nickname(self, new_nickname):
        self.__nickname = new_nickname


class Items(object):
    def __init__(self, Name, Value, Type):
        self.__name = Name
        self.__value = Value
        self.__type = Type

    def get_name(self):
        return self.__name

    def get_value(self):
        return self.__value

    def get_type(self):
        return self.__type

class Player(object):
    def __init__(self, Name: str, Party: list, Box: list, Inventory = dict):
        self.__name = Name
        self.__party = Party
        self.__box = Box
        self.__bag = Inventory

    def get_name(self):
        return self.__name

    def get_party(self):
        return self.__party

    def add_to_party(self, pokemon: Pokemon):
        while len(self.get_party()) > 6:
            decider = input("You already have a full party!\n"
                            "Please select one to return to the box, or enter a letter to exit.")
            for i in self.get_party():
                print(f"{i.index() + 1}. {i}")
            if decider.isalpha():
                return
            elif 0 <= int(decider) -1 < len(self.get_party()):
                self.add_to_box_from_party(self.get_party()[int(decider)])
        self.get_party().append(pokemon)

    def add_to_box_from_party(self, pokemon: Pokemon):
        print(f"You are returning {pokemon} to the box!")
        self.__box.append(pokemon)
        self.__party.remove(pokemon)

    def get_box(self):
        return self.__box

    def print_box_list(self):
        for i in self.get_box():
            print(f"{i.index() + 1}. {i}")

    def create_bag(self):
        self.__bag["Potions"] = []
        self.__bag["Berries"] = []
        self.__bag["Battle Items"] = []
        self.__bag["TMs"] = []

    def get_bag(self):
        return self.__bag

    def add_to_bag(self, item: Items):
        self.get_bag()[item.get_type()].append(item)

