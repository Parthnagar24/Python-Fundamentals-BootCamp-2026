data = ["Python", "SQL", "Excel", "Power BI", "Tableau"]

print(data[1])
print(data[4])

#["Python", "SQL"] ?
print(data[:2])
#["Power BI", "Tableau"] ?
print(data[3:])

data.reverse()
print(data)

skills = ["Python", "SQL", "Excel"]
skills.append("PowerBi")
skills.insert(1,"Tablue")
skills.remove("SQL")
skills[2]= "pandas"
print(skills)

numbers = [10, 20, 30, 20, 40, 20]
a = numbers.index(20) # a = 1
b = numbers.count(20) # b = 3

numbers.remove(20) 

c = numbers.count(20)  # c =2

x = numbers.pop(2) #20
print(a,b,c,x,numbers)


cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
cart.remove("Keyboard")
cart.append("headphpmes")
print(cart[-1])
#Wants to know how many products remain.

print(len(cart))
students = [
    ["Parth", 85],
    ["Rahul", 92],
    ["Amit", 78]
]

print(students[0])
print(students[0][0])
print(students[1][1])
print(students[2])

