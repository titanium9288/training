N = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[float("inf")] * N for _ in range(N)]

# 같은 위치의 행렬곱에 대해 초기화
for i in range(N):
    dp[i][i] = 0

# 처음엔 i j k 3중 루프로 했었는데,
# 작은 구간부터 dp를 확장해야하는 문제였음.
for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        for k in range(i, j):
            cost = matrix[i][0] * matrix[k][1] * matrix[j][1]
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)

print(dp[0][N - 1])
