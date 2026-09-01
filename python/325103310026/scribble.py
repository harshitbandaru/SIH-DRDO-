rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Enter element [{i}][{j}]: ")))
    matrix.append(row)

print(matrix)


