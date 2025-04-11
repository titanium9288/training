import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()


# 투 포인터 적용
start_right = 0
min_diff = float("inf")

for left in range(N):
    for right in range(start_right, N):
        diff = A[right] - A[left]

        if diff >= M:
            min_diff = min(min_diff, diff)
            start_right = right
            break

print(min_diff)
