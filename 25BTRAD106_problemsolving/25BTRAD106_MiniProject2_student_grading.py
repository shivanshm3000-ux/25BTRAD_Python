# Mini Project 2: Student Grading Automation
# Stores marks of 3 subjects per student, then calculates
# total, percentage and grade automatically.

students = {}

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def read_marks(subject):
    while True:
        marks = int(input("Enter " + subject + " marks (0-100): "))
        if 0 <= marks <= 100:
            return marks
        print("Invalid marks! Enter between 0 and 100.")

n = int(input("How many students? "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Enter name: ")
    m1 = read_marks("Subject 1")
    m2 = read_marks("Subject 2")
    m3 = read_marks("Subject 3")

    total = m1 + m2 + m3
    percentage = total / 3
    students[name] = {"total": total, "percentage": percentage, "grade": get_grade(percentage)}

print("\n=========== RESULT SHEET ===========")
print("Name\t\tTotal\tPercent\tGrade")
for name, data in students.items():
    print(name, "\t\t", data["total"], "\t", round(data["percentage"], 2), "\t", data["grade"])

# Topper and class average
topper = max(students, key=lambda s: students[s]["total"])
average = sum(d["percentage"] for d in students.values()) / len(students)

print("\nTopper        :", topper, "with", students[topper]["total"], "marks")
print("Class average :", round(average, 2), "%")
