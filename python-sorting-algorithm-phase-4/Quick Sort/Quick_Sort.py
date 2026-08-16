def quick_sort(numbers):

    # Base case
    if len(numbers) <= 1:
        return numbers

    # Choose the last element as pivot
    pivot = numbers[-1]

    left = []
    middle = []
    right = []

    # Divide elements around the pivot
    for number in numbers:

        if number < pivot:
            left.append(number)

        elif number == pivot:
            middle.append(number)

        else:
            right.append(number)

    # Recursively sort left and right
    return quick_sort(left) + middle + quick_sort(right)


numbers = [5, 3, 8, 1, 2]

result = quick_sort(numbers)

print(result)