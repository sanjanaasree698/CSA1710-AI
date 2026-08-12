# Python Program to Illustrate Different Set Operations

# Creating Sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union
print("Union:", A.union(B))

# Intersection
print("Intersection:", A.intersection(B))

# Difference
print("A - B:", A.difference(B))
print("B - A:", B.difference(A))

# Symmetric Difference
print("Symmetric Difference:", A.symmetric_difference(B))

# Subset and Superset
print("A is subset of B:", A.issubset(B))
print("A is superset of B:", A.issuperset(B))

# Membership Test
print("3 in A:", 3 in A)
print("10 in B:", 10 in B)