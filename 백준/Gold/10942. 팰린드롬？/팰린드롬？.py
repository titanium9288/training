import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 길이와 시작 점을 잡고, 팰린드롬인지 확인하는 dp
dp = [[0] * N for _ in range(N)]

for length in range(1, N + 1):
    for start in range(0, N - length + 1):
        end = start + length - 1

        if length == 1:
            dp[start][end] = 1
            continue

        if length == 2:
            if arr[start] == arr[end]:
                dp[start][end] = 1
            continue

        if arr[start] == arr[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
