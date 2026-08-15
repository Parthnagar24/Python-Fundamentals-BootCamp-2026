class Employee:
    language = "Python" # This is a class attribute
    salary = 11312442   # This is a class attribute

Alex = Employee()
Alex.name = "Alex" 
Alex.gender = 'Male'   # This is an instance/object attribute
print(Alex.name,Alex.language,Alex.gender)

Alexa = Employee()
Alexa.name = "Alexa"
Alexa.gender = 'Female'   # This is an instance/object attribute
print(Alexa.name,Alexa.language,Alexa.gender)