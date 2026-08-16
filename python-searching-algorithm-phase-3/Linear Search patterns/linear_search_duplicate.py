def linear_search_first(numbers, target):

    for i in range(len(numbers)):

        if numbers[i] == target:
            return i

    return -1


numbers = [12, 7, 20, 25, 15, 25, 30, 25]

result = linear_search_first(numbers, 25)

print(result)


