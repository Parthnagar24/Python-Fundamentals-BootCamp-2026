employee = {
    "name": "Parth",
    "age": 22,
    "role": "Data Analyst",
    "salary": 40000
}

print(employee["name"])
print(employee["role"])
print(employee["salary"])

employee.update({
    "salary" : 4500,
    "location": "kolkata",
    "role": "business analyst"

})

print(employee)



employee2 = {
    "name": "Parth",
    "age": 22
}

a = employee2.get("name")
b = employee2.get("salary")
c = employee2.get("salary", 0)

print(a) # parth
print(b) # none
print(c) # 0

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000
}
print(product.keys()) # dict_keys(['id', 'name', 'price'])
print(product.values()) # dict_values([101, 'Laptop', 55000])
print(product.items()) # dict_items([('id', 101), ('name', 'Laptop'), ('price', 55000)])



student = {
    "name": "Parth",
    "age": 22,
    "cgpa": 7.5
}

student["cgpa"] = 7.83
student["city"] = "Kolkata"

x = student.pop("age")

print(student)
print(x) #{'name': 'Parth', 'cgpa': 7.83, 'city': 'Kolkata'} 22

student = {
    "name": "Parth",
    "age": 22
}
print("name" in student) # true
print("Parth" in student) # false as this checks for keys
print("Parth" in student.values()) # true





data = {
    "Python": 90,
    "SQL": 85,
    "Power BI": 80,
    "Excel": 75
}
a = data.get("SQL")
data.update({
    "SQL": 95,
    "Tableau": 70
})
b = data.pop("Excel") # {'Python': 90, 'SQL': 95, 'Power BI': 80, 'Tableau': 70}
print(data)   # 
print(a) #85
print(b) # 75