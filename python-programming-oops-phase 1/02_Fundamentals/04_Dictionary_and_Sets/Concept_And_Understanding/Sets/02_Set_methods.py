s = {1,4,3,1,32,4,4,"Alexa "}
print(s,type(s))

s.add(566)
print(s,type(s))

e = len(s)
print(e)

s.remove(1)
print(s)

s = {1,4,3,1,32,4,4,"Alexa "}
s1 ={"alexa","bobby",4}
print(s.union(s1))
print(s.intersection(s1))