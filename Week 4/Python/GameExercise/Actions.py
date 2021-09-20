import random

import Master_Class as MC
import People as P


def enemy_select(bad_guys: list):
    return bad_guys[random.randint(0, len(bad_guys))-1]


def damage_calc(player: MC.Person):
    weapon = player
    return player.get_damage()
#     return player.get_damage()*player.get_weapon().get_damage()


def ranged_damage_calc(player: MC.Person):
    return player.get_damage()


def loot(list_of_loots: list) -> object:
    length = len(list_of_loots)
    return list_of_loots[random.randint(0, length)]


def check_death(person: MC.Person):
    pass


def battle_won(player: P.GoodGuy, enemy: P.BadGuy):
    print(f"You've knocked them out, well done!\n\n\n")
    enemy.kill_off()
    P.enemy_list.remove(enemy)
    P.dead_list.append(enemy)

    if enemy.get_balance() > 0:
        print(f"They had {enemy.get_balance()} coins on them, you may as well have them...")
        player.change_balance(enemy.get_balance())
        print(f"You've now got {player.get_balance()} coins!\n")

    if len(enemy.get_inventory()) > 0:
        option = input("It looks like they dropped something else, want to pick it up?"
                       "(1 for yes, 2 for no):\n--> ")
        if option == 1:
            found_loot = loot(enemy.get_inventory())
            print(f"You found a {found_loot}!\n")
            player.add_to_inventory(found_loot)

        else:
            print("Alright then, keep your secrets\n")


def battle_state(player: P.GoodGuy, enemy: P.BadGuy, player_pet: MC.Animal = None, enemy_pet: MC.Animal = None):

    print(f"\nYou've ran into the evil {enemy.get_name()}! And they don't look happy at all...")
    print(f"They have {enemy.get_health()} health and can do {enemy.get_damage()} damage with their {enemy.get_weapon()}"
          f"\nWhat do you want to do?\n")
    escape = False

    while enemy.get_health() > 0 and not escape:

        if player_pet is not None:
            print(f"Your pet, {player_pet.get_name()}, came to help you!")
            animal_attack_person(player_pet, enemy)

            if enemy.get_health() <= 0:
                battle_won(player, enemy)

        if enemy_pet is not None:
            print(f"{enemy.get_name()}'s pet, {enemy_pet.get_name()} has attacked you!")
            animal_attack_person(enemy_pet, player)

        option = int(input(f"1. Hit them!\n2. Shoot at them with your ranged "
                           f"weapon!\n3. Use an item\n4. Try running (you coward...)\n"))

        if option == 1:
            damage = damage_calc(player)
            print(f"You've attacked for {damage} damage!")
            enemy.take_damage(damage)

            if enemy.get_health() <= 0:

                battle_won(player, enemy)

            else:
                print(f"Big hit! {enemy.get_name()} has {enemy.get_health()} health left!")

                if random.random() < 0.9:
                    print("They didn't like that, and hit you back!")
                    damage = damage_calc(enemy)
                    player.take_damage(damage)

                    if player.get_health() > 0:
                        print(f"Ouch! They did {damage} to you, leaving you with {player.get_health()} points left")
                    else:
                        print(f"Oh no! {enemy.get_name()} has hit you for {damage} damage!")
                else:
                    print(f"Lucky! They missed you! You still have {player.get_health()} health left.\n")

        elif option == 2:

            if len(player.get_ranged_weapon()) == 0:
                print("You don't have a ranged weapon you fool! Visit the blacksmith next time you're in town")

            else:
                if random.random() < 0.7:                                                                                ## Accuracy check on weapon goes in here
                    damage = ranged_damage_calc(player)
                    enemy.take_damage(damage)
                    print(f"Bullseye! You hit them for {damage} damage! They have {enemy.get_health()} left!")
                else:
                    print(f"You missed! Keeping your distance means {enemy.get_name()} couldn't get in to hit you!")

                if len(enemy.get_ranged_weapon()) != 0:
                    print(f"{enemy.get_name()} has a {enemy.get_ranged_weapon()}...")

                    if random.random() < 0.7:                                                                            ## Also need an accuracy check here
                        damage = ranged_damage_calc(enemy)
                        player.take_damage(damage)
                        print(f"Sharpshooter! They hit you for {damage} points!")

                        if player.get_health() > 0:
                            print(f"Ouch! They did {damage} to you, leaving you with {player.get_health()} points left")
                        else:
                            print(f"Oh no! {enemy.get_name()} has hit you for {damage} damage!")
        elif option == 3:
            print("I can't lie I've not programmed items into the battle yet, please try something else\n")

        elif option == 4:
            chance_of_escape = random.randint(0, 75)
            print(f"It's a bold move, you've got a {chance_of_escape}% chance of it working...\n")

            if random.random()*100 < chance_of_escape:
                print(f"Hey it worked, you got away safely!\nBut the enemy will recover and be back...")
                break

            else:
                print("They caught you! No getting away that easily")

                if random.random() < 0.9:
                    print("and they weren't a fan of it at all and hit your even harder for it!\n")
                    damage = int(damage_calc(enemy)*1.2)
                    player.take_damage(damage)

                    if player.get_health() > 0:
                        print(f"Ouch! They did {damage} to you, leaving you with {player.get_health()} points left")
                    else:
                        print(f"Oh no! {enemy.get_name()} has hit you for {damage} damage!")

                else:
                    print("Lucky you! You dodged their swing!")

        if player.get_health() <= 0:
            player.set_health(0)
            player.kill_off()
            print(f"That means {enemy.get_name()} has killed you! If only we could program a save function...")
            break


def animal_attack_person(this_animal: MC.Animal, this_person: MC.Person):
    if this_animal.get_good() != this_person.is_good():
        print(f"{this_animal.get_name()} has attacked {this_person.get_name()}!")
        damage = this_animal.get_damage()
        print(f"They did {this_animal.get_damage()} points of damage!")
        this_person.take_damage(damage)
    else:
        print(f"{this_animal.get_name()} and {this_person.get_name()} are on the same side! "
              f"They would never harm each other")


def animal_attack_animal(animal1: MC.Animal, animal2: MC.Animal):
    print(f"{animal1.get_name()} has attacked {animal2.get_name()}!\n")
    damage = animal1.get_damage()
    print(f"They did {damage} points of damage")


def heal_check(this_player: P.GoodGuy, doc: P.Doctor):
    if this_player.get_health()/this_player.get_max_health() < 0.5:
        tester = input(f"You're at {this_player.get_health()*100/this_player.get_max_health()}% health, and doctor"
                       f" {doc.get_name()} is here, do you want to heal up? Y/N")
        if tester == "Y":
            this_player.heal(doc.get_heal_power())


# def check_for_dead(list_of_people: list):
#     to_be_removed = []
#     for i in range(len(list_of_people)):
#         print(f"{list_of_people[i].get_name()}, {list_of_people[i].get_is_alive()}")
#         if not list_of_people[i].get_is_alive():
#             print(f"{list_of_people[i].get_name()} is ded")
#             to_be_removed.append(i)
