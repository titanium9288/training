N = int(input())
triangle = []

for i in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        current_value = triangle[i][j]
        from_above = triangle[i - 1][j] if j <= i - 1 else 0
        from_above_left = triangle[i - 1][j - 1] if j > 0 else 0

        triangle[i][j] = max(
            current_value + from_above, current_value + from_above_left
        )

print(max(triangle[-1]))
