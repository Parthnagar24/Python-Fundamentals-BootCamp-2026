#Get all values inside a list using for loop
skills = ["Python", "SQL", "Power BI"]

for skill in skills:
    print(skill)

# Get each character in a string

name = "Parth"

for char in name:
    print(char)

# use of range built in function


for i in range(5):
    print(i)

# Get range of numbers but must be even
for i in range(2, 10, 2):
    print(i)

# Get range of number but must be odd
for i in range(1, 10, 2):
    print(i)

# reverse range
for i in range(5,0,-1):
    print(i)

# loop through a list

marks = [85, 92, 78, 90]

for mark in marks:
    print(mark)

# loop through tuple

data = ("Python", "SQL", "Excel")

for item in data:
    print(item)

# loop through dictionary

student = {
    "name": "Parth",
    "age": 22,
    "cgpa": 7.83
}

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)


numbers = [10, 20, 30]

for x in numbers:
    print(x * 2)

# sum of list values

numbers = [10, 20, 30, 40]
num =0
sum = 0
for num in numbers :
    sum += num
    num+=1
print(sum)

#count values in list
numbers = [10, 25, 30, 45, 50]
num=0
count = 0
for num in numbers:
    count+=1
    num+=1
print(count)

# count even numbers

number2 = [10, 15, 22, 31, 40, 55]
nums = 0
counted = 0
for nums in number2:
    if nums % 2 == 0:
        counted+=1
        nums+=1
print(counted)

# largest number

n = [15, 42, 8, 73, 29]
for i in n:
   pass


sales = [12000, 50000, 18000, 75000, 30000]
sum =0
s = 0
for s in sales:
    sum += s
    s+=1
print(sum)


marks = [85, 62, 91, 45, 78, 55]
counter = 0
for mark in marks:
    if mark >=70:
        counter += mark
        mark +=1
        print(counter)

name = "Parth Nagar"
count =0
for o in name:
    if (name.find(" ")):
        print(o)
