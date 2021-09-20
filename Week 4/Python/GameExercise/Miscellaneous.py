from Items import *


class Note(Miscellaneous):

    def __init__(self, cost: int, category: str, name: str, information: str):
        super().__init__(cost,category,name)
        self.information = information

    def read_note(self):
        return self.name + ' says ' + self.information


class Key(Miscellaneous):

    def __init__(self, cost: int, category: str, name: str, lock: str):
        super().__init__(cost,category,name)
        self.lock = lock
        self.get_info()

    def get_info(self):
        return self.name + ' is used for ' + self.lock
