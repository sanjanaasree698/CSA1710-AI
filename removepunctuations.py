# Python Program to Remove Punctuations from a String

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

string = input("Enter a string: ")

result = ""

for char in string:
    if char not in punctuations:
        result += char

print("String after removing punctuations:")
print(result)