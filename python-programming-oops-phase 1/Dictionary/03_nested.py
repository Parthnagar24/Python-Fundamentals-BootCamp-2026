employees = {
    "emp101": {
        "name": "Parth",
        "role": "Data Analyst",
        "salary": 45000
    },
    "emp102": {
        "name": "Rahul",
        "role": "Developer",
        "salary": 50000
    }
}

print(employees["emp101"]["name"])

employees["emp101"]["salary"] = 48000
print(employees)

employees["emp101"]["city"] = "Kolkata"
print(employees)