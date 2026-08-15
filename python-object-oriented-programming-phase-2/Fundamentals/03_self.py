class Employee:
    language = "Python" # This is a class attribute
    salary = 11312442   # This is a class attribute

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

Alex = Employee()
Alex.language = "JavaScript" # This is an instance attribute
Alex.getinfo()
#Employee.getinfo(Alex)