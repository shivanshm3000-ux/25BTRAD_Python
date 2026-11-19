# Mini Project 1: Unit Converter
# Converts length, weight and temperature.

def length_converter():
    print("\n1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Feet")
    print("4. Feet to Meters")
    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(value, "km =", round(value * 0.621371, 2), "miles")
    elif choice == "2":
        print(value, "miles =", round(value * 1.60934, 2), "km")
    elif choice == "3":
        print(value, "m =", round(value * 3.28084, 2), "feet")
    elif choice == "4":
        print(value, "feet =", round(value / 3.28084, 2), "m")
    else:
        print("Invalid choice")

def weight_converter():
    print("\n1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    print("3. Grams to Ounces")
    print("4. Ounces to Grams")
    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(value, "kg =", round(value * 2.20462, 2), "lb")
    elif choice == "2":
        print(value, "lb =", round(value / 2.20462, 2), "kg")
    elif choice == "3":
        print(value, "g =", round(value * 0.035274, 2), "oz")
    elif choice == "4":
        print(value, "oz =", round(value / 0.035274, 2), "g")
    else:
        print("Invalid choice")

def temperature_converter():
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose: ")
    value = float(input("Enter value: "))

    if choice == "1":
        print(value, "C =", round(value * 9 / 5 + 32, 2), "F")
    elif choice == "2":
        print(value, "F =", round((value - 32) * 5 / 9, 2), "C")
    elif choice == "3":
        print(value, "C =", round(value + 273.15, 2), "K")
    elif choice == "4":
        print(value, "K =", round(value - 273.15, 2), "C")
    else:
        print("Invalid choice")

while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")
    option = input("Enter your choice: ")

    if option == "1":
        length_converter()
    elif option == "2":
        weight_converter()
    elif option == "3":
        temperature_converter()
    elif option == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
