friends = ["Apple","Orange",7,3.32,False,"banana"]
print("original list",friends)

friends.append("Mango")
print("List after appending",friends)

friends.insert(2,"Pineapple")
print("List after inserting",friends)

friends.remove("Orange")
print("List after removing",friends)

friends.remove(7)
print("List after removing",friends)

hello = [0,2,31,1,31,33,444]
hello.sort()
print("List after sorting",hello)


friends.reverse()
print("List after reversing",friends)

friends.extend(hello)
print("List after extending",friends)

friends.pop(3)
print(friends)

hello.clear()
print(hello)


list = [ 1,2,2,3,4]
list2 = list.copy()
print(list2)


list4 =list.index(3)
print(list4)

list3 = list.count(2)
print(list3)