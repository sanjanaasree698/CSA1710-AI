# Python Program to Add Two Matrices

# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# First Matrix
print("Enter elements of First Matrix:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)

# Second Matrix
print("Enter elements of Second Matrix:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A
    B.append(row)

# Addition of Matrices
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    result.append(row)

# Display Result
print("Sum of Matrices:")
for row in result:
    print(row)