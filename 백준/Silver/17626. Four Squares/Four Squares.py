N = int(input())

squares = []
dp = [0] + [float("inf")] * N

# squares 초기화
for i in range(1, N + 1):
    square = i * i
    if square > N:
        break

    squares.append(square)

# dp 계산
for i in range(1, N + 1):

    for square in squares:
        if i < square:
            break

        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[N])
