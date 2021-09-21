import Actions as acts
import Pokedex as dex
import Move_Glossary as mgloss

pika = dex.Pikachu()
char = dex.Charizard()
char2 = dex.Charizard()
karp = dex.Magikarp()

print(f"Charizard HP: {char.get_hp()}\n")
print(f"Second Charizard HP: {char2.get_hp()}")


acts.attack(char2, char, mgloss.tbolt)
acts.attack(char, char2, mgloss.drag_claw)
