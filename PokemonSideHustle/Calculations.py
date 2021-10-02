import random as r
import Main_Class as MC
import Weakness_Chart as WC


def __DamageCalc(Move: MC.Moves, Attacker: MC.Pokemon, Defender: MC.Pokemon):
    move_power = Move.get_power()
    attack_power = Attacker.get_attack()
    defence_power = Defender.get_defence()
    move_type = Move.get_type()
    defender_types = Defender.get_type()
    type_effectiveness = 1

    for i in range(0, len(defender_types), 1):
        type_effectiveness = type_effectiveness * WC.type_effectiveness_dict[defender_types[i]][str(move_type)]
    if type_effectiveness > 1:
        print("It's super effective")
    elif 1 > type_effectiveness > 0:
        print("It's not very effective...")
    elif type_effectiveness == 0:
        print(f"It doesn't effect {Defender.get_name()}!")

    level = Attacker.get_level()
    roll = r.uniform(0.85, 1.00)
    if Move.get_type() in Attacker.get_type():
        STAB = 1.5
    else:
        STAB = 1
    damage = int(((((( (2*level) / 5) + 2) * move_power * (attack_power/defence_power)) / 50) + 2)
                 * roll * STAB * type_effectiveness)
    return damage


def faint_check(pokemon: MC.Pokemon):
    if pokemon.get_hp() <= 0:
        pokemon.feinted()
        pokemon.set_hp(0)
        return True
    else:
        return False

def exp_gain(winner: MC.Pokemon, loser: MC.Pokemon):
    winner_level = winner.get_level()
    loser_level = loser.get_level()
    base_exp = loser.get_base_exp_given()
    egg_factor = 1
    affection_factor = 1
    traded_factor = 1
    unevolved_factor = 1
    exp_share_factor = 1
    term_1 = (base_exp*loser_level*affection_factor*unevolved_factor)/(5*exp_share_factor)
    term_2 = ((2*loser_level) + 10)/(loser_level+winner_level+10)
    term_2 = pow(term_2, 2.5)
    exp = term_1*term_2*traded_factor*egg_factor
    return exp

