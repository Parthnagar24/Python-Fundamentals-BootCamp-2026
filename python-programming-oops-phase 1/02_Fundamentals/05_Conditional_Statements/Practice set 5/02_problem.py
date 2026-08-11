marks1 = float(input("Enter marks of subject 1:"))
marks2 = float(input("Enter marks of subject 2:"))
marks3 = float(input("Enter marks of subject 3:"))

#total percentage
total_percentage = (100) *(marks1 +marks2 +marks3)/300

if total_percentage >=40 and marks1 > 33 and marks2> 33 and marks3 > 33:
    print("You are passed",total_percentage)
else:
    print("u failed")