import BattleState as BS
import Pokedex as P
import Move_Glossary as MG


karp = P.Magikarp()

char = P.Charmander("Gary")
char.learn_new_move(MG.drag_claw)
char.learn_new_move(MG.fthrower)
char.learn_new_move(MG.equake)
char.learn_new_move(MG.b_slam)

char.set_nickname("Larry")

pika = P.Pikachu("Ash's Pikachu")
pika.learn_new_move(MG.tbolt)
pika.learn_new_move(MG.b_slam)
pika.learn_new_move(MG.tackle)
pika.learn_new_move(MG.surf)

BS.BattleRound(char, pika)

