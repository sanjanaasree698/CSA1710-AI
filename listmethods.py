# Python Program to Demonstrate List Methods
# Add (Insert), Append, Extend, and Delete

# Creating a List
numbers = [10, 20, 30]
print("Original List:", numbers)

# Add (Insert)
numbers.insert(1, 15)
print("After Insert:", numbers)

# Append
numbers.append(40)
print("After Append:", numbers)

# Extend
numbers.extend([50, 60, 70])
print("After Extend:", numbers)

# Delete an Element
del numbers[2]
print("After Delete:", numbers)