import Main_Class as classes
import Calculations as calcs

import random as r

def attack(attacker: classes.Pokemon, attackee: classes.Pokemon, move: classes.Moves):
    print(f"{attacker.get_name()} used {move.get_name()}!")
    if r.random() <= move.get_accuracy():
        damage = calcs.__DamageCalc(move, attacker, attackee)
        print(f"It did {damage} points of damage!")
        attackee.take_damage(damage)
    else:
        print("But it missed!\n")
        return False
