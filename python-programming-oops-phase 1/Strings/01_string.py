name = "Alexander"
city = 'Kolkata'
Sentence = """Python is a boy"""
word = 'Python is a girl'


print(f"{name}, {city},{Sentence},{word}")

# Immutability check

name = "Blexander"
print(name)  # this shows python is dynamically typed language

# instead of modification we can create a new string


# print 1st character of a string
print(name[0])
# print last character of a string
print(name[-1])

# slicing - to get a specific portion of a string
new_name = "Bob"

sliced_1 = print(new_name[0:3])
sliced_2 = print(new_name[1:2])
sliced_3 = print(new_name[0:3:2])

# reverse a string

rev = "reve rse"
print(rev[::-1])
print(rev[::-2])
print(rev[::-4])

# capitalize the string
rev2 = print(rev.upper())
#smaller the string
rev3 = print(rev.lower())

#title 1st character capitalize
print("data analyst role".title())

# just the 1st character of a string needs to be capitalize
print(rev.capitalize())

# lenght of a string
print(len(rev))

# print string without trailing or widespace

var = " The boy is a goo  d boy "
print(var)
print(var.strip())

# replace a word in the sentence

text = "I love Java"
print(text)
text2 = text.replace("Java", "Python")
print(text2)

# split data

skills = "SQL,Python,Excel"
print(skills)
skill = skills.split(",")
print(skill)


# reverse the above split

skill2 = ["SQL","Python","Excel"]

skill3 = ",".join(skill2)
print(skill3)

# find and index

email = "abc@gmail.com"
email2 =email.find("@")
print(email2)

email3 = "abcgmail.com"
email4 = email3.find("@")
print(email4)

# check if it starts with a string or character or not

print("report.pdf".startswith("report"))
print("report.pdf".endswith(".pdf"))

#count 

print("banana".count("a"))

