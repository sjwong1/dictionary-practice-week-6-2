# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
print(len(students))
print(students[0]["Combo,Name"])
print(students[0]["Email"][0])
print(students[0]["Email"][1])
print(students[0]["CPSID"])


print(students[1]["Combo,Name"])
print(students[1]["Email"][1])
print(students[1]["CPSID"])

print(students[2]["Combo,Name"])
print(students[2]["Email"][1])
print(students[2]["CPSID"])

#for loops allow us to illterate data through the data and perform some function. 
for student in students: 
  print(student["Combo,Name"])
  print(student["Email"][0])
  print(student["Email"][1])
  print(student["CPSID"])
  
  print("_"*25)