numbers = [1, 2, 2, 3, 4, 3, 5, 1, 6]
num = []

for i in numbers:
    if numbers.count(i) >1 and i not in num:
        num.append(i)
        print(num)
print(num)