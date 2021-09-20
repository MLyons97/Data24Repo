import Main_Classes as classes
import Calculations as calcs


def attack(attacker: classes.Pokemon, attackee: classes.Pokemon, move: classes.Moves):
    print(f"{attacker.get_name()} used {move.get_name()}!")
    damage = calcs.__DamageCalc(move, attacker, attackee)
    print(f"It did {damage} points of damage!")
    attackee.update_hp(damage)
    if calcs.feint_check(attackee):
        print(f"{attackee.get_name()} has fainted!")
        return True
    else:
        print(f"{attackee.get_name()} has {attackee.get_hp()} HP left!\n")
        return False