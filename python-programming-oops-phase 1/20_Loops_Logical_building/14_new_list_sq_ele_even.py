numbers = [10, 15, 22, 31, 40, 55, 60]
num = []

for i in numbers:
    if i% 2 ==0:
       num.append(i**2)
       print(num)
print(num)