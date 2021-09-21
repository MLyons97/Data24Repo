import Main_Class as classes


class Pikachu(classes.Pokemon):
    def __init__(self):
        super().__init__(Name="Pikachu", HP=211, Attack=131, Defence=117, Type1="Electric")


class Charizard(classes.Pokemon):
    def __init__(self):
        super().__init__(Name="Charizard", HP=360, Attack=293, Defence=280, Type1="Fire", Type2="Flying")


class Magikarp(classes.Pokemon):
    def __init__(self):
        super().__init__(Name="Magikarp", HP=244, Attack=130, Defence=229, Type1="Fire")