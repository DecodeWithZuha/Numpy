#This is a small project for just practicing Numpy Basics.

import numpy as np

#So, Class_05 consists of 5 students,[Zuha, Alishba, Fajar, Aleeza, Muneeza]. 
# All study 4 subjects, [ Programming, Maths, Physics, English]

Students = np.array([ "Zuha" , "Alishba", "Fajar", "Aleeza", "Muneeza" ])

Marks = np.array([
    #Pr, Ma, Ph, En
    [90, 95, 90, 88], #Zuha
    [72, 95, 85, 85], #Alishba
    [15, 85, 90, 32], #Fajar
    [85, 42, 92, 31], #Aleeza
    [13, 57, 67, 40]  #Muneeza
])

#.shape to get the shape of array
print("Class Students Shape:" , Students.shape)
print("Students Marks Shape:" , Marks.shape)

#Extracting Physics Marks of all students from the data
print("Physics Marks:" , Marks[: , 2])

#Extracting Aleeza's Marks for all subjects
print("Aleeza's Marks:" , Marks[3 , :])

#Extracting Fajar's English Marks
print("Fajar's English Marks:" , Marks[2 , 3])

#Extracting Zuha's , Alishba's & Aleeza's Marks for Maths & English
print("Zuha's, Alishba's & Aleeza's marks for Maths & English are:" , Marks[[0,1,3]][:,[1,3]]) 
#Marks[0,1,3]--> new matrix --> [90, 65, 70, 88], Zuha
#                               [72, 95, 85, 65], Alishba
#                               [75, 62, 92, 81], Aleeza
#Now on this new matrix the expression[:,[1,3]] will be applied to get desired output

# What are the highest scored numbers all Subjects
print("Maximum scores in Subjects", np.max(Marks, axis=0))

# What is the highest marks, scored by each student
print("Highest marks scored by each student in all subjects", np.max(Marks, axis=1))

# Average score in each subject
print("Average score in each subject", np.mean(Marks, axis=0))

# Find minimum score in Physics
Phy_Marks= Marks[: , 2]
print("Minimum Marks in Physics:" , np.min(Phy_Marks))

#Who scored Maximum Marks in Programming
Prog_Marks = Marks[: , 0]
Max_Index = np.argmax(Prog_Marks)
print(Students[Max_Index] ,"has scored the highest marks in programming")

#What & who scored minimum marks in Maths
Maths_Marks = Marks[: , 1]
Min_Index = np.argmin(Maths_Marks)
print(Students[Min_Index], "has scored the lowest marks of " , Maths_Marks[Min_Index], " in Maths")

#Now calculating total result for Class 05 & Finding out who topped in class & who got last position
Average_Marks = np.mean(Marks , axis=1)
Topper_Marks = np.max(Average_Marks)
Topper_Indexes = np.where(Average_Marks == Topper_Marks)[0] #np.where() returns a tuple eg: ([1,4],) toh agr [0] add krein toh woh extra wrapper ko remove kr deta hy, aur ab neeche topper aur failed main brackets ni aa rhi
Losser_Marks = np.min(Average_Marks)
Losser_Indexes = np.where(Average_Marks == Losser_Marks)[0]

for i in range(len(Students)):
    Average = np.mean(Marks[i]) #idhr Marks[i]--> yeh row wise hi niklay ga mean, q k 1d array create hua hy
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

    print(Students[i] , "Average: ", Average , "Grade: ",grade)

# Finding who topped & who failed
for i in Topper_Indexes:
    print(Students[i] , "has scored 1st Position in Class with a score of " , np.mean(Marks[i]))

for j in Losser_Indexes:
    print(Students[j] , "has Failed in Class with a score of " , np.mean(Marks[j]))

#Extract data as per positions
Student_Positions = np.argsort(Average_Marks)[::-1]
j=1
for i in Student_Positions:
    print(Students[i], "has scored" , j , "position in Class, with a score of ", np.mean(Marks[i]))
    j += 1