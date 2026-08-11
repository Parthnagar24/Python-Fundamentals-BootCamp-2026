day = input("Enter the today's date:").strip().title()
print(day)

if day == "Sunday":
    print(f"Order from outside as today is: {day}")
else:
    print(f"Eat at home as today is : {day}")


age = int(input("Enter the age:"))

if age >=18 : 
    print("adult")
elif age <=15 and age >=0: 
    print("minor")
elif age >15 and age <18:
    print("Min-dult")
else :
    print("None")