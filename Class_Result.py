import numpy as np

n = int(input("How many students? "))
subjects = int(input("How many subjects? "))

Students = []
Marks = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    Students.append(name)

    student_marks = []
    for j in range(subjects):
        m = float(input(f"Enter marks of subject {j+1}: "))
        student_marks.append(m)

    Marks.append(student_marks)