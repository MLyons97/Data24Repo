import Main_Class as MC


class Bulbasaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Bulbasaur", HP=294, Attack=216, Defence=216, Speed=207,
                         Base_HP=45, Base_Atk=49, Base_Def=49, Base_SpAtk=65, Base_SpDef=65, Base_Spd=45,
                         Base_Exp_Given=64, Next_Evolution=Ivysaur(), Type1="Grass", Type2="Poison", Nickname=Nickname)


class Ivysaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Ivysaur", HP=324, Attack=245, Defence=247, Speed=240,
                         Base_HP=60, Base_Atk=62, Base_Def=63, Base_SpAtk=80, Base_SpDef=80, Base_Spd=60,
                         Base_Exp_Given=142, Next_Evolution=Venusaur(), Type1="Grass", Type2="Poison", Nickname=Nickname)


class Venusaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Venusaur", HP=364, Attack=289, Defence=291, Speed=284,
                         Base_HP=80, Base_Atk=82, Base_Def=83, Base_SpAtk=100, Base_SpDef=100, Base_Spd= 80,
                         Base_Exp_Given=263, Next_Evolution=None, Type1="Grass", Type2="Poison", Nickname=Nickname)


class Charmander(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charmander", HP=282, Attack=223, Defence=203, Speed=251,
                         Base_HP=39, Base_Atk=52, Base_Def=43, Base_SpAtk=60, Base_SpDef=50, Base_Spd=65,
                         Next_Evolution=Charmeleon(), Base_Exp_Given=62, Type1="Fire", Nickname=Nickname)


class Charmeleon(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charmeleon", HP=320, Attack=249, Defence=236, Speed=284,
                         Base_HP=58, Base_Atk=64, Base_Def=58, Base_SpAtk=80, Base_SpDef=65, Base_Spd=80,
                         Next_Evolution=Charizard(), Base_Exp_Given=142, Type1="Fire", Nickname=Nickname)

class Charizard(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charizard", HP=360, Attack=293, Defence=280, Speed=328,
                         Base_HP=78, Base_Atk=84, Base_Def=78, Base_SpAtk=109, Base_SpDef=85, Base_Spd=100,
                         Next_Evolution=None, Base_Exp_Given=267, Type1="Fire", Type2="Flying", Nickname=Nickname)


class Squirtle(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Squirtle", HP=292, Attack=214, Defence=251, Speed=203,
                         Base_HP=44, Base_Atk=48, Base_Def=65, Base_SpAtk=50, Base_SpDef=64, Base_Spd=43,
                         Next_Evolution=Wartortle(), Base_Exp_Given=63, Type1="Water", Nickname=Nickname)


class Wartortle(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Wartortle", HP = 322, Attack=247, Defence=284, Speed=236,
                         Base_HP=59, Base_Atk=63, Base_Def=80, Base_SpAtk=65, Base_SpDef=80, Base_Spd=58,
                         Next_Evolution=Blastoise(), Base_Exp_Given=142, Type1="Water", Nickname=Nickname)


class Blastoise(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Blastoise", HP = 362, Attack=291, Defence=328, Speed=280,
                         Base_HP=79, Base_Atk=83, Base_Def=100, Base_SpAtk=85, Base_SpDef=105, Base_Spd=78,
                         Next_Evolution=None, Base_Exp_Given=265, Type1="Water", Nickname=Nickname)

class Pikachu(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Pikachu", HP=211, Attack=131, Defence=117, Speed=306,
                         Base_HP=35, Base_Atk=55, Base_Def=40, Base_SpAtk=50, Base_SpDef=50, Base_Spd=90,
                         Next_Evolution=Raichu(), Base_Exp_Given=112, Type1="Electric", Nickname=Nickname)


class Raichu(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Raichu", HP=324, Attack=306, Defence=229, Speed=350,
                         Base_HP=60, Base_Atk=90, Base_Def=55, Base_SpAtk=109, Base_SpDef=80, Base_Spd=110,
                         Next_Evolution=None, Base_Exp_Given=243, Type1="Electric", Nickname=Nickname)


class Magikarp(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Magikarp", HP=244, Attack=130, Defence=229, Speed=284,
                         Base_HP=20, Base_Atk=10, Base_Def=55, Base_SpAtk=15, Base_SpDef=20, Base_Spd=80,
                         Next_Evolution=Gyarados(),Base_Exp_Given=40, Type1="Water", Nickname=Nickname)


class Gyarados(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Gyarados", HP=394, Attack=383, Defence=282, Speed=287,
                         Base_HP=95, Base_Atk=125, Base_Def=79, Base_SpAtk=60, Base_SpDef=100, Base_Spd=81,
                         Next_Evolution=None, Base_Exp_Given=189, Type1="Water", Type2="Flying", Nickname=Nickname)


########################################################################################################################
class Testemon(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Testemon", HP=250, Attack=10, Defence=10, Speed=5, Next_Evolution=Testemon2(),
                         Base_Exp_Given=25, Type1="Normal", Nickname=Nickname)
class Testemon2(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Testemon Two", HP=25000, Attack=10000, Defence=10000, Speed=5000, Next_Evolution=None,
                         Base_Exp_Given=25000, Type1="Normal", Nickname=Nickname)
########################################################################################################################


def check_for_level_up(pokemon: MC.Pokemon, exp_gain):
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


def evolution(first: MC.Pokemon):

    unevolved_mon = first.get_mon_name()
    second = first.fetch_next_evol()
    nickname = first.get_name()
    moves = first.get_moves()

    if nickname != first.get_mon_name():
        second.set_nickname(nickname)
    second.reset_moves(moves)
    print(f"Congratulations! Your {unevolved_mon} evolved into a {second.get_mon_name()}!")

    return second
