student = ["Kriti","Sapna","Shive","Disha","Subh"]

marks = [36,67,89,90,98]

print("Students:", student)
print("Marks:",marks)

import numpy as np

marks_array = np.array(marks)

total = np.sum(marks_array)
average = np.mean(marks_array)
highest = np.max(marks_array)
lowest = np.min(marks_array)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:",highest)
print("Lowest Marks:", lowest)

import pandas as pd

marks_series = pd.Series(marks, index=student)

print("\nStudent Marks:")
print(marks_series)

print("\nKriti's Marks:", marks_series["Kriti"])
print("Subh's Marks:", marks_series["Subh"])

passed_student = marks_series[marks_series > 70]

print("\n student scoring more then 70:")
print(passed_student)

average_student = marks_series[marks_series < 60]

print("\n Students scoring less then 60:")
print(average_student)

passed = marks_series[marks_series >= 40]
failed = marks_series[marks_series < 40]

print("\n Passed Students:")
print(passed)

print("Failed Students:")
print(failed)

percentage = (marks_series / 100)*100

print("/n Percentage:")
print(percentage)

subjects = ["Python", "English", "Computer", "Math's", "Science"]

student_marks = {

    "Akriti" : [95,89,85,80,90],
    "Neha" : [10,56,90,70,75],
    "Shreya" : [5, 78,54,40,30,],
    "Disha" :[45,60,80,96,80],
    "Priya" : [20,40,80,70,20],
    "Krish" : [80,90,67,50,45],
}

print("\nSubjects:")
print(subjects)
print("Student Marks:")
print(student_marks)

for student, marks in student_marks.items():
    marks_array = np.array(marks)

    total = np.sum(marks_array)
    average = np.mean(marks_array)

    if np.all(marks_array >= 40):
        result = "Pass"
    else:
        result = "Fail" 

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"

    else:
        grade = "D"   


    print("\n Student:", student)
    print("total:",total)
    print("Average:",average)
    print("Result:",result)
    print("Grade:", grade)