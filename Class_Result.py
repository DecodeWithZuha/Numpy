import numpy as np

n = int(input("How many students? "))
s = int(input("How many subjects? "))

Students = []
Subjects =[]
Marks = []
Grades = []

for i in range(s):
    sub = input(f"Enter name of Subject {i+1}: ")
    Subjects.append(sub)

for i in range(n):
    name = input(f"Enter name of Student {i+1}: ")
    Students.append(name)

    student_marks = []
    for Subject in Subjects:
        m = float(input(f"Enter marks of {name} in {Subject}: "))
        student_marks.append(m)

    Marks.append(student_marks)

average_marks = np.mean(Marks, axis = 1)
topper_index = np.where(average_marks == (np.max(average_marks)))[0]
losser_index = np.where(average_marks == (np.min(average_marks)))[0]

def std_grade():
    std = []
    s = int(input("How many Students?"))

    for i in range(s):
        name = input(f"Enter name of Student {i+1}: ")
        std.append(name)
    
    for s in std:
        if s in Students:
            index = list(Students).index(s)
            print(Students[index] , "Grade: ",Grades[index])
        else:
            print(s , "does not exist")

for i in range(len(Students)):
    Average = np.mean(Marks[i]) 
    if(Average >= 95):
                grade = 'A+'
    elif(Average >= 90):
                grade = 'A-'
    elif(Average >= 85):
                grade = 'B+'
    elif(Average >= 80):
                grade = 'B-'
    elif(Average >= 75):
                grade = 'C+'
    elif(Average >= 70):
                grade = 'C-'
    elif(Average >= 65):
                grade = 'D+'
    elif(Average >= 60):
                grade = 'D-'
    elif(Average >= 55):
                grade = 'E+'
    elif(Average >= 50):
                grade = 'E-'
    else:
                grade = 'F'

    Grades.append(grade)

def grades():
    for i in range(len(Students)):
        print(Students[i] , "Average: ", np.mean(Marks[i]) , "Grade: ",Grades[i])

def topper():
    for i in topper_index:
        print(Students[i] , "has scored 1st Position in Class with a score of " , np.mean(Marks[i]))

def top_3_positions():
    Student_Positions = np.argsort(average_marks)[::-1]
    j = 1
    for i in Student_Positions:
        if (j <= 3):
            print(Students[i], "has scored" , j , "position in Class, with a score of ", np.mean(Marks[i]))
            j = j + 1

def failed_students():
    print("Failed Students: ")
    for i in range(len(Grades)):
        if Grades[i] == 'F':
            print(Students[i])

q = int(input("Please select one from below options: \n"
              "1- List the grades of all students \n"
              "2- List grade of specific student \n"
              "3- List who scored highest position in class \n"
              "4- Who got 1st 3 positions in the class \n"
              "5- List of students who failed \n"
              "0- End \n"))

while (q != 0):

    if (q == 1):
        grades()

    elif (q == 2):
        std_grade()

    elif (q == 3):
        topper()

    elif (q == 4):
        top_3_positions()

    elif (q == 5):
        failed_students()

    else:
        print("Invalid Entry. Try Again")

    q = int(input("\nSelect again (0 to exit): "))

print("Byeeeee")