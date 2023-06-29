matrix_9_by_9 = []
for i in range(9):
    matrix_9_by_9.append(list(map(int, input().split())))

max_value = max([max(i) for i in matrix_9_by_9])
for i in range(9):
    if max_value in matrix_9_by_9[i]:
        print(max_value)
        print(i + 1, matrix_9_by_9[i].index(max_value) + 1)
        break
