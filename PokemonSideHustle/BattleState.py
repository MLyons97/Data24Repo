import Main_Class as MC
import Move_Glossary as MG
import Actions as A
import Calculations as C
import random as r


def PlayerTurn(player_pokemon: MC.Pokemon, enemy_pokemon: MC.Pokemon) -> bool:      # Returns True for knocked out
    moveset = player_pokemon.get_moves()                                            # opponent, False for not knocked
    if len(moveset) == 0:                                                           # out
        player_pokemon.learn_new_move(MG.struggle)
        moveset = player_pokemon.get_moves()

    decider = int(input(f"\nWhat will {player_pokemon.get_name()} do?"
                    f"\n1. Fight"
                    f"\n2. Bag"
                    f"\n3. Pokemon"
                    f"\n4. Run"
                    f"\n--> "))

    if decider == 1:
        print(f"\n{player_pokemon.get_name()} knows:")
        for i in moveset:
            print(f"{moveset.index(i) + 1}: {i.get_name()}")
        moveselect = int(input(f"Which move should {player_pokemon.get_name()} use?\n"))
        A.attack(player_pokemon, enemy_pokemon, moveset[moveselect - 1])
        if C.faint_check(enemy_pokemon):
            print(f"{enemy_pokemon.get_name()} has fainted!")
            return False
        else:
            print(f"{enemy_pokemon.get_name()} has {enemy_pokemon.get_hp()} HP left!")
            return True
    elif decider == 2:
        print("Bag goes here")
        return True
    elif decider == 3:
        print("Pokemon goes here")
        return True
    elif decider == 4:
        print("Attempting to run...")
        attempts = 1
        escape_odds = int(((((player_pokemon.get_speed()*128) / enemy_pokemon.get_speed()) + 30 ) * attempts) % 256)
        randval = r.randint(0, 255)
        if randval < escape_odds:
            print("Got away safetly!")
            return False
        else:
            print("Couldn't get away!")
            return True


def EnemyTurn(player_pokemon: MC.Pokemon, enemy_pokemon: MC.Pokemon):
    moveset = enemy_pokemon.get_moves()
    if len(moveset) == 0:
        enemy_pokemon.learn_new_move(MG.struggle)
        moveset = enemy_pokemon.get_moves()

    # Some AI might go in here eventually but for the time being...
    print(f"\nThe enemy {enemy_pokemon.get_name()} used a random move!")
    A.attack(enemy_pokemon, player_pokemon, moveset[r.randint(0, len(moveset)-1)])

    if C.faint_check(player_pokemon):
        print(f"{player_pokemon.get_name()} has fainted!")
        return False
    else:
        print(f"{player_pokemon.get_name()} has {player_pokemon.get_hp()} HP left!")
        return True


def BattleRound(player_pokemon: MC.Pokemon, enemy_pokemon: MC.Pokemon):
    battle_state = True
    turn_count = 0

    while battle_state:
        turn_count += 1
        print(f"\nIt is turn {turn_count}.")
        if player_pokemon.get_speed() > enemy_pokemon.get_speed():
            battle_state = PlayerTurn(player_pokemon, enemy_pokemon)
            if not battle_state: break
            battle_state = EnemyTurn(player_pokemon, enemy_pokemon)
        elif player_pokemon.get_speed() < enemy_pokemon.get_speed():
            battle_state = EnemyTurn(player_pokemon, enemy_pokemon)
            if not battle_state: break
            battle_state = PlayerTurn(player_pokemon, enemy_pokemon)
        elif r.random() > 0.5:
            battle_state = PlayerTurn(player_pokemon, enemy_pokemon)
            if not battle_state: break
            battle_state = EnemyTurn(player_pokemon, enemy_pokemon)
        else:
            battle_state = EnemyTurn(player_pokemon, enemy_pokemon)
            if not battle_state: break
            battle_state = PlayerTurn(player_pokemon, enemy_pokemon)