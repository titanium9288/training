T, W = map(int, input().split())
tree = [0]

for i in range(T):
    tree.append(int(input()))

# 위치, 이동 횟수, 시간을 고려한 dp
dp = [[[0, 0, 0] for _ in range(W + 1)] for _ in range(T + 1)]

# 초기값 선언
# 1로 시작하면 움직일 필요 없음
if tree[1] == 1:
    dp[1][0][1] = 1

# 2로 시작했을 때 움직임 횟수 추가
if tree[1] == 2:
    dp[1][1][2] = 1


for i in range(2, T + 1):
    for j in range(W + 1):
        for pos in (1, 2):
            side = pos % 2 + 1

            # j가 0일 때 조심하기
            dp[i][j][pos] = max(
                dp[i - 1][j][pos], dp[i - 1][j - 1][side] if j > 0 else 0
            )
            if tree[i] == pos:
                dp[i][j][pos] += 1

print(max(map(max, dp[T])))
