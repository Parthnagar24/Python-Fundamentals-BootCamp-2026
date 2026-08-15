def count_digit(n):
    store_count = 0

    while (n > 0):
        digit = n % 10  # get the last digit from number
        store_count += 1 
        n = n // 10   # remove the last digit
        print(store_count)
    return store_count
    
result = count_digit (n = 583242)
print(result)