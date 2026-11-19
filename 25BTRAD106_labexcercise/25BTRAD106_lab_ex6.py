# Lab 6: Prime number and factorial programs

# ---------- Prime number check ----------
n = int(input("Enter a number to check prime: "))

if n < 2:
    print(n, "is not a prime number")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

# ---------- Factorial ----------
f = int(input("\nEnter a number to find factorial: "))

if f < 0:
    print("Factorial is not defined for negative numbers")
else:
    fact = 1
    for i in range(1, f + 1):
        fact = fact * i
    print("Factorial of", f, "is", fact)
