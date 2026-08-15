numbers = [10, 25, 30, 15, 40, 5, 8]
smallest_odd_number = None

for i in numbers:
    if i%2 !=0:
        if smallest_odd_number is None or i < smallest_odd_number:
            smallest_odd_number = i
            print(smallest_odd_number)
print(f"The smallest odd number : {smallest_odd_number}")
