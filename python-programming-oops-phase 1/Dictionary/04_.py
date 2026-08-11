employee = {
    "name": "Parth",
    "role": "Data Analyst",
    "skills": ["Python", "SQL", "Power BI"]
}

print(employee["name"])
print(employee["role"])
print(employee["skills"])
print(employee["skills"][1])
print(employee["skills"][2])

employees = {
    "emp101": {
        "name": "Parth",
        "salary": 45000
    },
    "emp102": {
        "name": "Rahul",
        "salary": 50000
    }
}
print(employees["emp101"]["salary"])
print(employees["emp102"]["name"])



employee = {
    "name": "Parth",
    "skills": ["Python", "SQL", "Excel"]
}

x = employee["skills"][1] # sql

employee["skills"].append("Power BI") # python sql exel powerbi

print(x)
print(employee)





employees = [
    {"name": "Parth", "salary": 45000},
    {"name": "Rahul", "salary": 50000},
    {"name": "Amit", "salary": 40000}
]
print(employees[0]["salary"])
print(employees[1]["name"])
print(employees[2]["salary"])


product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "categories": ["Electronics", "Computers"],
    "seller": {
        "name": "ABC Store",
        "city": "Kolkata"
    }
}
print(product["name"])
print(product["categories"][0])
print(product["categories"][1])
print(product["seller"]["name"])
print(product["seller"]["city"])


data = {
    "employee": {
        "name": "Parth",
        "skills": ["Python", "SQL"],
        "salary": 45000
    }
}

a = data["employee"]["name"] #parth
b = data["employee"]["skills"][0] # python

data["employee"]["skills"].append("Power BI") # adds powerbi in list at the end inside dict
data["employee"]["salary"] = 50000 # modify salary from 45000 to 50000

print(a)
print(b)
print(data)