def find_all_positions(numbers, target):

    positions = []

    for i in range(len(numbers)):

        if numbers[i] == target:
            positions.append(i)

    return positions


numbers = [12, 25, 7, 25, 30, 25, 15]

result = find_all_positions(numbers, 25)

print(result)