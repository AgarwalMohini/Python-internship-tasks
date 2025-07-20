#Matrix addition

# Input dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
mat1 = []
for i in range(rows):
    mat1.append(list(map(int, input().split())))

print("Enter elements of second matrix:")
mat2 = []
for i in range(rows):
    mat2.append(list(map(int, input().split())))

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Resultant matrix after addition:")
for row in result:
    print(*row)
