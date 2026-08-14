'''
a = 12
b = 45
c = 56
average = (a+b+c)/3
print(average)
'''

#function definition
def avg():
    a =int(input("Enter a number:"))
    b =int(input("Enter a number:"))
    c =int(input("Enter a number:"))

    average = (a+b+c)/3
    print(average)

avg() # function call
avg()
avg()
avg()


# greet user with gooday
def greet():
    user = input("Enter username:").strip().title()
    print(f"Good Day!,{user}")

greet()


# function with arguments

def greet(name,ending):         # name -> parameter -> passed Harry as name 
    print(f"Good Day!,{name},{ending}")

greet("Harry","ThankYou")  # Harry -argument




# function with arguments

def greet(name,ending):         
    print(f"Good Day!,{name},{ending}")
    return "ok"

a = greet("Harry","ThankYou")
print(a)

# function with default parament argument

def gooday(name,ending="ThankYou"):
    print(f"good day, {name},{ending}")

gooday("Alex")
