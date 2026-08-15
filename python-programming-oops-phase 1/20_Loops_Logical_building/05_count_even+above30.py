numbers = [12, 25, 36, 41, 48, 55, 60, 73]
count = 0

for i in numbers:
    if i % 2 == 0 and i > 30:
        count +=1
        print(count)
print(f"The count of numbers does are even and are above 30 : {count}")