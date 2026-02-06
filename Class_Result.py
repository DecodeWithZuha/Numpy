import numpy as np

n = int(input("How many students? "))
s = int(input("How many subjects? "))

Students = []
Subjects =[]
Marks = []

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

q = int(input("Please select one from below options: \n 1- List the grades of all students \n 2- List grade of specific student \n 3- List who scored highest position in class \n 4- Who got 1st 3 positions in the class \n 5- List of students who failed \n 6- List of student who failed in specific subject \n 7- list of all the students who failed in any subject"))

if (q == 1):
    
