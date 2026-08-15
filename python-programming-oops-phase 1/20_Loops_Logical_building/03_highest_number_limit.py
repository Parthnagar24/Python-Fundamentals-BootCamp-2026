numbers = [45, 82, 67, 91, 74, 88]
highest_number = None

for i in numbers:
    if i < 90:
        if  highest_number  is None or i > highest_number :
            highest_number = i
            print(highest_number)
print(f"The highest number below 91 limit is : {highest_number}")