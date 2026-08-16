def binary_search_even(numbers,target):

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

numbers = [10,20,30,40,50,60] 
result =binary_search_even(numbers,50)
print(result)