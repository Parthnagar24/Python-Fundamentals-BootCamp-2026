numbers = [10, 25, 30, 15, 40, 5]
total = 0

for i in numbers:
    if i % 2 ==0:
        total +=i   
        print(total)
print(f"The sum of even numbers: {total}")