import PeopleFuncs as PF
import People as P
import Actions as A
import Areas as Ar
import Miscellaneous_List as ML

MainChar = PF.create_player()
MainVillain = PF.create_villain()
P.enemy_list.append(MainVillain)
battle_counter = 0

doc1 = PF.create_doctor(100)

print("You've stumbled into some woods! They don't look all that fancy")
current_area = Ar.first_forest
Ar.initialise_area(current_area, ML.Key_1)


#current_boss = current_area.get_area_boss()

while len(P.enemy_list) > 0:

    A.battle_state(MainChar, A.enemy_select(P.enemy_list))
    #
    # if len(P.enemy_list) == 0 or ML.Key_1 in MainChar.get_inventory():
    #     print(f"You have found the area's boss! It's the one and only {current_boss.get_name()}!!!\n"
    #           f"They're super strong, so you better be ready!")
    #     A.battle_state(MainChar, current_boss)

    if not MainChar.get_is_alive():
        print(f"\nYou survived {battle_counter} battle(s)!")
        break
    else:
        A.heal_check(MainChar, doc1)
    battle_counter += 1
    print(f"...There are {len(P.enemy_list)} enemies left!\n")
