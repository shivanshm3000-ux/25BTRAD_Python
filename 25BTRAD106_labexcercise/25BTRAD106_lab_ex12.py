# Lab 12: Student data manager using files
# Each line in students.txt:  roll,name,marks
import os

filename = "students.txt"

if not os.path.exists(filename):
    open(filename, "w").close()

def add_student():
    roll = input("Roll no: ")
    name = input("Name: ")
    marks = input("Marks: ")
    if not marks.isdigit():
        print("Marks must be a number.")
        return
    with open(filename, "a") as f:
        f.write(roll + "," + name + "," + marks + "\n")
    print("Student added.")

def display_students():
    with open(filename, "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        print("No records found.")
    for line in lines:
        roll, name, marks = line.strip().split(",")
        print("Roll:", roll, "| Name:", name, "| Marks:", marks)

def search_student():
    roll = input("Enter roll no to search: ")
    with open(filename, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Found -> Name:", data[1], "| Marks:", data[2])
                return
    print("Student not found.")

def update_student():
    roll = input("Enter roll no to update: ")
    found = False
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            if data[0] == roll:
                new_marks = input("Enter new marks: ")
                f.write(data[0] + "," + data[1] + "," + new_marks + "\n")
                found = True
            else:
                f.write(line)
    print("Record updated." if found else "Student not found.")

while True:
    print("\n1.Add  2.Display  3.Search  4.Update  5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
