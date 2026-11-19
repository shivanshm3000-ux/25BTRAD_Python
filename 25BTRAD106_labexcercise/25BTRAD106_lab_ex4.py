# Lab 4: Simple calculator and area calculation

# ---------- Simple Calculator ----------
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result =", num1 + num2)
elif op == "-":
    print("Result =", num1 - num2)
elif op == "*":
    print("Result =", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# ---------- Area Calculation ----------
print("\n=== Area Calculator ===")
print("1. Circle  2. Rectangle  3. Triangle")
choice = int(input("Choose a shape: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area =", 3.14159 * r * r)
elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area =", l * w)
elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area =", 0.5 * b * h)
else:
    print("Invalid choice")
