data = ["Python", "SQL", "Python", "Excel", "Python", "SQL"]

a = data.index("Python")
b = data.count("SQL")

data.remove("Python")

c = data.index("Python")

x = data.pop(2)

print(data)
print(a)
print(b)
print(c)
print(x)



skills = ["Python", "SQL", "Excel"]

print("Python" in skills)
print("Java" not in skills)