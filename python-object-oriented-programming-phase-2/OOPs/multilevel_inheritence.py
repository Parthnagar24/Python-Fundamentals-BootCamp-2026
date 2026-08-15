class Animal:

    def eat(self):
        print("Eating")


class Pet:

    def play(self):
        print("Playing")


class Dog(Animal, Pet):

    def bark(self):
        print("Barking")


dog = Dog()

dog.eat()     # Animal
dog.play()    # Pet
dog.bark()    # Dog