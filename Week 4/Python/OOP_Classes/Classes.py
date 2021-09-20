class Dog:                              # Classes should start with capitals
    animal_kind = "Canine"              # Class variable

    def bark(self):                     # Class Method - the self means it is referring to its own class
        return "Woof"                   # "animal_kind" is defined within the class and needs to be called as such


print(Dog.animal_kind)
print(Dog().bark())                     # Parenthesis are needed for this as bark isn't static - we need a dog to bark

fido = Dog()                            # fido & lassie are both dogs, but are two separate objects
lassie = Dog()                          # Making a dog is instantiating a dog

# So changing fido won't change lassie - IE
fido.animal_kind = "Big Dog"

print(fido.animal_kind)
print(lassie.animal_kind)