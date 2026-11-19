# Lab 9: Student grading system using dictionaries

students = {}

n = int(input("How many students? "))
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks (0-100): "))
    students[name] = marks

def get_grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

print("\nName\tMarks\tGrade")
for name, marks in students.items():
    print(name, "\t", marks, "\t", get_grade(marks))

# Sample test cases: 95->A+, 85->A, 75->B, 65->C, 55->D, 30->F
