# string methods in 1 code

name = " alexander the great"

# accessing the characters of name 
print(name[2])  # l
print(name[-4]) # r

# lenght of a string
print(len(name))

# slicing - to retrive specific part from a string
print(name[0:])          # alexander the great
print(name[0:len(name)]) # alexander the great 
print(name[:len(name)])  # alexander the great

# look  whether the string ends with a t
print(name.endswith("t"))  #True
# look whether the string ends with a T
print(name.endswith("T"))  # False - because string is case -sensitive
# look whether the string starts with space
print(name.startswith(" ")) # True

# start from beginning and go till end but give 3 character jump
print(name[0:len(name):3])  #  enrhga

# delete a string
name2 = "Alexa"
del name2

print(name.replace(" ","?"))

# find the index of e
print(name.find("e"))
print(name.index("e"))