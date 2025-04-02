N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [1] + ([0] * K)

for coin in coins:
    for i in range(coin, K + 1):
        dp[i] += dp[i - coin]

print(dp[K])
