import sys

N, Q = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0] * (N * 2)

for _ in range(Q):
    start, end = map(int, sys.stdin.readline().split())

    prefix_sum[start] += 1
    prefix_sum[end + 1] -= 1

for i in range(1, N + 1):
    prefix_sum[i] += prefix_sum[i - 1]

answer = 0
# 홀수만 XOR
for i in range(1, N + 1):
    if prefix_sum[i] % 2 == 1:
        answer ^= numbers[i - 1]

print(answer)
