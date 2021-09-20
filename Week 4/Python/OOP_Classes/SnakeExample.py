from ReptileExample import *

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.heart_chambers = [2,4]
        self.venom = None
        self.announce()


    def announce(self):
        print("BEHOLD! A Snake has arrived")

    def surprise_attack(self):
        print("Gotcha")

Frank = Snake()

Frank.surprise_attack()                     # From Snake
Frank.seek_heat()                           # From reptile
Frank.breathe()                             # From animal
