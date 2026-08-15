class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print("Eating")


class Pet:

    def play(self):
        print("Playing")


class Dog(Animal, Pet):

    def bark(self):
        print("Barking")


dog = Dog("A")

dog.eat()     # Animal
dog.play()    # Pet
dog.bark()    # Dog