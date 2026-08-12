# Python Program to Demonstrate List Operations

# Nested List
list1 = [10, 20, [30, 40], 50]
print("Nested List:", list1)

# Length of List
print("Length of List:", len(list1))

# Concatenation
list2 = [60, 70]
concat_list = list1 + list2
print("Concatenated List:", concat_list)

# Membership
print("20 in list1:", 20 in list1)
print("100 in list1:", 100 in list1)

# Iteration
print("Elements in List:")
for item in list1:
    print(item)

# Indexing
print("First Element:", list1[0])
print("Third Element:", list1[2])

# Slicing
print("List from index 1 to 3:", list1[1:4])
print("First Three Elements:", list1[:3])
print("Elements from index 2 onwards:", list1[2:])