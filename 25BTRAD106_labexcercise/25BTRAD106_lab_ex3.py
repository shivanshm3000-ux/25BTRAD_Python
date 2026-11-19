# Lab 3: Variables, operators, and input/output
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b if b != 0 else "Cannot divide by zero")
print("Floor division :", a // b if b != 0 else "Cannot divide by zero")
print("Modulus        :", a % b if b != 0 else "Cannot divide by zero")
print("Power          :", a ** b)

print("a > b  :", a > b)
print("a == b :", a == b)
