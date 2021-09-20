import random

import Master_Class as MC
import People as P
import PeopleFuncs as PF
import Miscellaneous as M


first_forest  = MC.Area("First-off Forest", 1, "Forest", True, 4, PF.create_sub_boss(25), 25)
second_swamp  = MC.Area("Second Swamp", 2, "Swamp", True, 5, PF.create_sub_boss(50), 50)
third_thunder = MC.Area("Third Thunder", 3, "Special", True, 7, PF.create_sub_boss(75), 75)

# homestead = MC.Area("Homestead", 11, "Town", False, 0, PF.create_doctor(75))
# store...
# blacksmith...
# gun shop


def initialise_area(area: MC.Area, key:M.Key):
    P.enemy_list = []
    for i in range(area.get_enemy_number()):
        P.enemy_list[i] = PF.create_bad_goon()
    keyholder = random.randint(0, len(P.enemy_list)-1)
    P.enemy_list[keyholder].clear_inventory()
    P.enemy_list[keyholder].add_to_inventory("the key for the area")                                                     # Update this with the actual key
    #
    # Menu menu:
    # list of places:
    # 1
    # 2
    # 3
    # .....
    #
    # input number
    #
    # initialise_area(first_forest)

