def linear_search(numbers,target):
    
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
        
    return -1

numbers = [12, 7, 20, 15, 30, 9]
result = linear_search(numbers,30)
print(result)




