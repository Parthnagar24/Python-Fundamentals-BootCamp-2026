numbers = [10, 15, 22, 35, 40, 51, 60, 75, 82]
count = 0

for i in numbers:
    if i%2 == 0 and i >20 and i <80:
        count +=1

print(count)