tuple1 = "Python","SQL","PowerBI","Excel"

print(tuple1[0])
print(tuple1[-1])
print(tuple1[0:2])
print(tuple1[::-1])


x = (10)
y = (10,)

print(type(x))   # predict  -> int
print(type(y))   # predict -> tuple

data = ("Python", "SQL", "Python", "Excel", "Python")
print(data.count("Python")) # 3
print(data.index("Python"))  # 0
print(data.index("Excel"))  # 3

"""
data = ("Python", "SQL", "Excel")

data[1] = "Power BI"    error occurs because we are trying to modify an immutable tuple"""

location = ("Kolkata", "West Bengal", "India") # ?
location = ("Delhi",) + location[1:]
print(location)


a = (10, 20, 30, 20)
b = a.count(20)  
c = a.index(30)
a = a + (40, 50)
print(a)  # 10 20 30 20 40 50 
print(b)  # 2
print(c) # 2