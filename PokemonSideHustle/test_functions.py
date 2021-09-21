import Main_Class as MC
import Calculations as C
import Actions as A

testemon = MC.Pokemon("Tester", 200, 0, 0, "Normal")

testemon.take_damage(250)
print(testemon.get_hp())

def test_feint_check():
    assert C.feint_check(testemon)
