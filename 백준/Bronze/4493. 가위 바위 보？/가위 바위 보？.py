T = int(input())

RSP = {"R": 0, "S": 1, "P": 2}
RSP_SCORE = [0, -1, 1]
RESULT = ["Player 2", "TIE", "Player 1"]

for i in range(T):
    n = int(input())

    score = 0
    for _ in range(n):
        p1, p2 = (RSP[p] for p in input().split())
        score += RSP_SCORE[(p1 - p2 + 3) % 3]

    print(RESULT[(score > 0) - (score < 0) + 1])
