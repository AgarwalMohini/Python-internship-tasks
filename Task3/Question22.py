#Matrix multiplication

# Input dimensions
rows_A = int(input("Enter number of rows in Matrix A: "))
cols_A = int(input("Enter number of columns in Matrix A: "))
rows_B = int(input("Enter number of rows in Matrix B: "))
cols_B = int(input("Enter number of columns in Matrix B: "))

if cols_A != rows_B:
    print("Matrix multiplication not possible!")
else:
    print("Enter elements of Matrix A:")
    A = []
    for _ in range(rows_A):
        A.append(list(map(int, input().split())))

    print("Enter elements of Matrix B:")
    B = []
    for _ in range(rows_B):
        B.append(list(map(int, input().split())))

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A): 
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix (A x B):")
    for row in result:
        print(*row)
