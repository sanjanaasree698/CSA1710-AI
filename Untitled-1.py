# Simple Calculator Program

print("Simple Calculator - Untitled-1.py:3")
print("1. Addition - Untitled-1.py:4")
print("2. Subtraction - Untitled-1.py:5")
print("3. Multiplication - Untitled-1.py:6")
print("4. Division - Untitled-1.py:7")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result = - Untitled-1.py:15", num1 + num2)

elif choice == '2':
    print("Result = - Untitled-1.py:18", num1 - num2)

elif choice == '3':
    print("Result = - Untitled-1.py:21", num1 * num2)

elif choice == '4':
    if num2 != 0:
        print("Result = - Untitled-1.py:25", num1 / num2)
    else:
        print("Error! Division by zero is not allowed. - Untitled-1.py:27")

else:
    print("Invalid choice! Please select 1, 2, 3, or 4. - Untitled-1.py:30")