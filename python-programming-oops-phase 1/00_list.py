
array = ["Hello",1,2,2,"Bon",2.4,True]

#access a list
print(array[0])
print(array[-4])

# lenght of list
print(len(array))

# slicing a list
print(array[1:len(array)])
print(array[2:len(array):3])

# adding a element
array.append("mango") # adds at end
array.append(["Apple",23]) # adds at end considers as 1 item
array.insert(0,"Boga")
print(array)


# add multiple values
array.extend([(0,"Alexa"),False,"Sop"])
print(array)

'''
# clear a list
l = array
print(l)
l.clear()
print(l)  
 '''

# reverse a list
print(array[::-1])
array.reverse()
print(array)

# count total 2
array.count(2)
print(array)

''' 
# sort the list
array.sort()
print(array)  # use when list is float or number
'''

# remove
array.pop()
print(array)
array.pop(2)
print(array)
array.remove("mango")
print(array)

arr = []
arr= array.copy()
print(arr)

