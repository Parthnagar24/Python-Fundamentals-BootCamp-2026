def linear_search_last(numbers, target):

    index = -1

    for i in range(len(numbers)):

        if numbers[i] == target:
            index = i

    return index


numbers = [12, 7, 25, 20, 25, 30, 25]

result = linear_search_last(numbers, 25)

print(result)