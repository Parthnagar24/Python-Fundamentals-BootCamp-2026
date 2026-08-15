numbers = [12, 25, 36, 41, 48, 55, 60]

last_even = None

for i in numbers:
    if i % 2 == 0:
        last_even = i

print(last_even)