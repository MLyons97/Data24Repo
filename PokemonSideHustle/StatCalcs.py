import Main_Class as MC


def HP_Calc(pokemon: MC.Pokemon):
    base_hp = pokemon.get_base_hp()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_hp + iv + (ev / 4)) * level
    hp = (numerator/100) + level + 10
    return hp


def atk_calc(pokemon: MC.Pokemon):
    base_atk = pokemon.get_base_attack()
    iv = 10
    ev = 100
    level = pokemon.get_level()
    numerator = (2 * base_atk + iv + (ev / 4)) * level
    return (numerator/100) + 5

