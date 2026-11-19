# Lab 10: Frequency counter using dictionaries

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

# Same logic works for a list, e.g. survey responses
responses = ["tea", "coffee", "tea", "juice", "coffee", "tea"]
count = {}
for r in responses:
    count[r] = count.get(r, 0) + 1

print("\nSurvey result:", count)
