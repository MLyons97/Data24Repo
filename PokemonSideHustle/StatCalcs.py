import Main_Class as MC
import math as m


def HP_Calc(pokemon: MC.Pokemon):
    base_hp = pokemon.get_base_hp()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = ((2 * base_hp) + iv + (ev / 4)) * level
    print(numerator)
    hp = (numerator/100) + level + 10
    print(hp)
    return m.floor(hp)


def atk_calc(pokemon: MC.Pokemon):
    base_atk = pokemon.get_base_attack()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_atk + iv + (ev / 4)) * level
    return m.floor((numerator/100) + 5)


def def_calc(pokemon: MC.Pokemon):
    base_def = pokemon.get_base_defence()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_def + iv + (ev / 4)) * level
    return m.floor((numerator/100) + 5)


def sp_atk_calc(pokemon: MC.Pokemon):
    base_sp_atk = pokemon.get_base_sp_attack()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_sp_atk + iv + (ev / 4)) * level
    return m.floor((numerator/100) + 5)


def sp_def_calc(pokemon: MC.Pokemon):
    base_sp_def = pokemon.get_base_sp_defence()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_sp_def + iv + (ev / 4)) * level
    return m.floor((numerator/100) + 5)


def speed_calc(pokemon: MC.Pokemon):
    base_speed = pokemon.get_base_speed()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_speed + iv + (ev / 4)) * level
    return m.floor((numerator/100) + 5)
