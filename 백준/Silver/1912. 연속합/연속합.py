N = int(input())
array = list(map(int, input().split()))
dp = [array[0]] + [0] * (N - 1)

for i in range(1, N):
    dp[i] = max(dp[i - 1] + array[i], array[i])

print(max(dp))