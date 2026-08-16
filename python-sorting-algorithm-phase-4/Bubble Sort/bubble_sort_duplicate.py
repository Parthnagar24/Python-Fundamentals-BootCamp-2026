def bubble_sort(numbers):

    n = len(numbers)

    # Each pass puts the largest unsorted value at the end
    for i in range(n):

        # Compare adjacent elements
        for j in range(0, n - i - 1):

            # If left element is bigger, swap them
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


numbers = [5, 2, 5, 1, 2]

result = bubble_sort(numbers)

print(result)