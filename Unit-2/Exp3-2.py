matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

print("Row sums:")
for i in range(rows):
    print(f"Row {i}:", sum(matrix[i]))

print("\nColumn sums:")
for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    print(f"Column {j}:", s)

key = 5
found = False

print("\nSearch result:")
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == key:
            print(f"Found at ({i}, {j})")
            found = True

if not found:
    print("Not found")

print("\nTranspose:")
for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()