skills = ["Python", "SQL", "Power BI"]
print(skills)
print(skills[0])
print(skills[-1])

skills[0] = 3.2
print(skills)


student = ["Parth", 22, "CSE", 7.83]

#What is the index of "CSE"
print(student.index("CSE"))
#How would you access 7.83
print(student[3])

#How would you change "CSE" to "Computer Science"
student[2] = "Computer Science"
print(student)

#How would you get the first two elements using slicing

print(student[0:2])

#How would you get the list in reverse using slicing?

print(student[::-1])

# append

skills = ["Python", "SQL"]

skills.append("Excel")

print(skills)

# join both the list

a = ["A","b"]
print(a)
b = [1,2,3,4]
a.extend(b)
print(a)

a.insert(3,"b")
print(a)


# remove b

a.remove("b")
print(a)

print(a.pop())
print(a.pop(0))

print(a.count('b'))