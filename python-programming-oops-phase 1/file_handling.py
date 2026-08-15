# -----------------------------------
# 1. WRITE - create/overwrite a file
# -----------------------------------

file = open("data.txt", "w")

file.write("Parth\n")
file.write("Data Analyst\n")
file.write("Python\n")

file.close()


# -----------------------------------
# 2. APPEND - add new content
# -----------------------------------

file = open("data.txt", "a")

file.write("SQL\n")
file.write("Power BI\n")

file.close()


# -----------------------------------
# 3. READ - read the complete file
# -----------------------------------

file = open("data.txt", "r")

content = file.read()

print("Complete file:")
print(content)

file.close()


# -----------------------------------
# 4. READLINES - get all lines
# -----------------------------------

file = open("data.txt", "r")

lines = file.readlines()

print("Lines:")
print(lines)

file.close()


# -----------------------------------
# 5. READ LINE BY LINE
# -----------------------------------

file = open("data.txt", "r")

for line in file:
    print("Line:", line.strip())

file.close()