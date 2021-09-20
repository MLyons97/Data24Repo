import random

import Main_Classes as classes


def __DamageCalc(Move: classes.Moves, Attacker: classes.Pokemon, Defender: classes.Pokemon):
    move_power = Move.get_power()
    attack_power = Attacker.get_attack()
    defence_power = Defender.get_defence()
    level = 100
    roll = random.uniform(0.85, 1.00)
    if Move.get_type() in Attacker.get_type():
        STAB = 1.5
    else:
        STAB = 1
    damage = int(((((( (2*level) / 5) + 2) * move_power * (attack_power/defence_power)) / 50) + 2) * roll * STAB)
    return damage


def feint_check(pokemon: classes.Pokemon):
    if pokemon.get_hp() <= 0:
        return True
    else:
        return False
