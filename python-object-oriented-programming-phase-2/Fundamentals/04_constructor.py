class Employee:
    language = "Python"
    salary = 10

    def __init__(self):  # dunder methods which is automatically called
        print("I am creating an object")

    def getinfo(self):
        print(f"{self.language},{self.salary}")

    @staticmethod
    def greet():
        print("Guten Morgan")

harry = Employee()
harry.name ="Harry"
print(harry.name,harry.salary)