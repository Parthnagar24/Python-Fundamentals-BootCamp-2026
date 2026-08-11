#Print the first and last character of a string.
#Convert a sentence into title case.
#Remove extra spaces from a sentence.
name = input("Enter the name:").strip().title()
print(name)
print(name[0]) # print 1st character
print(name[-1]) # print last character

#Reverse a string using slicing.

rev = print(name[::-1])

#Count the number of vowels in a string.
countt1 = print(name.count("a")) 
countt2 = print(name.count("e"))
countt3 = print(name.count("i"))
countt4 = print(name.count("o"))
countt5= print(name.count("u"))

#Replace every space with _.
rep = print(name.replace(" ","_"))


#Extract the username from an email.

email = "abc123@gmail.com"
findd = email.find("@")
print(findd)
retrieve = email[0:6]
print(retrieve)   # but need to think a better approach here 

# 2nd approach 
email2 = "abc123@gmail.com"
mail = email2.split("@")
print(mail)
print(mail[0]) #usename
print(mail[-1]) #domain

#Check whether a file is a PDF.
file = input("Enter a filename:")
print(file.endswith(".pdf"))

#Print only the middle character of a string.

x = "bobby"
x2 = x[1:5:2]
print(x2) # odd 

# 16

email = "  aplead@ffaf.com  "
print(email.strip())

#17

print("data analyst".replace(" ","_"))

# 18 - 19 -20
print("Python Programming".lower())
print("Python Programming".upper())
print("Python Programming".capitalize())