N, M = map(int, input().split())

matrix_a = []
for i in range(N):
    matrix_a.append(list(map(int, input().split())))

matrix_b = []
for i in range(N):
    matrix_b.append(list(map(int, input().split())))

result = [[0 for _ in range(M)] for _ in range(N)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in result:
    print(*row)
