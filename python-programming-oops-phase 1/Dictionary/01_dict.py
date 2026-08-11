employee = {
    "name": "Rahul",
    "age": 25,
    "salary": 45000
}
print(employee)
print(employee["name"]) # access value based on key


employee = {
    "name": "Rahul",
    "age": 25
}

print(employee.get("name"))
print(employee.get("salary"))