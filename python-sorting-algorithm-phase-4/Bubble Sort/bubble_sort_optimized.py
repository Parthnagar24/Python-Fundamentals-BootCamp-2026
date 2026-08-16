def bubble_sort(numbers):

    n = len(numbers)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

                swapped = True

        # If no swap happened, list is already sorted
        if swapped == False:
            break

    return numbers


numbers = [1, 2, 3, 4, 5]

result = bubble_sort(numbers)

print(result)