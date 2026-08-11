marks = {
      "student1" : 100,
      "student2" : 45,
      "student3" : 21
    }

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"student1":99},"")
print(marks)

print(marks.get("Haary"))
print(marks.get("student1"))  

marks.pop("student1")
print(marks)