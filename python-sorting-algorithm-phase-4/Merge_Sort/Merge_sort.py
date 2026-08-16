def merge_sort(numbers):

    # Base case: a list with 0 or 1 element is already sorted
    if len(numbers) <= 1:
        return numbers

    # Find the middle
    middle = len(numbers) // 2

    # Divide the list into two halves
    left = numbers[:middle]
    right = numbers[middle:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    # Add remaining elements from left
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements from right
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


numbers = [5, 3, 8, 1, 2]

result = merge_sort(numbers)

print(result)