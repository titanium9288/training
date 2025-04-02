N = int(input())

# 아무것도 안 채운 상황을 1로 본다면,
# 점화식을 깔끔하게 유도할 수 있음
dp = [1] + ([0] * N)


for i in range(2, N + 1, 2):
    dp[i] += dp[i - 2] * 3

    # 0이 아니네......
    for j in range(i - 4, -1, -2):
        dp[i] += dp[j] * 2

print(dp[N])
