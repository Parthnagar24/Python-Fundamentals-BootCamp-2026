def binary_search_last(numbers,target):
    low = 0
    high = len(numbers) - 1
    index = -1

    while low <= high:
        middle = (low + high)  //2
        if numbers[middle] == target:
            index = middle
            low = middle + 1

        elif numbers[middle] > target :
            high = middle - 1

        else :
            low = middle + 1
    return index


numbers = [5, 10, 30, 30, 30]

result = binary_search_last(numbers, 30)

print(result)