class Employee:
    language = "Python" # This is a class attribute
    salary = 11312442   # This is a class attribute

Alex = Employee()
Alex.language = "JavaScript" # This is an instance attribute
print(Alex.language,Alex.salary)

# preference : instance attri > class attri  during assignment and retrieval
