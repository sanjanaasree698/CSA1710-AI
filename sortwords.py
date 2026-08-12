# Python Program to Sort Words in a Sentence Alphabetically

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Sort words alphabetically
words.sort()

print("Words in Alphabetical Order:")
for word in words:
    print(word)