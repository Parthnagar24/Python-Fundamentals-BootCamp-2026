class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def bark(self):
        print(self.name, "says Woof")


class Cat(Animal):

    def meow(self):
        print(self.name, "says Meow")


class Cow(Animal):

    def moo(self):
        print(self.name, "says Moo")


dog = Dog("Bruno")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.eat()
dog.bark()

cat.eat()
cat.meow()

cow.eat()
cow.moo()