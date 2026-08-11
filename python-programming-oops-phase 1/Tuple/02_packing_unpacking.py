data = "Python", "SQL", "Excel"
print(data)
print(type(data))

data2 = ("Python", "SQL", "Excel")

a, b, c = data2
print(a)
print(b)
print(c)
print(data2)


student = ("Parth", 22, 7.83)
name, age, cgpa = student
print(name) #"Parth"
print(age) # 22
print(cgpa) # 7.83

student = ("Parth", 22, 7.83)
#name, age = student # throws errow because we have 3 values but we should 2 variables variable no. = value no.


students = (
    ("Parth", 85),
    ("Rahul", 92),
    ("Amit", 78)
)

print(students[0][0])
print(students[0][1])
print(students[1][1])
print(students[2][0])


skills = ("Python", "SQL", "Excel")
l = list(skills)
print(l)
l.append("PowerBi")
print(l)
skills = tuple(l)
print(skills)



employee = ("Parth", "Data Analyst", 7.83)
name,role,cgpa = employee
new_employee = name, role
print(new_employee)

data = (10, 20, 30, 20, 40)
a = data.count(20)
b = data.index(40)
x, *y, z = data
print(a) # 2
print(b) # 4
print(x) # 10
print(y) # 20 30 20
print(z) # 40