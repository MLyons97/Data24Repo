# Main classes that everything will inherit from
class Animal:
    def __init__(self, name: int, health: int, damage: int):
        self.__name = name
        self.__health = health
        self.__damage = damage
        self.__is_good = None

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        self.__health = new_health

    def get_damage(self):
        return self.__damage

    def get_good(self):
        return self.__is_good

    def take_damage(self, damage: int):
        self.__current_health = self.get_health() - damage

    def set_allignment(self, good: bool):
        if good:
            self.__is_good = True
        else:
            self.__is_good = False


class Person:
    def __init__(self, name: str, health: int, base_damage: int,
                 weapon: str, ranged_weapon: str, is_good: bool, is_alive: bool):                                        # Key attributes that all 'persons'
        self.__name = name                                                                                               # will have
        self.__max_health = health
        self.__current_health = health
        self.__base_damage = base_damage
        self.__weapon = weapon
        self.__ranged_weapon = ranged_weapon
        self.__is_good = is_good
        self.__is_alive = is_alive
        self.__inventory = []
        self.__money = 0
        self.__pet = None

    def get_name(self) -> str:                                                                                           # Getters & Setters
        return self.__name

    def get_health(self):
        return self.__current_health

    def get_max_health(self):
        return self.__max_health

    def set_health(self, new_health):
        self.__current_health = new_health

    def take_damage(self, damage: int):
        self.__current_health = self.get_health() - damage

    def heal(self, heal_amount):
        if self.get_health() + heal_amount > self.__max_health:
            self.set_health(self.__max_health)
        else:
            self.set_health(self.get_health() + heal_amount)
        print(f"You have been healed up to {self.get_health()}")

    def get_damage(self):
        return self.__base_damage

    def get_weapon(self):
        return self.__weapon

    def new_weapon(self, new_weapon):
        print(f"Are you sure you want to change your {self.get_weapon()} for a {new_weapon}?")
        decision = input("Type 1 to change or 2 to keep.")
        checker = True
        while checker:
            if decision == 1:
                self.__weapon = new_weapon
                print(f"You now have the {new_weapon}!")
                checker = False
            elif decision == 2:
                print(f"You have decided to keep your {self.get_weapon()}")
                checker = False
            else:
                print("Please enter only 1 or 2")

    def get_ranged_weapon(self):
        return self.__weapon

    def new_ranged_weapon(self, new_weapon):
        print(f"Are you sure you want to change your {self.get_ranged_weapon()} for a {new_weapon}?")
        decision = input("Type 1 to change or 2 to keep.")
        checker = True
        while checker:
            if decision == 1:
                self.__ranged_weapon = new_weapon
                print(f"You now have the {new_weapon}!")
                checker = False
            elif decision == 2:
                print(f"You have decided to keep your {self.get_ranged_weapon()}")
                checker = False
            else:
                print("Please enter only 1 or 2")

    def is_good(self):
        return self.__is_good

    def change_of_heart(self):
        if self.is_good():
            self.__is_good = False
        else:
            self.__is_good = True

    def get_is_alive(self):
        return self.__is_alive

    def kill_off(self):
        if not self.__is_alive:
            print("They're already dead!")
        else:
            self.__is_alive = False

    def resurrect(self):
        if self.__is_alive:
            print("They're already alive!")
        else:
            self.__is_alive = True

    def get_inventory(self):
        return self.__inventory

    def add_to_inventory(self, item):
        self.__inventory.append(item)

    def remove_from_inventory(self, item):
        self.__inventory.remove(item)

    def clear_inventory(self):
        self.__inventory.clear()

    def get_balance(self):
        return self.__money

    def change_balance(self, change):
        self.__money += change

    def get_pet(self):
        return self.__pet

    def get_new_pet(self, new_pet: Animal):
        if not self.get_pet():
            self.__pet = new_pet
        else:
            check1 = True
            while check1:
                check = input(f"Do you want to replace your current {self.get_pet().get_name()} with a {new_pet.get_name()}?\n-->Y/N")
                if check == "Y":
                    self.__pet = new_pet
                    print(f"You now have a {self.get_pet().get_name()} as a pet!")
                    check1 = False
                elif check == "N":
                    print(f"You have kept your {self.get_pet().get_name()}")
                    check1 = False
                else:
                    print("The animal couldn't understand you! Please enter either Y or N.\n")

    def setpet(self, pet: Animal):
        self.__pet = pet


class Items:
    def __init__(self, cost: int, category: str):
        self.__cost = cost
        self.__category = category



    def get_cost(self):
        return str(self.cost)

    def get_category(self):
        return self.category



class Area:
    def __init__(self, name:str, id_number: int, category: str, is_battle_area: bool, enemies: int,
                 difficulty: int, boss: Person):
        self.__name = name
        self.__id_number = id_number
        self.__category = category
        self.__is_battle_area = is_battle_area
        self.__enemies = enemies
        self.__boss = boss
        self.__difficulty = difficulty

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id_number

    def get_category(self):
        return self.__category

    def check_battle_area(self):
        return self.__is_battle_area

    def get_enemy_number(self):
        return self.__enemies

    def get_area_boss(self):
        return self.__boss

    def get_difficulty(self):
        return self.__difficulty