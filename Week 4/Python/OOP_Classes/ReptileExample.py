import AnimalExample as AE


class Reptile(AE.Animal):

    def __init__(self):
        super().__init__()                      # Need to call this super to link back to previous instance
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        print("Y'all got any of that new kendrick?")    # Hehehe get it?
