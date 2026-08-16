def selection_sort(numbers):

    n = len(numbers)

    for i in range(n):

        # Assume current position has the smallest value
        min_index = i

        # Search for a smaller value
        for j in range(i + 1, n):

            if numbers[j] < numbers[min_index]:
                min_index = j

        # Put the smallest value at position i
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


numbers = [5, 3, 8, 1, 2]

result = selection_sort(numbers)

print(result)