# class Animal:
#     def __init__(self, NoLegsI, SizeI):
#         self.__NoLegs = NoLegsI
#         self.__Size = SizeI
#
#     def get_legs(self):
#         return self.__NoLegs
#
#     def get_type(self):
#         return self.__Type
#
#
# class Dog(Animal):
#     def __init__(self, NoLegsI, SizeI):
#         self.__NoLegs = 4
#         self.__Size = SizeI
#         self.__Type = "Dog"
#         super().__init__(NoLegsI, SizeI)
#
# class Cat(Animal):
#     def __init__(self, NoLegsI, SizeI):
#         self.__NoLegs = 4
#         self.__Size = SizeI
#         self.__Type = "Cat"
#         super(Cat, self).__init__(NoLegsI, SizeI)
#
class Dog:
    def __init__(self, Name, Breed, Owner):
        self.__name = Name
        self.__breed = Breed
        self.__owner = Owner

    def get_breed(self):
        return self.__breed

    def get_owner(self):
        return self.__owner


class Spaniel(Dog):
    def __init__(self, Name, Owner):
        self.__breed = "Spaniel"
        super().__init__(Name, Breed="Spaniel", Owner)


class Lab(Dog):
    def __init__(self, Name, Owner):
        self.__breed = "Labrador"
        super().__init__(Name, Breed="Labrador", Owner)