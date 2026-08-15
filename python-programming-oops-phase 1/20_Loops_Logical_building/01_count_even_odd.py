numbers = [12, 7, 20, 15, 30, 9, 40, 11,7]
even_count ,odd_count = 0,0
for i  in numbers:
    if i % 2 ==0:
        even_count += 1  
        print(even_count)
    else:
        odd_count += 1
        print(odd_count)

print(f"The total even count: {even_count}")
print(f"The total odd count :{odd_count}")