tups = (10,20,30,40)
print(type(tups))

t = (10)
t1 = (10,)
print(type(t),type(t1))

list1 = [1,2,3.32,True]
string = "Heep Sheep Deep"
print(tuple(list1))
print(tuple(string))

# tuple packing and unpacking
tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)

