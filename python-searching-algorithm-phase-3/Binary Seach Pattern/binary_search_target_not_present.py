def binary_search(numbers,target):
    low = 0
    high = len(numbers) -1

    while low <=high:
        middle = (low +high) //2

        if numbers[middle] ==target:
            return middle
        elif numbers[middle] > target:
            high = middle -1
        else:
            low = middle + 1

    return -1

numbers = [5, 10, 15, 20, 25, 30, 35, 40] 
result =binary_search(numbers,29)
print(result)