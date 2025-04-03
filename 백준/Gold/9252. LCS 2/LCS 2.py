str1 = input()
str2 = input()
N, M = len(str1), len(str2)

dp = [[0] * (M + 1) for _ in range(N + 1)]
path = [[(0, 0) for _ in range(M + 1)] for _ in range(N + 1)]

# DP와 추적용 경로를 같이 저장
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            path[i][j] = (-1, -1)
        elif dp[i - 1][j] >= dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j]
            path[i][j] = (-1, 0)
        else:
            dp[i][j] = dp[i][j - 1]
            path[i][j] = (0, -1)

print(max(map(max, dp)))

# 경로 역산
r, c = N, M
partial_str = ""

while True:
    dr, dc = path[r][c]
    nr = r + dr
    nc = c + dc

    if dr == -1 and dc == -1:
        partial_str += str1[r - 1]
    elif dr == 0 and dc == 0:
        break

    r, c = nr, nc

# 문자열이 거꾸로 나오니까 뒤집어서
print(partial_str[::-1])
