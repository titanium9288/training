N = int(input())
stair_list = [0]

for i in range(N):
    stair_list.append(int(input()))

dp = [[0, 0] for _ in range(N + 1)]
dp[1] = [stair_list[1], stair_list[1]]
if N > 1:
    dp[2] = [stair_list[2], stair_list[1] + stair_list[2]]


for i in range(3, N + 1):
    # 기존 코드를 보니, 아예 접근을 잘못 하고 있었음.
    # 기준을 세칸 연속으로 올라갈 수 없음에 잡고 코드를 작성했음.

    dp[i][0] = max(dp[i - 3]) + stair_list[i - 1] + stair_list[i]
    dp[i][1] = max(dp[i - 2]) + stair_list[i]

print(max(dp[-1]))
