import Main_Class as MC
########################################################################################################################
# Pokemon Classes

class Bulbasaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Bulbasaur", Next_Evolution=Ivysaur(), Type1="Grass", Type2="Poison", Nickname=Nickname,
                         Base_HP=45, Base_Atk=49, Base_Def=49, Base_SpAtk=65, Base_SpDef=65, Base_Spd=45,
                         Base_Exp_Given=64)


class Ivysaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Ivysaur", Next_Evolution=Venusaur(), Type1="Grass", Type2="Poison", Nickname=Nickname,
                         Base_HP=60, Base_Atk=62, Base_Def=63, Base_SpAtk=80, Base_SpDef=80, Base_Spd=60,
                         Base_Exp_Given=142)


class Venusaur(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Venusaur", Next_Evolution=None, Type1="Grass", Type2="Poison", Nickname=Nickname,
                         Base_HP=80, Base_Atk=82, Base_Def=83, Base_SpAtk=100, Base_SpDef=100, Base_Spd= 80,
                         Base_Exp_Given=263)


class Charmander(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charmander", Next_Evolution=Charmeleon(), Type1="Fire", Nickname=Nickname,
                         Base_HP=39, Base_Atk=52, Base_Def=43, Base_SpAtk=60, Base_SpDef=50, Base_Spd=65,
                         Base_Exp_Given=62)


class Charmeleon(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charmeleon", Next_Evolution=Charizard(), Type1="Fire", Nickname=Nickname,
                         Base_HP=58, Base_Atk=64, Base_Def=58, Base_SpAtk=80, Base_SpDef=65, Base_Spd=80,
                         Base_Exp_Given=142)

class Charizard(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Charizard", Next_Evolution=None, Type1="Fire", Type2="Flying", Nickname=Nickname,
                         Base_HP=78, Base_Atk=84, Base_Def=78, Base_SpAtk=109, Base_SpDef=85, Base_Spd=100,
                        Base_Exp_Given=267)


class Squirtle(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Squirtle", Type1="Water", Nickname=Nickname, Next_Evolution=Wartortle(),
                         Base_HP=44, Base_Atk=48, Base_Def=65, Base_SpAtk=50, Base_SpDef=64, Base_Spd=43,
                         Base_Exp_Given=63)


class Wartortle(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Wartortle", Next_Evolution=Blastoise(), Type1="Water", Nickname=Nickname,
                         Base_HP=59, Base_Atk=63, Base_Def=80, Base_SpAtk=65, Base_SpDef=80, Base_Spd=58,
                         Base_Exp_Given=142)


class Blastoise(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Blastoise", Next_Evolution=None, Type1="Water", Nickname=Nickname,
                         Base_HP=79, Base_Atk=83, Base_Def=100, Base_SpAtk=85, Base_SpDef=105, Base_Spd=78,
                         Base_Exp_Given=265)


class Caterpie(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Caterpie", Next_Evolution=Metapod(), Type1="Bug", Nickname=Nickname,
                         Base_HP=45, Base_Atk=30, Base_Def=35, Base_SpAtk=20, Base_SpDef=20, Base_Spd=45,
                         Base_Exp_Given=39)


class Metapod(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Metapod", Next_Evolution=Butterfree(),Type1="Bug", Nickname=Nickname,
                         Base_HP=50, Base_Atk=20, Base_Def=55, Base_SpAtk=25, Base_SpDef=25, Base_Spd=30,
                         Base_Exp_Given=72)


class Butterfree(MC.Pokemon):
    def __init__(self, Nickname = None):
        super().__init__(Name="Butterfree", Next_Evolution=None, Type1="Bug", Type2="Flying", Nickname=Nickname,
                         Base_HP=60, Base_Atk=45, Base_Def=50, Base_SpAtk=90, Base_SpDef=80, Base_Spd=70,
                         Base_Exp_Given=198)


class Weedle(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Weedle", Next_Evolution=Kakuna(), Type1="Bug", Type2="Poison", Nickname=Nickname,
                         Base_HP=40, Base_Atk=35, Base_Def=30, Base_SpAtk=20, Base_SpDef=20, Base_Spd=50,
                         Base_Exp_Given=39)


class Kakuna(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Kakuna", Next_Evolution=Beedrill(), Type1="Bug", Type2="Poison", Nickname=Nickname,
                         Base_HP=45, Base_Atk=25, Base_Def=50, Base_SpAtk=25, Base_SpDef=25, Base_Spd=35,
                         Base_Exp_Given=72)

class Beedrill(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Beedrill", Next_Evolution=None, Type1="Bug", Type2="Poison", Nickname=Nickname,
                         Base_HP=65, Base_Atk=90, Base_Def=40, Base_SpAtk=45, Base_SpDef=80, Base_Spd=75,
                         Base_Exp_Given=198)


class Pidgey(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Pidgey", Next_Evolution=Pidgeotto(), Type1="Normal", Type2="Flying", Nickname=Nickname,
                         Base_HP=40, Base_Atk=45, Base_Def=40, Base_SpAtk=35, Base_SpDef=35, Base_Spd=56,
                         Base_Exp_Given=50)


class Pidgeotto(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Pidgeotto", Next_Evolution=Pidgeot(), Type1="Normal", Type2="Flying", Nickname=Nickname,
                         Base_HP=63, Base_Atk=60, Base_Def=55, Base_SpAtk=50, Base_SpDef=50, Base_Spd=71,
                         Base_Exp_Given=122)


class Pidgeot(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Pidgeot", Next_Evolution=None, Type1="Normal", Type2="Flying", Nickname=Nickname,
                         Base_HP=83, Base_Atk=80, Base_Def=75, Base_SpAtk=70, Base_SpDef=70, Base_Spd=101,
                         Base_Exp_Given=240)



class Rattata(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Rattata", Next_Evolution=Raticate(), Type1="Normal", Nickname=Nickname,
                         Base_HP=30, Base_Atk=56, Base_Def=35, Base_SpAtk=25, Base_SpDef=35, Base_Spd=72,
                         Base_Exp_Given=51)


class Raticate(MC.Pokemon):
    def __init__(self, Nickanme=None):
        super().__init__(Name="Raticate", Next_Evolution=None, Type1="Normal", Nickname=Nickanme,
                         Base_HP=55, Base_Atk=81, Base_Def=60, Base_SpAtk=50, Base_SpDef=70, Base_Spd=97,
                         Base_Exp_Given=145)


class Spearow(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Spearow", Next_Evolution=Fearow(), Type1="Normal", Type2="Flying", Nickname=Nickname,
                         Base_HP=40, Base_Atk=60, Base_Def=30, Base_SpAtk=31, Base_SpDef=31, Base_Spd=70,
                         Base_Exp_Given=52)


class Fearow(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Fearow", Next_Evolution=None, Type1="Normal", Type2="Flying", Nickname=Nickname,
                         Base_HP=65, Base_Atk=90, Base_Def=65, Base_SpAtk=61, Base_SpDef=61, Base_Spd=100,
                         Base_Exp_Given=155)


class Ekans(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Ekans", Next_Evolution=Arbok(), Type1="Poison", Nickname=Nickname,
                         Base_HP=35, Base_Atk=60, Base_Def=44, Base_SpAtk=40, Base_SpDef=54, Base_Spd=55,
                         Base_Exp_Given=58)


class Arbok(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Arbok", Next_Evolution=None, Type1="Poison", Nickname=Nickname,
                         Base_HP=60, Base_Atk=95, Base_Def=69, Base_SpAtk=65, Base_SpDef=79, Base_Spd=80,
                         Base_Exp_Given=448)


class Pikachu(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Pikachu", Next_Evolution=Raichu(), Type1="Electric", Nickname=Nickname,
                         Base_HP=35, Base_Atk=55, Base_Def=40, Base_SpAtk=50, Base_SpDef=50, Base_Spd=90,
                         Base_Exp_Given=112)


class Raichu(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Raichu", Next_Evolution=None, Type1="Electric", Nickname=Nickname,
                         Base_HP=60, Base_Atk=90, Base_Def=55, Base_SpAtk=109, Base_SpDef=80, Base_Spd=110,
                         Base_Exp_Given=243)


class Sandshrew(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Sandshrew", Next_Evolution=Sandslash, Type1="Ground", Nickname=Nickname,
                         Base_HP=50, Base_Atk=75, Base_Def=85, Base_SpAtk=20, Base_SpDef=30, Base_Spd=40,
                         Base_Exp_Given=60)


class Sandslash(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Sandslash", Next_Evolution=None, Type1="Ground", Nickname=Nickname,
                         Base_HP=75, Base_Atk=100, Base_Def=110, Base_SpAtk=45, Base_SpDef=55, Base_Spd=65,
                         Base_Exp_Given=60)


class Nidoranf(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidoran (female)", Next_Evolution=Nidorina, Type1="Poison", Nickname=Nickname,
                         Base_HP=55, Base_Atk=47, Base_Def=52, Base_SpAtk=40, Base_SpDef=40, Base_Spd=41,
                         Base_Exp_Given=55)


class Nidorina(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidorina", Next_Evolution=Nidoqueen, Type1="Poison", Nickname=Nickname,
                         Base_HP=70, Base_Atk=62, Base_Def=67, Base_SpAtk=55, Base_SpDef=55, Base_Spd=56,
                         Base_Exp_Given=128)


class Nidoqueen(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidoqueen", Next_Evolution=None, Type1="Poison", Type2="Ground", Nickname=Nickname,
                         Base_HP=90, Base_Atk=92, Base_Def=87, Base_SpAtk=75, Base_SpDef=85, Base_Spd=76,
                         Base_Exp_Given=227)


class Nidoranm(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidoran (male)", Next_Evolution=Nidorino, Type1="Poison", Nickname=Nickname,
                         Base_HP=46, Base_Atk=57, Base_Def=40, Base_SpAtk=40, Base_SpDef=40, Base_Spd=50,
                         Base_Exp_Given=55)


class Nidorino(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidorino", Next_Evolution=Nidoking, Type1="Poison", Nickname=Nickname,
                         Base_HP=61, Base_Atk=72, Base_Def=57, Base_SpAtk=55, Base_SpDef=55, Base_Spd=65,
                         Base_Exp_Given=128)


class Nidoking(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Nidoking", Next_Evolution=None, Type1="Poison", Type2="Ground", Nickname=Nickname,
                         Base_HP=81, Base_Atk=102, Base_Def=77, Base_SpAtk=85, Base_SpDef=75, Base_Spd=85,
                         Base_Exp_Given=227)


class Clefairy(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Clefairy", Next_Evolution=Clefable, Type1="Fairy", Nickname=Nickname,
                         Base_HP=70, Base_Atk=45, Base_Def=48, Base_SpAtk=60, Base_SpDef=65, Base_Spd=35,
                         Base_Exp_Given=113)


class Clefable(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Clefable", Next_Evolution=None, Type1="Fairy", Nickname=Nickname,
                         Base_HP=95, Base_Atk=70, Base_Def=73, Base_SpAtk=95, Base_SpDef=90, Base_Spd=60,
                         Base_Exp_Given=217)


class Vuplix(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Vulpix", Next_Evolution=Ninetails, Type1="Fire", Nickname=Nickname,
                         Base_HP=38, Base_Atk=41, Base_Def=40, Base_SpAtk=50, Base_SpDef=65, Base_Spd=65,
                         Base_Exp_Given=60)


class Ninetails(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Ninetails", Next_Evolution=None, Type1="Fire", Nickname=Nickname,
                         Base_HP=73, Base_Atk=76, Base_Def=75, Base_SpAtk=81, Base_SpDef=100, Base_Spd=100,
                         Base_Exp_Given=177)


class Jigglypuff(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Jigglypuff", Next_Evolution=Wigglytuff, Type1="Normal", Type2="Fairy", Nickname=Nickname,
                         Base_HP=115, Base_Atk=45, Base_Def=20, Base_SpAtk=45, Base_SpDef=25, Base_Spd=20,
                         Base_Exp_Given=95)


class Wigglytuff(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Wigglytuff", Next_Evolution=None, Type1="Normal", Type2="Fairy", Nickname=Nickname,
                         Base_HP=140, Base_Atk=70, Base_Def=45, Base_SpAtk=85, Base_SpDef=50, Base_Spd=45,
                         Base_Exp_Given=196)

class Magikarp(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Magikarp", Next_Evolution=Gyarados(), Type1="Water", Nickname=Nickname,
                         Base_HP=20, Base_Atk=10, Base_Def=55, Base_SpAtk=15, Base_SpDef=20, Base_Spd=80,
                         Base_Exp_Given=40)


class Gyarados(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Gyarados", Next_Evolution=None, Type1="Water", Type2="Flying", Nickname=Nickname,
                         Base_HP=95, Base_Atk=125, Base_Def=79, Base_SpAtk=60, Base_SpDef=100, Base_Spd=81,
                         Base_Exp_Given=189)


########################################################################################################################
# Testing Requirements
class Testemon(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Testemon", Base_HP=250, Base_Atk=10, Base_Def=10, Base_SpAtk=10, Base_SpDef=10, Base_Spd=5, Next_Evolution=Testemon2(),
                         Base_Exp_Given=25, Type1="Normal", Nickname=Nickname)
class Testemon2(MC.Pokemon):
    def __init__(self, Nickname=None):
        super().__init__(Name="Testemon Two", Base_HP=25000, Base_Atk=10000, Base_Def=10000, Base_SpAtk=1000, Base_SpDef=10000, Base_Spd=5000, Next_Evolution=None,
                         Base_Exp_Given=25000, Type1="Normal", Nickname=Nickname)
########################################################################################################################
# Pokemon-altering functions

def exp_gain_function(pokemon: MC.Pokemon, exp_gain):
    next_level = pokemon.get_level() + 1
    total_exp = pokemon.get_total_exp()
    new_exp = total_exp + exp_gain
    exp_threshold = pow(next_level, 3)
    if new_exp > exp_threshold:
        pokemon.level_up()
        pokemon.set_current_exp(new_exp - exp_threshold)
        pokemon.gain_exp_t(exp_gain)
        print(f"Congratulations! {pokemon.get_name()} levelled up!")
    else:
        pokemon.both_gain_exp(exp_gain)


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

########################################################################################################################
# Pokedex dictionary and functions


pokedex_dict = {1: Bulbasaur, 2: Ivysaur, 3: Venusaur, 4: Charmander, 5: Charmeleon, 6: Charizard,
                7: Squirtle, 8: Wartortle, 9: Blastoise, 10: Caterpie, 11: Metapod, 12: Butterfree,
                13: Weedle, 14: Kakuna, 15: Beedrill, 16: Pidgey, 17: Pidgeotto, 18: Pidgeot, 19: Rattata,
                20: Raticate, 21: Spearow, 22: Fearow, 23: Ekans, 24: Arbok, 25: Pikachu, 26: Raichu,
                27: Sandshrew, 28: Sandslash, 29: Nidoranf, 30: Nidorina, 31: Nidoqueen, 32: Nidoranm,
                33: Nidorino, 34: Nidoking, 35: Clefairy, 36: Clefable, 37: Vuplix, 38: Ninetails, 39: Jigglypuff,
                40: Wigglytuff, 129: Magikarp, 130: Gyarados}


def print_full_dex():
    numbers = list(pokedex_dict.keys())
    mons = list(pokedex_dict.values())
    for i in range(len(pokedex_dict)):
        print(f"Pokedex No. {numbers[i]}: {mons[i]().get_mon_name()}")
