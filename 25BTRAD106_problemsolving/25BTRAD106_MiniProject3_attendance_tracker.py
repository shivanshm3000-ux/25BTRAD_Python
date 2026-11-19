# Mini Project 3: Attendance Tracker
# Each student is stored as: {"name": ..., "present": ..., "total": ...}
# All students are kept in a list.

students = []

def find_student(name):
    for s in students:
        if s["name"].lower() == name.lower():
            return s
    return None

def add_student():
    name = input("Enter student name: ")
    if find_student(name) is not None:
        print("Student already exists.")
        return
    students.append({"name": name, "present": 0, "total": 0})
    print("Student added.")

def mark_attendance():
    name = input("Enter student name: ")
    s = find_student(name)
    if s is None:
        print("Student not found.")
        return
    status = input("Present or Absent? (P/A): ").upper()
    if status == "P":
        s["present"] += 1
        s["total"] += 1
        print("Marked present.")
    elif status == "A":
        s["total"] += 1
        print("Marked absent.")
    else:
        print("Invalid status.")

def percentage(s):
    if s["total"] == 0:
        return 0
    return s["present"] / s["total"] * 100

def display_attendance():
    if len(students) == 0:
        print("No students added.")
        return
    print("\nName\t\tPresent\tTotal\tPercentage")
    for s in students:
        print(s["name"], "\t\t", s["present"], "\t", s["total"], "\t", round(percentage(s), 2), "%")

def low_attendance():
    limit = float(input("Enter attendance threshold (%): "))
    found = False
    print("\nStudents below", limit, "%:")
    for s in students:
        if s["total"] > 0 and percentage(s) < limit:
            print(s["name"], "-", round(percentage(s), 2), "%")
            found = True
    if not found:
        print("No student is below the threshold.")

while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add student")
    print("2. Mark attendance")
    print("3. Display attendance")
    print("4. Show students below threshold")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        display_attendance()
    elif choice == "4":
        low_attendance()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
