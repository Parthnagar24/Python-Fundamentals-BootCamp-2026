def binary_search_first(numbers, target):

    low = 0
    high = len(numbers) - 1
    answer = -1

    while low <= high:

        middle = (low + high) // 2

        if numbers[middle] == target:
            answer = middle
            high = middle - 1

        elif numbers[middle] > target:
            high = middle - 1

        else:
            low = middle + 1

    return answer


numbers = [10, 20, 30, 30, 30, 40, 50]

result = binary_search_first(numbers, 30)

print(result)