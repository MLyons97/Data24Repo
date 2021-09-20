import random

import People as P


def create_player():
    player_name = input("Please enter your hero's name: ")
    base_health = 100
    base_damage = 10
    weapon = "hands"
    ranged_weapon = ""
    player = P.GoodGuy(player_name, base_health, base_damage, weapon)
    player.add_to_inventory("a thing")
    player.change_balance(10)
    return player


def create_villain():
    villain_name = "Dastardly Danny"
    base_health = 1000
    base_damage = 99
    weapon = "hands"
    villain = P.BadGuy(villain_name, base_health, base_damage, weapon)
#    villain.setpet(Wolf)                                                                                                ## Wolf Needed
    return villain


def create_sub_boss(difficulty: int):
    villain_name = random.choice(P.list_of_sidekicks)
    P.list_of_sidekicks.remove(villain_name)
    base_health = 10*difficulty
    base_damage = 2*difficulty
    weapon = "hands"
    sub_villain = P.BadGuy(villain_name, base_health, base_damage, weapon)
    return sub_villain


def create_good_goon():
    good_goon = P.GoodGuy(random.choice(P.list_of_good_names), random.randint(40,60), random.randint(1,4), "one hand")
    P.friend_list.append(good_goon)
    return good_goon


def create_bad_goon():
    bad_goon = P.BadGuy(random.choice(P.list_of_bad_names), (random.randint(30, 70)),
                        random.randint(2,4), "one hand")
    P.enemy_list.append(bad_goon)
    bad_goon.change_balance(random.randint(1,20))
    return bad_goon

def create_doctor(healing_power):
    doctor = P.Doctor("Dr. " + random.choice(P.list_of_doctor_names), 100, healing_power)
    P.doctor_list.append(doctor)
    return doctor
###########################################################################################################
