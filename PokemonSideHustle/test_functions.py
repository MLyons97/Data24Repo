import Main_Class as MC
import Move_Glossary as MG
import Calculations as C
import Actions as A
import Pokedex as P

test = P.Testemon("Greg")
testevo = P.Testemon2()

test.take_damage(250)
print(test.get_hp())


def test_feint_check():
    assert C.faint_check(test)


def test_accuracy_mechanic():
    assert not A.attack(test, testevo, MG.missing)


def test_naming_conservation():
    assert test.get_name() == P.evolution(test).get_name()