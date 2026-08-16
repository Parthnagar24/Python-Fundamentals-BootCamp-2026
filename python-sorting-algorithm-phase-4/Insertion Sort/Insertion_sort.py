def insertion_sort(numbers):

    n = len(numbers)

    # Start from index 1 because index 0 is already considered sorted
    for i in range(1, n):

        # Store the current value
        key = numbers[i]

        # Start comparing with the element just before key
        j = i - 1

        # Move larger elements one position to the right
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        # Put key in its correct position
        numbers[j + 1] = key

    return numbers


numbers = [5, 3, 8, 1, 2]

result = insertion_sort(numbers)

print(result)