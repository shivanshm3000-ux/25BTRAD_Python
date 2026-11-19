# Lab 16: Dice simulator using random module
import random

# ---------- Roll dice repeatedly ----------
while True:
    dice = int(input("How many dice to roll? "))
    rolls = [random.randint(1, 6) for i in range(dice)]
    print("You rolled:", rolls, "| Total:", sum(rolls))

    again = input("Roll again? (y/n): ")
    if again.lower() != "y":
        break

# ---------- Frequency analysis ----------
trials = 600
frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(trials):
    frequency[random.randint(1, 6)] += 1

print("\nFrequency after", trials, "rolls:")
for face, count in frequency.items():
    print(face, ":", count, "(", round(count / trials * 100, 1), "% )")

# Each face should be close to 16.7% (1/6) - the more rolls, the closer it gets.
