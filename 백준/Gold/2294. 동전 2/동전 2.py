N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] + ([float("inf")] * K)

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

answer = dp[K]
if answer == float("inf"):
    print(-1)
else:
    print(answer)