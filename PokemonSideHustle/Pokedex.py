import Main_Class as classes

class Charmander(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Charmander", HP=282, Attack=223, Defence=203, Speed=251, Next_Evolution=Charmeleon(),
                         Base_Exp_Given=62, Type1="Fire", Nickname=Nickname)

class Charmeleon(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Charmeleon", HP=320, Attack=249, Defence=236, Speed=284, Next_Evolution=Charizard(),
                         Base_Exp_Given=142, Type1="Fire", Nickname=Nickname)

class Charizard(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Charizard", HP=360, Attack=293, Defence=280, Speed=328, Next_Evolution=None,
                         Base_Exp_Given=267, Type1="Fire", Type2="Flying", Nickname=Nickname)


class Pikachu(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Pikachu", HP=211, Attack=131, Defence=117, Speed=306, Next_Evolution=Raichu(),
                         Base_Exp_Given=112, Type1="Electric", Nickname=Nickname)


class Raichu(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Raichu", HP=324, Attack=306, Defence=229, Speed=350, Next_Evolution=None,
                         Base_Exp_Given=243, Type1="Electric", Nickname=Nickname)


class Magikarp(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Magikarp", HP=244, Attack=130, Defence=229, Speed=284, Next_Evolution=Gyarados(),
                         Base_Exp_Given=40, Type1="Water", Nickname=Nickname)


class Gyarados(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Gyarados", HP=394, Attack=383, Defence=282, Speed=287, Next_Evolution=None,
                         Base_Exp_Given=189, Type1="Water", Type2="Flying", Nickname=Nickname)


########################################################################################################################
class Testemon(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Testemon", HP=250, Attack=10, Defence=10, Speed=5, Next_Evolution=Testemon2(),
                         Base_Exp_Given=25, Type1="Normal", Nickname=Nickname)
class Testemon2(classes.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Testemon Two", HP=25000, Attack=10000, Defence=10000, Speed=5000, Next_Evolution=None,
                         Base_Exp_Given=25000, Type1="Normal", Nickname=Nickname)
########################################################################################################################


def check_for_level_up(pokemon: classes.Pokemon, exp_gain):
    next_level = pokemon.get_level() + 1
    total_exp = pokemon.get_total_exp()
    new_exp = total_exp + exp_gain
    exp_threshold = pow(next_level, 3)
    if new_exp > exp_threshold:
        pokemon.level_up()
        pokemon.set_exp_c(new_exp-exp_threshold)
        pokemon.gain_exp_t(exp_gain)
        print(f"Congratulations! {pokemon.get_name()} levelled up!")
    else:
        pokemon.both_gain_exp()


def evolution(first: classes.Pokemon):

    unevolved_mon = first.get_mon_name()
    second = first.fetch_next_evol()
    nickname = first.get_name()
    moves = first.get_moves()

    if nickname != first.get_mon_name():
        second.set_nickname(nickname)
    second.reset_moves(moves)
    print(f"Congratulations! Your {unevolved_mon} evolved into a {second.get_mon_name()}!")

    return second
