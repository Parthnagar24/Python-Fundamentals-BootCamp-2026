a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)

d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()



d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)


d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)