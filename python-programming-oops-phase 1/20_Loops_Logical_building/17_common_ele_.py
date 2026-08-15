list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 9]

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)
        print(list3)
print(list3)